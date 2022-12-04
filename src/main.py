#!/usr/bin/python3

import sys
from ui.Main_Window import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QWidget

from Player_Dialog import PlayerDialog
from Vault_Dialog import VaultDialog


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_e = VaultDialog(self)
        self.ui_e.setModal(True)
        self.ui.pushButton_Encounter.clicked.connect(self.ui_e.show)
        self.ui_p = PlayerDialog(self)
        self.ui_p.setModal(True)
        self.ui.pushButton_Players.clicked.connect(self.ui_p.show)
        self.ui.pushButton_Inititave.clicked.connect(self.advance_initiative)
        self.ui.pushButton_toggle_expand.clicked.connect(self.toggle_expand)
        self.ui.pushButton_dam_1.clicked.connect(lambda: self.damage_thing(1))
        self.ui.pushButton_dam_3.clicked.connect(lambda: self.damage_thing(3))
        self.ui.pushButton_dam_5.clicked.connect(lambda: self.damage_thing(5))
        self.ui.pushButton_dam_10.clicked.connect(
                                            lambda: self.damage_thing(10))
        self.ui.pushButton_b_star.clicked.connect(
                                            lambda: self.update_icon('bs', 6))
        self.ui.pushButton_w_star.clicked.connect(
                                            lambda: self.update_icon('ws', 6))
        self.ui.pushButton_cross.clicked.connect(
                                            lambda: self.update_icon('DSF', 3))
        self.ui.pushButton_check.clicked.connect(
                                            lambda: self.update_icon('DSS', 3))
        # self.ui.pushButton_open.clicked.connect(self.open_dialog)
        # self.ui.pushButton_save.clicked.connect(self.save_dialog)
        self.ui.pushButton_kill_remove.clicked.connect(self.kill_remove)
        # connect to quick update fields
        self.ui.listWidget_Encounter.itemSelectionChanged.connect(
                                    self.spinBox_update)
        self.ui.spinBox_main_initiative.valueChanged.connect(
                                    self.update_creature_initiative)
        self.ui.spinBox_main_hp.valueChanged.connect(
                                    self.update_creature_hp)

    def update_icon(self, kind, cycle):
        # print("update_icon")
        for row in range(0, len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                new = (item.encounter.get_option(kind) + 1) % cycle
                item.encounter.set_option(kind, new)
                update_text(item)

    def closeEvent(self, event):
        # print("closeEvent")
        quit_msg = "Replace default save file ?"
        reply = QMessageBox.question(self, 'Message',
                                     quit_msg, QMessageBox.Yes,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.save_session()
            event.accept()
        else:
            event.accept()

    def kill_remove(self):
        # print("kill_remove")
        remove_these = []
        for row in range(0, len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                if item.encounter.get_option('groupOf') > 1:
                    groupHP = item.encounter.get_option('groupHP')
                    groupHP = [0 for x in groupHP if x > 0]
                    if len(groupHP):
                        item.encounter.set_option('groupHP', groupHP)
                        item.encounter.set_option('groupOf', len(groupHP))
                    else:
                        remove_these.append(row)
                else:
                    hp = item.encounter.get_option('hp')
                    if hp == 0:
                        remove_these.append(row)
                    if hp > 0:
                        hp = 0
                    item.encounter.set_option('hp', hp)
                update_text(item)
        remove_these.sort()
        remove_these.reverse()
        for row in remove_these:
            self.ui.listWidget_Encounter.takeItem(row)

    def open_dialog(self):
        # print("open_dialog")
        # outputs ('filename', 'Filetype') in this case 'Pickles'
        fileName = QFileDialog.getOpenFileName(self,
                                               "Open Save Files",
                                               "~",
                                               "Pickles (*.pickle)")[0]
        if fileName:
            # print("fileName: {}".format(fileName))
            self.load_session(fileName)

    def save_dialog(self):
        # print("save_dialog")
        # outputs ('filename', 'Filetype') in this case 'Pickles'
        fileName = QFileDialog.getSaveFileName(self,
                                               "Save File Name",
                                               "MyGame.pickle",
                                               "Pickles (*.pickle)")[0]
        if fileName:
            self.save_session(fileName)

    def save_session(self, fh=None):
        # print("save_session")
        # try:
        if fh:
            fh = open(fh, 'wb')
        else:
            fh = open('saved_session.pickle', 'wb')
        pack = {}
        # items in main window
        pack['main'] = []
        # just player names
        pack['players'] = []
        # items in encounter window?
        pack['encounters'] = []
        for row in range(0, len(self.ui.listWidget_Encounter)):
            item = self.ui.listWidget_Encounter.item(row)
            pack['main'].append(item.encounter)
        for row in range(0, self.ui_p.ui.comboBox_name.count()):
            pack['players'].append(
                        str(self.ui_p.ui.comboBox_name.itemText(row)))
        for row in range(0, len(self.ui_e.ui.listWidget_Display)):
            item = self.ui_e.ui.listWidget_Display.item(row)
            if item:
                pack['encounters'].append(item.encounter)
        pack['itemID'] = self.ui_e.itemID
        pickle.dump(pack, fh)
        fh.close()
        # except:
        #     # raise
        #     QMessageBox.question(self,
        #                          'Wisdom.',
        #                          'Unable to write file',
        #                          QMessageBox.Ok)

    def load_session(self, fh=None):
        # print("load_session")
        try:
            if fh:
                with open(fh, 'rb') as fh:
                    # print("fh: {}".format(fh))
                    pack = pickle.load(fh)
                    # print(pack)
            else:
                with open('saved_session.pickle', 'rb') as fh:
                    # print("fh2: {}".format(fh))
                    pack = pickle.load(fh)
                    # print(pack)
            self.ui_e.itemID = pack['itemID']
            self.ui_p.ui.comboBox_name.clear()
            for item in pack['players']:
                self.ui_p.ui.comboBox_name.insertItem(1, item)
            for row in range(0, len(self.ui_e.ui.listWidget_Display)):
                self.ui_e.ui.listWidget_Display.takeItem(0)
            for encounter in pack['encounters']:
                self.ui_e.ui_s.add_item(encounter)
            for row in range(0, len(self.ui.listWidget_Encounter)):
                self.ui.listWidget_Encounter.takeItem(0)
            for encounter in pack['main']:
                item = QListWidgetItem("***")
                item.encounter = encounter
                update_text(item)
                self.ui.listWidget_Encounter.addItem(item)
        except FileNotFoundError:
            QMessageBox.question(self,
                                 'Wisdom.',
                                 'Sorry no save 0_o',
                                 QMessageBox.Ok)

    def spinBox_update(self):
        # print("spinBox_update")
        self.suppress_spinbox_update = True
        for row in range(0, len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                self.ui.spinBox_main_initiative.setValue(
                    item.encounter.get_option('initiative'))
                self.ui.spinBox_main_hp.setValue(
                    item.encounter.get_option('hp'))
        self.suppress_spinbox_update = False

    def update_creature_initiative(self):
        # print("update_creature_initiative")
        if self.suppress_spinbox_update:
            pass
        else:
            for row in range(0, len(self.ui.listWidget_Encounter)):
                if self.ui.listWidget_Encounter.item(row).isSelected():
                    init_value = self.ui.spinBox_main_initiative.value()
                    item = self.ui.listWidget_Encounter.item(row)
                    item.encounter.set_option('initiative',
                                              init_value)
                    update_text(item)

    def update_creature_hp(self):
        # print("update_creature_hp")
        if self.suppress_spinbox_update:
            pass
        else:
            newHP = self.ui.spinBox_main_hp.value()
            for row in range(0, len(self.ui.listWidget_Encounter)):
                if self.ui.listWidget_Encounter.item(row).isSelected():
                    item = self.ui.listWidget_Encounter.item(row)
                    if item.encounter.get_option('groupOf') == 1:
                        item.encounter.set_option('hp', newHP)
                    if item.encounter.get_option('maxHP') < newHP:
                        item.encounter.set_option('maxHP', newHP)
                    update_text(item)

    def damage_thing(self, damage):
        # print("damage_thing")
        for row in range(0, len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                if item.encounter.get_option('groupOf') > 1:
                    groupHP = item.encounter.get_option('groupHP')
                    groupHP = [x - damage for x in groupHP]
                    groupHP = [x for x in groupHP if x > 0]
                    item.encounter.set_option('groupHP', groupHP)
                    item.encounter.set_option('groupOf', len(groupHP))
                else:
                    hp = item.encounter.get_option('hp') - damage
                    if hp < 0:
                        hp = 0
                    item.encounter.set_option('hp', hp)
                update_text(item)

    def toggle_expand(self):
        # print("toggle_expand")
        for row in range(0, len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.item(row) and \
                    self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                # -1 indicates a non-encounter object
                if item.encounter.get_option('id') != -1:
                    if item.encounter.get_option('groupOf') > 1:
                        self.expands(row, item)
                        self.ui.listWidget_Encounter.takeItem(row)
                    else:
                        if item.encounter.get_option('id') != -1:
                            self.collapse(item)

    def expands(self, row, item):
        # print("expands")
        for hp in item.encounter.get_option('groupHP'):
            encItem = QListWidgetItem("***")
            encItem.encounter = item.encounter.copy()
            encItem.encounter.set_option('hp', hp)
            encItem.encounter.set_option('groupOf', 1)
            encItem.encounter.set_option('id', item.encounter.get_option('id'))
            encItem.encounter.set_option('initiative',
                                         item.encounter.
                                         get_option('initiative'))
            update_text(encItem)
            self.ui.listWidget_Encounter.insertItem((row + 1), encItem)

    def collapse(self, inItem):
        # print("collapse")
        EncounterId = inItem.encounter.get_option('id')
        encounter = inItem.encounter
        initiative = inItem.encounter.get_option('initiative')
        group = []
        for row in range(0, len(self.ui.listWidget_Encounter)):
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
            groupHP.append(current_item.encounter.get_option('hp'))
            groupOf = groupOf + 1
        encItem = QListWidgetItem("***")
        encItem.encounter = encounter
        encItem.encounter.set_option('initiative', initiative)
        encItem.encounter.set_option('id', EncounterId)
        encItem.encounter.set_option('groupHP', groupHP)
        encItem.encounter.set_option('groupOf', groupOf)
        update_text(encItem)
        self.ui.listWidget_Encounter.insertItem(insertPosition, encItem)

    def update_window(self, Item):
        # print("update_window")
        self.ui.listView_Encounter()

    def advance_initiative(self):
        # print("advance_initiative")
        flag = False
        initiative = 0
        E = self.ui.listWidget_Encounter
        for row in range(0, len(E)):
            if E.item(row).isSelected():
                initiative = E.item(row).encounter.get_option('initiative')
                E.item(row).setSelected(False)
                flag = True
                break
        self.sort_initiative()
        if flag:
            flag2 = False
            for row in range(0, len(E)):
                if E.item(row).encounter.get_option('initiative') < initiative:
                    E.item(row).setSelected(True)
                    flag2 = True
                    break
            if not flag2:
                E.item(0).setSelected(True)
        else:
            E.item(0).setSelected(True)

    def sort_initiative(self):
        # print("sort_initiative")
        E = self.ui.listWidget_Encounter
        Initiatives = []
        order = []
        for row in range(0, len(E)):
            Initiatives.append(E.item(row).encounter.get_option('initiative'))
        Initiatives.sort()
        Initiatives.reverse()
        for init in Initiatives:
            for row in range(0, len(E)):
                if E.item(row).encounter.get_option('initiative') == init:
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
