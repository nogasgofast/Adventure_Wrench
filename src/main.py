#!/usr/bin/python3

import sys
from ui.Main_Window import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, QMainWindow,
                              QDialog, QWidget,
                              QListWidgetItem)
from PySide6.QtGui import QBrush, QColor, QFont
from pony.orm import db_session, commit
from lib.aw_db import aw_db
from Player import PlayerDialog
from Vault import VaultDialog



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        try:
            aw_db.bind(provider="sqlite", filename="awdb.sqlite", create_db=True)
            aw_db.generate_mapping(create_tables=True)
            self.db = aw_db
        except Exception as e:
            print("aw_db.sqlite Failed to load: {e}")
            raise e
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_vault = VaultDialog(self)
        self.ui_p = PlayerDialog(self)


        self.ui_p.setModal(True)

        self.ui.pushButton_vault.clicked.connect(self.ui_vault.show)
        self.ui.pushButton_players.clicked.connect(self.ui_p.add_player)
        self.ui.pushButton_Inititave.clicked.connect(self.advance_initiative)
        self.ui.pushButton_toggle_expand.clicked.connect(self.toggle_expand)
        self.ui.pushButton_dam_1.clicked.connect(lambda: self.damage_thing(1))
        self.ui.pushButton_dam_3.clicked.connect(lambda: self.damage_thing(3))
        self.ui.pushButton_dam_5.clicked.connect(lambda: self.damage_thing(5))
        self.ui.pushButton_dam_10.clicked.connect(
                            lambda: self.damage_thing(10))
        self.ui.pushButton_b_star.clicked.connect(
                            lambda: self.update_icon('black_star', 6))
        self.ui.pushButton_w_star.clicked.connect(
                            lambda: self.update_icon('white_star', 6))
        self.ui.pushButton_cross.clicked.connect(
                            lambda: self.update_icon('death_save_fail', 3))
        self.ui.pushButton_check.clicked.connect(
                            lambda: self.update_icon('death_save_success', 3))
        self.ui.pushButton_kill_remove.clicked.connect(self.kill_remove)

        self.ui.listWidget_Encounter.itemDoubleClicked.connect(self.ui_p.update_player)
        # connect to quick update fields
        self.ui.listWidget_Encounter.itemSelectionChanged.connect(
                                    self.spinBox_update)
        self.ui.spinBox_main_initiative.valueChanged.connect(
                                    self.update_initiative)
        self.ui.spinBox_main_hp.valueChanged.connect(
                                    self.update_hp)
        self.load_session()


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
    def kill_remove(self):
        # print("kill_remove")
        remove_these = []
        E = self.ui.listWidget_Encounter
        for row in range(0, E.count()):
            if E.item(row).isSelected():
                item = E.item(row)
                item.dbObj = self.db.Active[item.dbObj.id]
                if item.dbObj.count > 1 and sum(item.dbObj.group_hp) == 0:
                    remove_these.append(row)
                    E.item(row).setSelected(False)
                    continue
                elif item.dbObj.count > 1 and sum(item.dbObj.group_hp) > 0:
                    groupHP = [ 0 for x in item.dbObj.group_hp if x > 0 ]
                    item.dbObj.group_hp = groupHP
                    item.dbObj.count = len(groupHP)
                    self.update_encounter_text(item)
                elif item.dbObj.hp:
                    item.dbObj.hp = 0
                    self.update_encounter_text(item)
                else:
                    remove_these.append(row)
                    E.item(row).setSelected(False)
        commit()
        remove_these.sort()
        remove_these.reverse()
        for row in remove_these:
            deletion = E.takeItem(row)
            deletion.dbObj.delete()
        commit()

    @db_session
    def load_session(self):
        all_Active = self.db.Active.select()
        for thing in all_Active:
            item = QListWidgetItem()
            item.dbObj = thing
            self.update_encounter_text(item)
            self.ui.listWidget_Encounter.addItem(item)


    @db_session
    def spinBox_update(self):
        # print("spinBox_update")
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
        # print("update_creature_initiative")
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
    def damage_thing(self, damage):
        # print("damage_thing")
        for row in range(0, self.ui.listWidget_Encounter.count()):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                if len(item.dbObj.group_hp) > 1:
                    groupHP = item.dbObj.group_hp
                    groupHP = [x - damage for x in groupHP]
                    groupHP = [x for x in groupHP if x > 0]
                    item.dbObj.group_hp = groupHP
                    item.dbObj.count = len(groupHP)
                else:
                    item.dbObj = self.db.Active[item.dbObj.id]
                    hp = item.dbObj.hp - damage
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
                            description = item.dbObj.description,
                            initiative = item.dbObj.initiative,
                            hp = hp,
                            max_hp = hp,
                            death_save_fail = item.dbObj.death_save_fail,
                            death_save_success = item.dbObj.death_save_success,
                            black_star = item.dbObj.black_star,
                            white_star = item.dbObj.white_star)
            commit()
            self.update_encounter_text(newItem)
            self.ui.listWidget_Encounter.insertItem((row + 1), newItem)

    @db_session
    def collapse(self, item, inRow):
        item.dbObj = self.db.Active[item.dbObj.id]
        name = item.dbObj.name
        group = []
        E = self.ui.listWidget_Encounter
        for row in range(0, E.count()):
            rowItem = E.item(row)
            rowItem.dbObj = self.db.Active[rowItem.dbObj.id]
            if (rowItem.dbObj.name == name and
                rowItem.dbObj.count == 1   and row != inRow):
                group.append(row)
        group.sort()
        group.reverse()
        groupHP = []
        groupOf = 0
        for row in group:
            rowItem = E.item(row)
            rowItem.dbObj = self.db.Active[rowItem.dbObj.id]
            groupHP.append(rowItem.dbObj.hp)
            groupOf = groupOf + 1
            rowItem.dbObj.delete()
            E.takeItem(row)
        # include the item slected as well.
        commit()
        groupHP.append(item.dbObj.hp)
        item.dbObj.hp = sum(groupHP)
        item.dbObj.max_hp = sum(groupHP)
        item.dbObj.count = len(groupHP)
        item.dbObj.group_hp = groupHP
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
