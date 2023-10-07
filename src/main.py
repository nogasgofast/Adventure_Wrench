#!/bin/env python

import sys, os
import requests
import configparser
from ui.Main_Window import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, QMainWindow,
                              QWidget, QListWidgetItem,
                              QMessageBox, QFileDialog)
from PySide6.QtGui import QBrush, QColor, QFont
from pony.orm import db_session, commit
from lib.aw_db import database_factory
from Player import PlayerDialog
from Vault import VaultDialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # read config
        self.db = database_factory()
        self.config_setup()

        # initialize views.
        self.ui_vault = VaultDialog(self)
        self.ui_p = PlayerDialog(self)
        self.suppress_spinbox_update = False
        self.ui_p.setModal(True)

        # connect views to button logic
        self.ui.pushButton_switch_game.clicked.connect(self.switch_game)
        self.ui.pushButton_vault.clicked.connect(self.ui_vault.show)
        self.ui.pushButton_players.clicked.connect(self.ui_p.add_player)
        self.ui.pushButton_Inititave.clicked.connect(self.advance_initiative)
        self.ui.pushButton_toggle_expand.clicked.connect(self.toggle_expand)
        self.ui.pushButton_heal_1.clicked.connect(lambda: self.change_hp(1))
        self.ui.pushButton_heal_3.clicked.connect(lambda: self.change_hp(3))
        self.ui.pushButton_heal_5.clicked.connect(lambda: self.change_hp(5))
        self.ui.pushButton_heal_10.clicked.connect(
                            lambda: self.change_hp(10))
        self.ui.pushButton_dam_1.clicked.connect(lambda: self.change_hp(-1))
        self.ui.pushButton_dam_3.clicked.connect(lambda: self.change_hp(-3))
        self.ui.pushButton_dam_5.clicked.connect(lambda: self.change_hp(-5))
        self.ui.pushButton_dam_10.clicked.connect(
                            lambda: self.change_hp(-10))
        self.ui.pushButton_b_star.clicked.connect(
                            lambda: self.update_icon('black_star', 6))
        self.ui.pushButton_w_star.clicked.connect(
                            lambda: self.update_icon('white_star', 6))
        self.ui.pushButton_cross.clicked.connect(
                            lambda: self.update_icon('death_save_fail', 3))
        self.ui.pushButton_check.clicked.connect(
                            lambda: self.update_icon('death_save_success', 3))
        self.ui.pushButton_kill.clicked.connect(self.kill)
        self.ui.pushButton_remove.clicked.connect(self.remove)

        self.ui.listWidget_Encounter.itemDoubleClicked.connect(self.ui_p.update_player)
        self.ui.listWidget_Encounter.itemSelectionChanged.connect(
                                    self.spinBox_update)

        self.ui.spinBox_main_initiative.valueChanged.connect(
                                    self.update_initiative)
        self.ui.spinBox_main_hp.valueChanged.connect(
                                    self.update_hp)

        self.check_version()
        self.load_session()


    def config_setup(self):
        self.config_name = 'awconfig.ini'
        self.db_default_name = 'save/default.sqlite'
        self.config_file = configparser.ConfigParser()
        self.config_file.read(self.config_name)

        if 'Game' in self.config_file:
            db_file = self.config_file['Game']['db']
        else:
            # make default configs/database name
            try:
                os.mkdir('save')
            except FileExistsError:
                pass
            self.config_file['Game'] = { 'db': self.db_default_name }
            with open(self.config_name, 'w') as fh:
                self.config_file.write(fh)
            db_file = self.db_default_name
        try:
            # connect to database and try to create missing items if needed.
            self.db.bind(provider="sqlite", filename=db_file, create_db=True)
            self.db.generate_mapping(create_tables=True)
        except Exception as e:
            print("aw_db.sqlite Failed to load: {e}")
            raise e

        # Setting the game name based on the save file name.
        game_name = os.path.basename(db_file)
        game_name = os.path.splitext(game_name)[0]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_current_game.setText(f'Current Game: {game_name}')

    def switch_game(self):
        file_name, filtered_by = QFileDialog.getOpenFileName(self,
                                                 "Switch Game",
                                                 './save',
                                                 "sqlite databases (*.sqlite)")
        if file_name:
            # use relative path.
            file_name = os.path.basename(file_name)
            relative_path = f'save/{file_name}'
            try:
                # print(file_name)
                self.config_file['Game'] = { 'db': relative_path }
                with open(self.config_name, 'w') as fh:
                    self.config_file.write(fh)
                try:
                    self.ui_p.close()
                    self.ui_vault.close()
                    del(self.db)
                    self.db = database_factory()
                    self.db.bind(provider="sqlite",
                               filename=relative_path,
                               create_db=False)
                    self.db.generate_mapping(create_tables=False)
                except Exception as e:
                    print("aw_db.sqlite Failed to load: {e}")
                    raise e
                self.ui_vault.load_vault()
                self.ui_vault.ui_acadamy.load_acadamy()
                self.load_session()
                # just use the name not the extention here
                game_name = os.path.splitext(file_name)[0]
                self.ui.label_current_game.setText(f'Current Game: {game_name}')
            except Exception as e:
                print(f"Failed to load: {e}")
                raise e

    def check_version(self):
        'Checking for latest version'
        from version import ver
        try:
            r = requests.get("https://api.github.com/repos/nogasgofast/Adventure_Wrench/releases")
            update_version = None
            for release in r.json():
                remote_ver = [ int(x) for x in release["tag_name"][1:].split('.') ]
                local_ver = [ int(x) for x in ver.split('.') ]
                for i in range(0, 2):
                    if remote_ver[i] > local_ver[i]:
                        update_version = f'''New Version: <a href="{release["html_url"]}">
                                             {release["name"]}</a>'''
                        self.ui.label_version.setText(update_version)
                        break
                    elif remote_ver[i] == local_ver[i]:
                        continue
                    else:
                        # Our version is better go ahead and stop.
                        break
                if not update_version:
                    self.ui.label_version.setText(f"On latest version: v{ver}")
        except:
            self.ui.label_version.setText(f"Current Version: v{ver}")


    @db_session
    def update_icon(self, kind, cycle):
        for row in range(0, self.ui.listWidget_Encounter.count()):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                item.dbObj = self.db.Active[item.dbObj.id]
                if kind == 'black_star':
                    new = (item.dbObj.black_star + 1) % cycle
                    item.dbObj.black_star = new
                elif kind == 'white_star':
                    new = (item.dbObj.white_star + 1) % cycle
                    item.dbObj.white_star = new
                elif kind == 'death_save_fail':
                    new = (item.dbObj.death_save_fail + 1) % cycle
                    item.dbObj.death_save_fail = new
                elif kind == 'death_save_success':
                    new = (item.dbObj.death_save_success + 1) % cycle
                    item.dbObj.death_save_success = new
                self.update_encounter_text(item)


    @db_session
    def remove(self):
        remove_these = []
        E = self.ui.listWidget_Encounter
        for row in range(0, E.count()):
            if E.item(row).isSelected():
                remove_these.append(row)
                E.item(row).setSelected(False)
        remove_these.sort()
        remove_these.reverse()
        for row in remove_these:
            deletion = E.takeItem(row)
            dbObj = self.db.Active[deletion.dbObj.id]
            dbObj.delete()
            del(deletion)


    @db_session
    def kill(self):
        E = self.ui.listWidget_Encounter
        for row in range(0, E.count()):
            if E.item(row).isSelected():
                item = E.item(row)
                item.dbObj = self.db.Active[item.dbObj.id]
                if item.dbObj.count > 1 and sum(item.dbObj.group_hp) > 0:
                    groupHP = [ 0 for x in item.dbObj.group_hp if x > 0 ]
                    item.dbObj.group_hp = groupHP
                    item.dbObj.count = len(groupHP)
                    self.update_encounter_text(item)
                elif item.dbObj.hp:
                    item.dbObj.hp = 0
                    self.update_encounter_text(item)


    @db_session
    def load_session(self):
        all_Active = self.db.Active.select()
        self.ui.listWidget_Encounter.clear()
        for thing in all_Active:
            item = QListWidgetItem()
            item.dbObj = thing
            self.update_encounter_text(item)
            self.ui.listWidget_Encounter.addItem(item)


    @db_session
    def spinBox_update(self):
        # print("spinBox_update")
        # TODO switch to signal blocking here.
        self.suppress_spinbox_update = True
        for row in range(0, self.ui.listWidget_Encounter.count()):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                item.dbObj = self.db.Active[item.dbObj.id]
                if item.dbObj.count > 1:
                    hp = sum(item.dbObj.group_hp)
                else:
                    hp = item.dbObj.hp
                self.ui.spinBox_main_initiative.setValue(
                    item.dbObj.initiative)
                self.ui.spinBox_main_hp.setValue(hp)
        self.suppress_spinbox_update = False


    @db_session
    def update_initiative(self):
        if self.suppress_spinbox_update:
            pass
        else:
            E = self.ui.listWidget_Encounter
            for row in range(0, E.count()):
                if E.item(row).isSelected():
                    init_value = self.ui.spinBox_main_initiative.value()
                    item = E.item(row)
                    item.dbObj = self.db.Active[item.dbObj.id]
                    item.dbObj.initiative = init_value
                    commit()
                    self.update_encounter_text(item)


    @db_session
    def update_hp(self):
        if self.suppress_spinbox_update:
            pass
        else:
            E = self.ui.listWidget_Encounter
            newHP = self.ui.spinBox_main_hp.value()
            for row in range(0, E.count()):
                if E.item(row).isSelected():
                    item = E.item(row)
                    item.dbObj = self.db.Active[item.dbObj.id]
                    if item.dbObj.count > 1:
                       all_hp = item.dbObj.group_hp
                       hp_sum = sum(all_hp)
                       while hp_sum != newHP:
                           if hp_sum < newHP:
                               min_value = all_hp.index(min(all_hp))
                               value = all_hp.pop(min_value)
                               value += 1
                               hp_sum += 1
                               all_hp.append(value)
                           else:
                               max_value = all_hp.index(max(all_hp))
                               value = all_hp.pop(max_value)
                               value -= 1
                               hp_sum -= 1
                               all_hp.append(value)
                       all_hp = [ hp for hp in all_hp if hp > 0 ]
                       item.dbObj.count = len(all_hp)
                       item.dbObj.group_hp = all_hp
                    else:
                        item.dbObj.hp = newHP
                    if item.dbObj.max_hp < newHP:
                        item.dbObj.max_hp = newHP
                    commit()
                    self.update_encounter_text(item)


    @db_session
    def change_hp(self, diff):
        # print("diff_thing")
        for row in range(0, self.ui.listWidget_Encounter.count()):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                item.dbObj = self.db.Active[item.dbObj.id]
                if len(item.dbObj.group_hp) > 1:
                    groupHP = item.dbObj.group_hp
                    groupHP = [x + diff for x in groupHP]
                    groupHP = [x for x in groupHP if x > 0]
                    item.dbObj.group_hp = groupHP
                    item.dbObj.count = len([ x for x in groupHP if x > 0])
                else:
                    hp = item.dbObj.hp + diff
                    if hp < 0:
                        hp = 0
                    item.dbObj.hp = hp
                commit()
                self.update_encounter_text(item)

    @db_session
    def toggle_expand(self):
        # print("toggle_expand")
        E = self.ui.listWidget_Encounter
        for row in range(0, E.count()):
            if E.item(row).isSelected():
                item = E.item(row)
                if item.dbObj.count > 1:
                    self.expands(item, row)
                    item.dbObj.delete()
                    E.item(row).setSelected(False)
                    E.takeItem(row)
                    break
                else:
                    self.collapse(item, row)
                    break

    @db_session
    def expands(self, item, row):
        item.dbObj = self.db.Active[item.dbObj.id]
        for hp in item.dbObj.group_hp:
            newItem = QListWidgetItem()
            newItem.dbObj = self.db.Active(
                            name = item.dbObj.name,
                            stat_block = item.dbObj.stat_block,
                            initiative = item.dbObj.initiative,
                            hp = hp,
                            max_hp = hp,
                            death_save_fail = item.dbObj.death_save_fail,
                            death_save_success = item.dbObj.death_save_success,
                            black_star = item.dbObj.black_star,
                            white_star = item.dbObj.white_star,
                            from_vault = item.dbObj.from_vault)
            commit()
            self.update_encounter_text(newItem)
            self.ui.listWidget_Encounter.insertItem((row + 1), newItem)

    @db_session
    def collapse(self, item, inRow):
        viewObj = self.db.Active[item.dbObj.id]
        name = viewObj.name
        group = []
        encounter_view = self.ui.listWidget_Encounter
        for row in range(0, encounter_view.count()):
            if encounter_view.item(row).isSelected():
                rowItem = encounter_view.item(row)
                rowObj = self.db.Active[rowItem.dbObj.id]
                if (rowObj.name == name and
                    rowObj.count == 1   and row != inRow):
                    group.append(row)
        group.sort()
        group.reverse()
        groupHP = []
        groupOf = 0
        for row in group:
            rowItem = encounter_view.item(row)
            rowObj = self.db.Active[rowItem.dbObj.id]
            groupHP.append(rowObj.hp)
            groupOf += 1
            rowObj.delete()
            encounter_view.takeItem(row)
        # include the item slected as well.
        commit()
        groupHP.append(viewObj.hp)
        viewObj.hp = sum(groupHP)
        viewObj.max_hp = sum(groupHP)
        viewObj.count = len(groupHP)
        viewObj.group_hp = groupHP
        self.update_encounter_text(item)


    @db_session
    def advance_initiative(self):
        # print("advance_initiative")
        flag = False
        initiative = 0
        E = self.ui.listWidget_Encounter
        for row in range(0, E.count()):
            if E.item(row).isSelected():
                item = E.item(row)
                item.dbObj = self.db.Active[item.dbObj.id]
                initiative = item.dbObj.initiative
                E.item(row).setSelected(False)
                flag = True
                break
        self.sort_initiative()
        if flag:
            flag2 = False
            for row in range(0, E.count()):
                item = E.item(row)
                item.dbObj = self.db.Active[item.dbObj.id]
                if item.dbObj.initiative < initiative:
                    E.item(row).setSelected(True)
                    flag2 = True
                    break
            if not flag2:
                E.item(0).setSelected(True)
        else:
            E.item(0).setSelected(True)


    @db_session
    def sort_initiative(self):
        # print("sort_initiative")
        E = self.ui.listWidget_Encounter
        Initiatives = []
        order = []
        for row in range(0, E.count()):
            item = E.item(row)
            item.dbObj = self.db.Active[item.dbObj.id]
            Initiatives.append(item.dbObj.initiative)
        Initiatives.sort()
        Initiatives.reverse()
        for init in Initiatives:
            for row in range(0, E.count()):
                item = E.item(row)
                item.dbObj = self.db.Active[item.dbObj.id]
                if item.dbObj.initiative == init:
                    item = E.takeItem(row)
                    order.append(item)
                    break
        for item in order:
            E.addItem(item)


    def get_health_color(self, item):
        hp = item.dbObj.hp
        if item.dbObj.count > 1:
            all_hp = item.dbObj.group_hp
            hp = sum(all_hp)
        if hp <= 0:
            hp = 0
            (red,green,blue)=(255,255,255)
            return (red,green,blue)
        else:
            maxhp = item.dbObj.max_hp
            green = int(255 * (float(hp) / float(maxhp)))
            green = green if green > 0 else 0
            green = green if green < 255 else 255
            red =  255 - green
            blue = 0
            return (red,green,blue)


    @db_session
    def update_encounter_text(self, item):
        item.dbObj = self.db.Active[item.dbObj.id]
        if item.dbObj.count > 1:
            format = '''%s | %s
    %s left with hp Sum: %s High: %s Low: %s
    %s%s%s%s''' % (
                    item.dbObj.initiative,
                    item.dbObj.name,
                    item.dbObj.count,
                    sum(item.dbObj.group_hp),
                    max(item.dbObj.group_hp),
                    min(item.dbObj.group_hp),
                    u'\u2716' * item.dbObj.death_save_fail,
                    u'\u2714' * item.dbObj.death_save_success,
                    u'\u2605' * item.dbObj.black_star,
                    u'\u2606' * item.dbObj.white_star)
        else:
            format = "%s | %s | hp:%s | %s%s%s%s" % (
                    item.dbObj.initiative,
                    item.dbObj.name,
                    item.dbObj.hp,
                    u'\u2716' * item.dbObj.death_save_fail,
                    u'\u2714' * item.dbObj.death_save_success,
                    u'\u2605' * item.dbObj.black_star,
                    u'\u2606' * item.dbObj.white_star)
        item.setText(format)
        (red,green,blue) = self.get_health_color(item)
        painter = QBrush(QColor(red,green,blue))
        item.setBackground(painter)
        (red,green,blue) = (0,0,0)
        painter = QBrush(QColor(red,green,blue))
        item.setForeground(painter)
        item.setFont(QFont("Times", 16, QFont.Bold))
        item.setToolTip(item.dbObj.stat_block)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
