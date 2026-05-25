#!/bin/env python

import sys, os, shutil
import requests
import configparser
import sqlite3
from ui.Main_Window import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, QMainWindow,
                              QListWidgetItem,
                              QProgressBar,
                              QMessageBox, QFileDialog,
                              QStyle,QLabel)
from PySide6.QtGui import QBrush, QColor, QIcon
from PySide6.QtCore import QStandardPaths 
# from pony.orm import db_session, commit
from pony.orm import *
from lib.aw_db import database_factory
from lib.schema_upgrades import upgrade_db
from Player import PlayerDialog
from Vault import VaultDialog
from Settings import SettingsDialog
from jinja2 import Environment, FileSystemLoader
from myWidgets import GProgressBar, GDisplayWidget




class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # read config
        self.debug = False
        self.config_setup()
        self.Initiative_Icon = QStyle.StandardPixmap.SP_MediaSeekForward
        self.isAlarmDisplayed = False

        # initialize views.
        self.ui_vault = VaultDialog(self)
        self.ui_p = PlayerDialog(self)
        self.ui_s = SettingsDialog(self)
        self.ui_s.update()
        # Window Modal is set in the designer. Or should be
        # self.ui_p.setModal(True)

        # connect views to button logic
        self.ui.pushButton_settings.clicked.connect(self.ui_s.show)
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
                                    self.selection_update)

        self.ui.spinBox_main_initiative.valueChanged.connect(
                                    self.update_initiative)
        self.ui.spinBox_main_hp.valueChanged.connect(
                                    self.spinbox_update_hp)

        self.check_version()
        self.load_session()


    def config_setup(self):
        # quit("program debug halt -3")
        # ~/.config/<app id>.ini

        self.db = database_factory()

        if self.debug == True:
            self.config_name = './awconfig.ini'
            self.default_save_dir = './save'
        else:
            self.config_name = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppConfigLocation)
            self.default_save_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation)
            self.default_app_path = os.path.dirname(os.path.realpath(__file__)) + '/save'
            if not os.path.exists(self.default_save_dir):
                os.mkdir(self.default_save_dir)
            if 'library.zip' in self.default_app_path:
                self.default_app_path = 'save'
            for f in os.listdir(self.default_app_path):
                full_p = os.path.join(self.default_app_path , f)
                if os.path.isfile(full_p) and not os.path.isfile(f'{self.default_save_dir}/{f}'):
                    shutil.copyfile(full_p, f'{self.default_save_dir}/{f}')

        self.db_default_name = self.default_save_dir + '/default.sqlite'
        self.config_file = configparser.ConfigParser()
        self.config_file.read(self.config_name)

        if 'Game' in self.config_file:
            db_file = self.config_file['Game']['db']
        else:
            self.config_file['Game'] = { 'db': self.db_default_name }
            with open(self.config_name, 'w') as fh:
                self.config_file.write(fh)
            db_file = self.db_default_name
        try:
            # connect to database and try to create missing items if needed.
            self.db.bind(provider="sqlite", filename=db_file, create_db=True)
            self.db.generate_mapping(create_tables=True)
        except pony.orm.dbapiprovider.OperationalError as e:
            print("entered Exception")
            print(db_file)
            # detected a currupt or out of date database, attempting upgrade.
            del(self.db)
            upgrade_db(e, db_file)
            self.config_setup()
            return
        except Exception as e:
            print(f"Save file failed to load: {db_file}")
            raise e

        # Setting the game name based on the save file name.
        game_name = os.path.basename(db_file)
        game_name = os.path.splitext(game_name)[0]
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label_current_game.setText(f'Current Game: {game_name}')

        # Initialize the PnP system type
        with db_session:
            system_name = self.db.Settings.get(name='pnp_system_name')
            if not system_name:
                system_name = self.db.Settings(name='pnp_system_name', value='5e')
            self.system_config = configparser.ConfigParser(interpolation=None)
            system_path = self.default_save_dir + f"/{system_name.value}.ini"
            self.system_config.read(system_path)
            try:
                raw_stats = self.system_config['stats']
            except Exception as e:
                print(f"failed to open {system_path} or no stats present in config file")
                raise e
            self.system_stats = dict()
            for stat in raw_stats:
                if ':' in raw_stats[stat]:
                    name, value = raw_stats[stat].split(":")
                    self.system_stats[stat] = {"name": name, "value": value }
                else:
                    name = raw_stats[stat]
                    self.system_stats[stat] = {"name": name, "value": 0 }
            try:
                self.system_macros = dict(self.system_config['macros'])
            except Exception as e:
                print(f"warning: no macros loaded")
                raise e
        # Initialize template for vault items
        if self.debug:
            self.templEnv = Environment(
                loader=FileSystemLoader("save/"))
        else:
            self.templEnv = Environment(
                loader=FileSystemLoader(self.default_save_dir))



    def switch_game(self):
        file_path, filtered_by = QFileDialog.getOpenFileName(self,
                                                 "Switch Game",
                                                 self.default_save_dir,
                                                 "sqlite databases (*.sqlite)")
        if file_path:
            try:
                # print(file_path)
                self.config_file['Game'] = { 'db': file_path }
                with open(self.config_name, 'w') as fh:
                    self.config_file.write(fh)
                try:
                    self.ui_p.close()
                    self.ui_vault.close()
                    del(self.db)
                    self.db = database_factory()
                    self.db.bind(provider="sqlite",
                               filename=file_path,
                               create_db=False)
                    self.db.generate_mapping(create_tables=False)
                except pony.orm.dbapiprovider.OperationalError as e:
                    # We have detected a currupt or old database schema
                    # disconnect from database and perform upgrade.
                    del(self.db)
                    upgrade_db(e, file_path)
                    raise(e)
                    self.switch_game()
                    return
                except Exception as e:
                    print("aw_db.sqlite Failed to load: {e}")
                    raise e
                self.ui_vault.load_vault()
                self.ui_vault.ui_acadamy.load_acadamy()
                self.load_session()
                # just use the name not the extention here
                game_name = os.path.splitext(os.path.basename(file_path))[0]
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
                local_ver = [ int(x) for x in ver[1:].split('.') ]
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
                    self.ui.label_version.setText(f"On latest version: {ver}")
        except:
            self.ui.label_version.setText(f"Current Version: {ver}")


    @db_session
    def update_icon(self, kind, cycle):
        # print("update_icon")
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
    def remove(self, selection=False):
        remove_these = []
        E = self.ui.listWidget_Encounter
        if not selection:
            for row in range(0, E.count()):
                if E.item(row) and E.item(row).isSelected():
                    remove_these.append(row)
                    E.item(row).setSelected(False)
            remove_these.sort()
            remove_these.reverse()
        else:
            remove_these = selection
        for row in remove_these:
            # print("removing ", row)
            if E.item(row) and E.count() > 1 and E.item(row).isSessionInitiative:
                # print('advance_initiative')
                self.advance_initiative()
                # print('entering remove')
                self.remove(remove_these)
                # print('exiting remove')
                break
            # print('deleting')
            if E.item(row):
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
        # print("load_session")
        all_Active = self.db.Active.select()
        E = self.ui.listWidget_Encounter
        E.clear()
        for thing in all_Active:
            item = QListWidgetItem()
            item.dbObj = thing
            item.vbox = GDisplayWidget()
            if thing.max_hp:
                item.vbox.pbar.setRange(0, thing.max_hp)
            else:
                item.vbox.pbar.setRange(0, thing.hp)
            self.update_encounter_text(item)

            item.setSizeHint(item.vbox.sizeHint())
            item.isSessionInitiative = False

            E.addItem(item)
            E.setItemWidget(item, item.vbox)


    @db_session
    def selection_update(self):
        # print("selection_update")
        # TODO switch to signal blocking here.
        for row in range(0, self.ui.listWidget_Encounter.count()):
            item = self.ui.listWidget_Encounter.item(row)
            item.dbObj = self.db.Active[item.dbObj.id]
            if self.ui.listWidget_Encounter.item(row).isSelected():
                # update spinboxes
                if item.dbObj.count > 1:
                    hp = sum(item.dbObj.group_hp)
                else:
                    hp = item.dbObj.hp
                self.ui.spinBox_main_initiative.blockSignals(True)
                self.ui.spinBox_main_hp.blockSignals(True)

                self.ui.spinBox_main_initiative.setValue(
                    item.dbObj.initiative)
                self.ui.spinBox_main_hp.setValue(hp)
                
                self.ui.spinBox_main_initiative.blockSignals(False)
                self.ui.spinBox_main_hp.blockSignals(False)

                # update style for sub-components
                SelectedColor = r'background-color: rgb(69, 72, 103); size: ' 
                item.vbox.icon.setStyleSheet(SelectedColor)
                item.vbox.description.setStyleSheet(SelectedColor)
            else:
                NotSelectedColor = r'background-color: rgb(89, 92, 123);'
                item.vbox.icon.setStyleSheet(NotSelectedColor)
                item.vbox.description.setStyleSheet(NotSelectedColor)


    @db_session
    def update_initiative(self):
        # print("update_initiative")
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
    def spinbox_update_hp(self):
        # print("spinbox_update_hp")
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
                if newHP > item.dbObj.max_hp:
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
                    if sum(groupHP) > item.dbObj.max_hp:
                        item.dbObj.max_hp = sum(groupHP)
                else:
                    hp = item.dbObj.hp + diff
                    if hp < 0:
                        hp = 0
                    item.dbObj.hp = hp
                    if hp > item.dbObj.max_hp:
                        item.dbObj.max_hp = hp
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
                    # print('func toggle expand')
                    E.item(row).setSelected(False)
                    E.takeItem(row)
                    item.dbObj.delete()
                    break
                else:
                    self.collapse(item, row)
                    break

    @db_session
    def expands(self, item, row):
        # print("start expands")
        item.dbObj = self.db.Active[item.dbObj.id]
        isSessionInitiative = item.isSessionInitiative
        # print("for each hp in group_hp")
        for hp in item.dbObj.group_hp:
            # print("creating QprogressBar")
            pbar = QProgressBar()
            description = QLabel()
            newItem = QListWidgetItem()
            newItem.vbox = GDisplayWidget()
            newItem.setSizeHint(newItem.vbox.sizeHint())
            # pre-calculate max hp in a sensible way
            max_hp = item.dbObj.max_hp//item.dbObj.count
            if max_hp < hp:
                max_hp = hp
            newItem.dbObj = self.db.Active(
                            name = item.dbObj.name,
                            stat_block = item.dbObj.stat_block,
                            initiative = item.dbObj.initiative,
                            hp = hp,
                            max_hp = max_hp,
                            death_save_fail = item.dbObj.death_save_fail,
                            death_save_success = item.dbObj.death_save_success,
                            black_star = item.dbObj.black_star,
                            white_star = item.dbObj.white_star,
                            from_vault = item.dbObj.from_vault)
            commit()
            # print("checking isSessionInitiative")
            if isSessionInitiative:
                newItem.isSessionInitiative = True
                newItem.setIcon(self.style().standardIcon(self.Initiative_Icon))
                # only do this once if we were in the session Initiative.
                isSessionInitiative = False
            else:
                newItem.isSessionInitiative = False
            # print("Update item text")
            self.update_encounter_text(newItem)
            # print("insert item into list")
            self.ui.listWidget_Encounter.insertItem((row + 1), newItem)
            # print("set item widget")
            self.ui.listWidget_Encounter.setItemWidget(newItem, newItem.vbox)
        # print("finish expands")

    @db_session
    def collapse(self, item, inRow):
        # print("starting collapse")
        viewObj = self.db.Active[item.dbObj.id]
        session_initiative = 0
        name = viewObj.name
        group = []
        isSessionInitiative = False
        encounter_view = self.ui.listWidget_Encounter
        # print("for each item in init list")
        for row in range(0, encounter_view.count()):
            if encounter_view.item(row).isSelected():
                # print("if it is selected")
                rowItem = encounter_view.item(row)
                rowObj = self.db.Active[rowItem.dbObj.id]
                if rowItem.isSessionInitiative:
                    # print("and is on initiative, copy session_initiative")
                    session_initiative = rowObj.initiative
                if (rowObj.name == name and
                    rowObj.count == 1   and row != inRow):
                    # print("and name match and it's a single item, and not viewObj. Add to group.")
                    group.append(row)
        group.sort()
        group.reverse()
        groupHP = []
        # print("for each item in group")
        for row in group:
            # print("record item and send stats to viewObj")
            rowItem = encounter_view.item(row)
            rowObj = self.db.Active[rowItem.dbObj.id]
            # punt the initiative up the list one if this 
            # item has the Initiative and will be deleted.
            if rowItem.isSessionInitiative:
                nextItem = encounter_view.item(row - 1)
                if nextItem:
                    nextItem.isSessionInitiative = True
                    nextItem.setIcon(self.style().standardIcon(self.Initiative_Icon))
            groupHP.append(rowObj.hp)
            # print('remove each item')
            encounter_view.takeItem(row)
            rowObj.delete()
            # print(f'removed {row}')
        # include the item slected as well.
        # print("add viewObj to group stats")
        groupHP.append(viewObj.hp)
        # print("set stats for view object")
        viewObj.hp = sum(groupHP)
        viewObj.count = len(groupHP)
        viewObj.max_hp = sum(groupHP)
        viewObj.group_hp = groupHP
        commit()
        # print('update text')
        self.update_encounter_text(item)
        # print('collapes done')


    @db_session
    def advance_initiative(self):
        # print("advance initiative")
        def toggle_alarm(text):
            if self.isAlarmDisplayed:
                self.ui.label_alarm_notice.setText('')
                self.ui.pushButton_Inititave.setText('Advance Initiative')
                self.ui.pushButton_Inititave.setStyleSheet(r'background-color: rgb(38, 60, 134);color: white;height: 40px;')
                self.isAlarmDisplayed = False
            else:
                self.ui.label_alarm_notice.setText(text)
                self.ui.pushButton_Inititave.setText("Clear Alarm")
                self.ui.pushButton_Inititave.setStyleSheet(r'background-color: rgb(237, 51, 59);color: black; height: 40px;')
                self.isAlarmDisplayed = True
        selection_initiative = 1000
        if self.isAlarmDisplayed:
            toggle_alarm('')
            return

        # Find the selection
        initiative_groups = list()
        E = self.ui.listWidget_Encounter
        for row in range(0, E.count()):
            item = E.item(row)
            item.dbObj = self.db.Active[item.dbObj.id]
            if not item.dbObj.initiative in initiative_groups:
                # print("not in: ", item.dbObj.initiative)
                initiative_groups.append(item.dbObj.initiative)
            # turn Off the current session initiative.
            if E.item(row).isSessionInitiative:
                # print("last initiative:",  item.dbObj.initiative)
                E.item(row).isSessionInitiative = False
                E.item(row).vbox.setIcon(None)
                selection_initiative = item.dbObj.initiative

        # beyond this point we can assume 
        # the list is not empty
        if not initiative_groups:
            return

        # sort items in the list
        self.sort_initiative()
        # remove all initiatives above the selection
        # print("section 1")
        initiative_groups = [x for x in initiative_groups if x < selection_initiative]
        initiative_groups.sort(reverse=True)
        target_group = None

        # advance to next group or loop to top.
        if len(initiative_groups):
            target_group = initiative_groups.pop(0)
        else:
            self.advance_initiative()
            return

        # If item is selected
        # print("targeting :", target_group, initiative_groups)
        if target_group:
           isTop = True
           # find the next item in target group.
           # print(E.count())
           for row in range(0, E.count()):
               item = E.item(row)
               item.dbObj = self.db.Active[item.dbObj.id]
               # print(f"db object aquired: {item.dbObj.initiative}")
               # if this is the top of the group set that item selected.
               if item.dbObj.initiative == target_group and isTop:
                   # print("top of the group:")
                   E.item(row).isSessionInitiative = True
                   icon = self.style().standardIcon(self.Initiative_Icon)
                   E.item(row).vbox.setIcon(icon)
                   isTop = False
               # check every item in the target group for alarms to run.
               if item.dbObj.initiative == target_group and item.dbObj.isAlarm:
                   # print("is alarm")
                   toggle_alarm(f"Alarm {item.dbObj.name}")
               # Even if there are more to check we don't need to check them.
               if item.dbObj.initiative < target_group:
                   # print("below initiative")
                   break
        elif E.item(0):
            # print("why am i here?")
            item = E.item(0)
            item.isSessionInitiative = True
            # icon = self.style().standardIcon(None)
            item.vbox.setIcon(None)
            item.dbObj = self.db.Active[item.dbObj.id]
            if item.dbObj.isAlarm:
                toggle_alarm(f"Alarm {item.dbObj.name}")
        # print("exiting function")


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
                    widget = E.itemWidget(E.item(row)) 
                    E.removeItemWidget(E.item(row))
                    item = E.takeItem(row)
                    tup = (item, widget)
                    order.append(tup)
                    break
        for tup in order:
            thing = tup[0].dbObj
            item = QListWidgetItem()
            item.dbObj = thing
            item.vbox = GDisplayWidget()
            if thing.max_hp:
                item.vbox.pbar.setRange(0, thing.max_hp)
            else:
                item.vbox.pbar.setRange(0, thing.hp)
            self.update_encounter_text(item)

            item.setSizeHint(item.vbox.sizeHint())
            item.isSessionInitiative = tup[0].isSessionInitiative

            E.addItem(item)
            E.setItemWidget(item, item.vbox)


    def get_health_color(self, item):
        # print("get_health_color")
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
        # print("update_encounter_text")
        item.dbObj = self.db.Active[item.dbObj.id]
        if item.dbObj.count > 1:
            format_str = '''%s | %s (%s) hp Sum: %s High: %s Low: %s
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
            # print("range max ", item.dbObj.max_hp)
            item.vbox.pbar.setRange(0, item.dbObj.max_hp)
            # print("value group ", sum(item.dbObj.group_hp))
            item.vbox.pbar.setValue(sum(item.dbObj.group_hp))
        else:
            format_str = "%s | %s | hp:%s | %s%s%s%s" % (
                    item.dbObj.initiative,
                    item.dbObj.name,
                    item.dbObj.hp,
                    u'\u2716' * item.dbObj.death_save_fail,
                    u'\u2714' * item.dbObj.death_save_success,
                    u'\u2605' * item.dbObj.black_star,
                    u'\u2606' * item.dbObj.white_star)
            if item.dbObj.max_hp:
                # print("setting max_hp range ", item.dbObj.max_hp)
                item.vbox.pbar.setRange(0, item.dbObj.max_hp)
            else:
                # print("setting hp range ", item.dbObj.hp)
                item.vbox.pbar.setRange(0, item.dbObj.hp)
            item.vbox.pbar.setValue(item.dbObj.hp)
        # print(item.vbox.pbar.value(), item.vbox.pbar.maximum())
        self.update_pbar_color(item)
        item.vbox.description.setText(format_str)
        item.setToolTip(item.dbObj.stat_block)
        # print("END update_encounter_text")


    def update_pbar_color(self, item):
        # print("update_pbar_color")
        # this also adds the mask on top of the progress bar to give it the 
        # right shape.
        (red,green,blue) = self.get_health_color(item)
        painter = QBrush(QColor(red,green,blue))
        # print(red,green,blue)
        stylesheet = r'QProgressBar::chunk {' + f'background-color: rgba({red},{green},{blue},180);' + r'}'
        stylesheet += r'QProgressBar {background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #990000, stop: 1 #111111);}'
        # print(stylesheet)
        item.vbox.pbar.setStyleSheet(stylesheet)
        (red,green,blue) = (0,0,0)
        painter = QBrush(QColor(red,green,blue))
        item.setForeground(painter)
        # print("end update_pbar_color")


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
