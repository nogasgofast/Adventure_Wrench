#!/usr/bin/python3

import sys
from ui.Main_Window import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, QMainWindow,
                              QDialog, QWidget,
                              QListWidgetItem)
from lib.display_utils import update_text
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
        self.ui_e = VaultDialog(self)
        self.ui_e.setModal(True)
        self.ui.pushButton_Encounter.clicked.connect(self.ui_e.show)
        self.ui_p = PlayerDialog(self)
        self.ui_p.setModal(True)
        self.ui.listWidget_Encounter.itemDoubleClicked.connect(self.ui_p.update_player)
        self.ui.pushButton_Players.clicked.connect(self.ui_p.add_player)
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
                if item.type == 'pc':
                    item.dbObj = self.db.Active[item.dbObj.id]
                else:
                    item.dbObj = self.db.Perils[item.dbObj.id]

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
                update_text(item, self.db)


    @db_session
    def kill_remove(self):
        # print("kill_remove")
        remove_these = []
        E = self.ui.listWidget_Encounter
        for row in range(0, E.count()):
            if E.item(row).isSelected():
                item = E.item(row)
                if item.type == 'pc':
                    item.dbObj = self.db.Active[item.dbObj.id]
                else:
                    item.dbObj = self.db.Perils[item.dbObj.id]
                    groupHP = item.dbObj.group_hp.split(' ')
                    groupHP = [0 for x in groupHP if x > 0]
                    if len(groupHP):
                        item.dbObj.group_hp = ' '.join(groupHP)
                        item.dbObj.count = len(groupHP)
                        update_text(item, self.db)
                    else:
                        E.item(row).setSelected(False)
                        item.dbObj.delete()
                        remove_these.append(row)
                hp = item.dbObj.hp
                if hp == 0:
                    E.item(row).setSelected(False)
                    item.dbObj.delete()
                    remove_these.append(row)
                if hp > 0:
                    hp = 0
                    item.dbObj.hp = hp
                    update_text(item, self.db)

                commit()
        remove_these.sort()
        remove_these.reverse()
        for row in remove_these:
            E.takeItem(row)


    @db_session
    def load_session(self):
        all_Active = self.db.Active.select()
        for player in all_Active:
            item = QListWidgetItem("{player.initiative} | {player.name} | hp:{player.hp}")
            item.dbObj = player
            item.type = 'pc'
            update_text(item, self.db)
            self.ui.listWidget_Encounter.addItem(item)


    @db_session
    def spinBox_update(self):
        # print("spinBox_update")
        self.suppress_spinbox_update = True
        for row in range(0, self.ui.listWidget_Encounter.count()):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                item.dbObj = self.db.Active[item.dbObj.id]
                self.ui.spinBox_main_initiative.setValue(
                    item.dbObj.initiative)
                self.ui.spinBox_main_hp.setValue(
                    item.dbObj.hp)
        self.suppress_spinbox_update = False


    @db_session
    def update_initiative(self):
        # print("update_creature_initiative")
        if self.suppress_spinbox_update:
            pass
        else:
            for row in range(0, self.ui.listWidget_Encounter.count()):
                if self.ui.listWidget_Encounter.item(row).isSelected():
                    init_value = self.ui.spinBox_main_initiative.value()
                    item = self.ui.listWidget_Encounter.item(row)
                    item.dbObj = self.db.Active[item.dbObj.id]
                    item.dbObj.initiative = init_value
                    commit()
                    update_text(item, self.db)


    @db_session
    def update_hp(self):
        # print("update_creature_hp")
        if self.suppress_spinbox_update:
            pass
        else:
            newHP = self.ui.spinBox_main_hp.value()
            for row in range(0, self.ui.listWidget_Encounter.count()):
                if self.ui.listWidget_Encounter.item(row).isSelected():
                    item = self.ui.listWidget_Encounter.item(row)
                    if item.type == 'pc':
                        item.dbObj = self.db.Active[item.dbObj.id]
                        item.dbObj.hp = newHP
                    else:
                        # pull in other encounter types here
                        item.dbObj = self.db.Perils[item.dbObj.id]
                        pass
                    if item.dbObj.max_hp < newHP:
                        item.dbObj.max_hp = newHP
                    commit()
                    update_text(item, self.db)


    @db_session
    def damage_thing(self, damage):
        # print("damage_thing")
        for row in range(0, self.ui.listWidget_Encounter.count()):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                if item.type != 'pc':
                    groupHP = item.dbObj.group_hp
                    groupHP = [x - damage for x in groupHP]
                    groupHP = [x for x in groupHP if x > 0]
                    item.encounter.set_option('groupHP', groupHP)
                    item.encounter.set_option('groupOf', len(groupHP))
                else:
                    item.dbObj = self.db.Active[item.dbObj.id]
                    hp = item.dbObj.hp - damage
                    if hp < 0:
                        hp = 0
                    item.dbObj.hp = hp
                    commit()
                update_text(item, self.db)


    def toggle_expand(self):
        # print("toggle_expand")
        for row in range(0, self.ui.listWidget_Encounter.count()):
            if self.ui.listWidget_Encounter.item(row) and \
                    self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                if item.type != 'pc':
                    if item.dbObj.count > 1:
                        self.expands(row, item)
                        self.ui.listWidget_Encounter.takeItem(row)
                    else:
                        if item.type != 'pc':
                            self.collapse(item)


    def expands(self, row, item):
        # print("expands")
        for hp in item.dbObj.group_hp:
            encItem = QListWidgetItem("***")
            encItem.encounter = item.encounter.copy()
            encItem.encounter.set_option('hp', hp)
            encItem.encounter.set_option('groupOf', 1)
            encItem.encounter.set_option('id', item.dbObj.id)
            encItem.encounter.set_option('initiative',
                                         item.encounter.
                                         get_option('initiative'))
            update_text(encItem)
            self.ui.listWidget_Encounter.insertItem((row + 1), encItem)



    def collapse(self, inItem):
        # print("collapse")
        EncounterId = initem.dbObj.id
        encounter = inItem.encounter
        initiative = initem.dbObj.initiative
        group = []
        for row in range(0, self.ui.listWidget_Encounter.count()):
            if self.ui.listWidget_Encounter. \
                    item(row).encounter.get_option('id') == EncounterId:
                group.append(row)
        group.sort()
        insertPosition = min(group)
        group.reverse()
        groupHP = []
        groupOf = 0
        for row in group:
            current_item = self.ui.listWidget_Encounter.takeItem(row)
            groupHP.append(current_item.dbObj.hp)
            groupOf = groupOf + 1
        encItem = QListWidgetItem("***")
        encItem.encounter = encounter
        encItem.encounter.set_option('initiative', initiative)
        encItem.encounter.set_option('id', EncounterId)
        encItem.encounter.set_option('groupHP', groupHP)
        encItem.encounter.set_option('groupOf', groupOf)
        update_text(encItem)
        self.ui.listWidget_Encounter.insertItem(insertPosition, encItem)


    @db_session
    def advance_initiative(self):
        # print("advance_initiative")
        flag = False
        initiative = 0
        E = self.ui.listWidget_Encounter
        for row in range(0, E.count()):
            if E.item(row).isSelected():
                item = E.item(row)
                if item.type == 'pc':
                    item.dbObj = self.db.Active[item.dbObj.id]
                else:
                    item.dbObj = self.db.Perils[item.dbObj.id]
                initiative = item.dbObj.initiative
                E.item(row).setSelected(False)
                flag = True
                break
        self.sort_initiative()
        if flag:
            flag2 = False
            for row in range(0, E.count()):
                item = E.item(row)
                if item.type == 'pc':
                    item.dbObj = self.db.Active[item.dbObj.id]
                else:
                    item.dbObj = self.db.Perils[item.dbObj.id]
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
            if item.type == 'pc':
                item.dbObj = self.db.Active[item.dbObj.id]
            else:
                item.dbObj = self.db.Perils[item.dbObj.id]
            Initiatives.append(item.dbObj.initiative)
        Initiatives.sort()
        Initiatives.reverse()
        for init in Initiatives:
            for row in range(0, E.count()):
                item = E.item(row)
                if item.type == 'pc':
                    item.dbObj = self.db.Active[item.dbObj.id]
                else:
                    item.dbObj = self.db.Perils[item.dbObj.id]
                if item.dbObj.initiative == init:
                    item = E.takeItem(row)
                    order.append(item)
                    break
        for item in order:
            E.addItem(item)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
