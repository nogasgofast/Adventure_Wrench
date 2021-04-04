#!/usr/bin/python3

import sys
import dice
import pickle
from PyQt5.QtWidgets import QMainWindow, QDialog, \
    QApplication, QListWidgetItem, QMessageBox, \
    QFileDialog
from PyQt5.QtGui import QBrush, QColor
from w_main import Ui_MainWindow
from d_vault import Ui_Vault
from d_configurator import Ui_configurator
from d_player import Ui_Player
from encounter import Encounter, preset_data
from display_utils import update_text

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
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
        self.ui.pushButton_dam_10.clicked.connect(lambda: self.damage_thing(10))
        self.ui.pushButton_b_star.clicked.connect(lambda: self.update_icon('bs',6))
        self.ui.pushButton_w_star.clicked.connect(lambda: self.update_icon('ws',6))
        self.ui.pushButton_cross.clicked.connect(lambda: self.update_icon('DSF',3))
        self.ui.pushButton_check.clicked.connect(lambda: self.update_icon('DSS',3))
        self.ui.pushButton_open.clicked.connect(self.open_dialog)
        self.ui.pushButton_save.clicked.connect(self.save_dialog)
        self.ui.pushButton_kill_remove.clicked.connect(self.kill_remove)
        #connect to quick update fields
        self.ui.listWidget_Encounter.itemSelectionChanged.connect(
                                    self.spinBox_update)
        self.ui.spinBox_main_initiative.valueChanged.connect(
                                    self.update_creature_initiative)
        self.ui.spinBox_main_hp.valueChanged.connect(
                                    self.update_creature_hp)

    def update_icon(self,kind,cycle):
        print("update_icon")
        for row in range(0,len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                new = (item.encounter.get_option(kind) + 1) % cycle
                item.encounter.set_option(kind,new)
                update_text(item)

    def closeEvent(self, event):
        print("closeEvent")
        quit_msg = "Replace default save file ?"
        reply = QMessageBox.question(self, 'Message',
                        quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.save_session()
            event.accept()
        else:
            event.accept()

    def kill_remove(self):
        print("kill_remove")
        remove_these = []
        for row in range(0,len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                if item.encounter.get_option('groupOf') > 1:
                    groupHP = item.encounter.get_option('groupHP')
                    groupHP = [ 0 for x in groupHP if x > 0 ]
                    if len(groupHP):
                        item.encounter.set_option('groupHP', groupHP)
                        item.encounter.set_option('groupOf', len(groupHP))
                    else:
                        remove_these.append(row)
                else:
                    hp = item.encounter.get_option('hp')
                    if hp == 0: remove_these.append(row)
                    if hp > 0: hp = 0
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
            print("fileName: {}".format(fileName))
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

    def save_session(self,fh=None):
        # print("save_session")
        try:
            if fh:
                fh = open(fh,'wb')
            else:
                fh = open('saved_session.pickle','wb')
            pack = {}
            pack['main'] = [] #items in main window
            pack['players'] = [] #just player names
            pack['encounters'] = [] #items in encounter window?
            for row in range(0,len(self.ui.listWidget_Encounter)):
                item = self.ui.listWidget_Encounter.item(row)
                pack['main'].append(item.encounter)
            for row in range(0,self.ui_p.ui.comboBox_name.count()):
                pack['players'].append(str(self.ui_p.ui.comboBox_name.itemText(row)))
            for row in range(0, len(self.ui_e.ui.listWidget_Display)):
                item = self.ui_e.ui.listWidget_Display.item(row)
                if item:
                    pack['encounters'].append(item.encounter)
            pack['itemID'] = self.ui_e.itemID
            pickle.dump(pack, fh)
            fh.close()
        except:
            # raise
            QMessageBox.question(self,
                                 'Wisdom.',
                                 'Unable to write file',
                                 QMessageBox.Ok)

    def load_session(self,fh=None):
        # print("load_session")
        try:
            if fh:
                with open(fh, 'rb') as fh:
                    print("fh: {}".format(fh))
                    pack = pickle.load(fh)
            else:
                with open('saved_session.pickle', 'rb') as fh:
                    print("fh2: {}".format(fh))
                    pack = pickle.load(fh)
            self.ui_e.itemID = pack['itemID']
            self.ui_p.ui.comboBox_name.clear()
            for item in pack['players']:
                self.ui_p.ui.comboBox_name.insertItem(1,item)
            for row in range(0, len(self.ui_e.ui.listWidget_Display)):
                self.ui_e.ui.listWidget_Display.takeItem(0)
            for encounter in pack['encounters']:
                self.ui_e.add_item(encounter)
            for row in range(0,len(self.ui.listWidget_Encounter)):
                self.ui.listWidget_Encounter.takeItem(0)
            for encounter in pack['main']:
                item = QListWidgetItem("***")
                item.encounter = encounter
                update_text(item)
                self.ui.listWidget_Encounter.addItem(item)
        except:
            QMessageBox.question(self,
                                 'Wisdom.',
                                 'Sorry no save 0_o',
                                 QMessageBox.Ok)

    def spinBox_update(self):
        print("spinBox_update")
        self.suppress_spinbox_update = True
        for row in range(0,len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                self.ui.spinBox_main_initiative.setValue(
                    item.encounter.get_option('initiative'))
                self.ui.spinBox_main_hp.setValue(
                    item.encounter.get_option('hp'))
        self.suppress_spinbox_update = False

    def  update_creature_initiative(self):
        print("update_creature_initiative")
        if self.suppress_spinbox_update:
            pass
        else:
            for row in range(0,len(self.ui.listWidget_Encounter)):
                if self.ui.listWidget_Encounter.item(row).isSelected():
                    item = self.ui.listWidget_Encounter.item(row)
                    item.encounter.set_option('initiative',
                        self.ui.spinBox_main_initiative.value())
                    update_text(item)

    def  update_creature_hp(self):
        print("update_creature_hp")
        if self.suppress_spinbox_update:
            pass
        else:
            newHP = self.ui.spinBox_main_hp.value()
            for row in range(0,len(self.ui.listWidget_Encounter)):
                if self.ui.listWidget_Encounter.item(row).isSelected():
                    item = self.ui.listWidget_Encounter.item(row)
                    if item.encounter.get_option('groupOf') == 1:
                        item.encounter.set_option('hp', newHP)
                    if item.encounter.get_option('maxHP') < newHP:
                        item.encounter.set_option('maxHP', newHP)
                    update_text(item)

    def damage_thing(self,damage):
        print("damage_thing")
        for row in range(0,len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                if item.encounter.get_option('groupOf') > 1:
                    groupHP = item.encounter.get_option('groupHP')
                    groupHP = [ x - damage for x in groupHP ]
                    groupHP = [ x for x in groupHP if x > 0  ]
                    item.encounter.set_option('groupHP', groupHP)
                    item.encounter.set_option('groupOf', len(groupHP))
                else:
                    hp = item.encounter.get_option('hp') - damage
                    if hp < 0: hp = 0
                    item.encounter.set_option('hp', hp)
                update_text(item)

    def toggle_expand(self):
        print("toggle_expand")
        for row in range(0,len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.item(row).isSelected():
                item = self.ui.listWidget_Encounter.item(row)
                # -1 indicates a non-encounter object
                if item.encounter.get_option('id') != -1:
                    if item.encounter.get_option('groupOf') > 1:
                        self.expands(row,item)
                        self.ui.listWidget_Encounter.takeItem(row)
                    else:
                        if item.encounter.get_option('id') != -1:
                            self.collapse(item)

    def expands(self,row,item):
        print("expands")
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
        print("collapse")
        EncounterId = inItem.encounter.get_option('id')
        encounter = inItem.encounter
        initiative = inItem.encounter.get_option('initiative')
        group = []
        for row in range(0,len(self.ui.listWidget_Encounter)):
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

    def update_window(self,Item):
        print("update_window")
        self.ui.listView_Encounter()

    def advance_initiative(self):
        print("advance_initiative")
        flag = False
        initiative = 0
        E = self.ui.listWidget_Encounter
        for row in range(0,len(E)):
            if E.item(row).isSelected():
                initiative = E.item(row).encounter.get_option('initiative')
                E.item(row).setSelected(False)
                flag = True
                break
        self.sort_initiative()
        if flag:
            flag2 = False
            for row in range(0,len(E)):
                if E.item(row).encounter.get_option('initiative') < initiative:
                    E.item(row).setSelected(True)
                    flag2 = True
                    break
            if not flag2:
                E.item(0).setSelected(True)
        else:
            E.item(0).setSelected(True)

    def sort_initiative(self):
        print("sort_initiative")
        E = self.ui.listWidget_Encounter
        Initiatives = []
        order = []
        for row in range(0,len(E)):
            Initiatives.append(E.item(row).encounter.get_option('initiative'))
        Initiatives.sort()
        Initiatives.reverse()
        for init in Initiatives:
            for row in range(0,len(E)):
                if E.item(row).encounter.get_option('initiative') == init:
                    item = E.takeItem(row)
                    order.append(item)
                    break
        for item in order:
            E.addItem(item)

class PlayerDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.main = parent
        self.ui = Ui_Player()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.add_player)
        self.ui.pushButton_delete.clicked.connect(self.remove_player)


    def add_player(self):
        print("add_player")
        #roll initiative
        player = Encounter()
        initiative = self.ui.spinBox_initiative.value()
        player.set_option('initiative', initiative)
        hp = self.ui.spinBox_hp.value()
        player.set_option('hp', hp)
        player.set_option('maxHP',hp)
        #if this seems strange, i have to ensure this function always updates
        #the name combo box. Because comboBox_name.insertPolicy is set to do nothing.
        self.ui.comboBox_name.insertItem(self.ui.comboBox_name.currentIndex(),
                                         self.ui.comboBox_name.currentText())
        name = self.ui.comboBox_name.currentText()
        player.set_option('name', name)
        player.set_option('groupOf', 1)
        item = QListWidgetItem("%s | %s | hp:%s" % (
                                    initiative,
                                    name,
                                    hp))
        # initiative window requires these attributes be added to items
        item.encounter = player
        item.encounter.set_option('id', -1)
        self.main.ui.listWidget_Encounter.addItem(item)
        self.ui.comboBox_name.setEditText('')
        self.ui.spinBox_initiative.setValue(1)
        self.ui.spinBox_hp.setValue(1)
        self.ui.comboBox_name.setFocus()
        self.close()
        # RESET!

    def remove_player(self):
        print("remove_player")
        name = self.ui.comboBox_name.currentText()
        Remove = []
        for row in range(0,len(self.main.ui.listWidget_Encounter)):
            item = self.main.ui.listWidget_Encounter.item(row)
            if item.encounter.get_option('name') == name:
                Remove.append(row)
        Remove.sort()
        Remove.reverse()
        for row in Remove:
            self.main.ui.listWidget_Encounter.takeItem(row)
        self.ui.comboBox_name.removeItem(self.ui.comboBox_name.currentIndex())


class VaultDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.main = parent
        self.ui = Ui_Vault()
        self.ui.setupUi(self)
        self.ui_s = EncounterSelectorDialog(self)
        self.ui_s.setModal(True)
        self.ui.pushButton_Summon.clicked.connect(self.summon_item)
        self.ui.pushButton_UnSummon.clicked.connect(self.unsummon_item)
        self.ui.pushButton_delete.clicked.connect(self.delete_item)

        self.ui.pushButton_New.clicked.connect(self.ui_s.show)
        self.ui.pushButton_save.clicked.connect(self.save_dialog)
        self.ui.pushButton_load.clicked.connect(self.open_dialog)
        self.ui.pushButton_back.clicked.connect(self.close)
        self.ui.listWidget_Display.itemDoubleClicked.connect(self.toggle_item_view)
        # Set this value to keep track of my listItems
        self.itemID = 1

#   # def add_update_callback(self,update_callback):
#   #     self.main_window_callback = update_callback

    def toggle_item_view(self):
        print("toggle_item_view")
        for row in range(0,len(self.ui.listWidget_Display)):
            if self.ui.listWidget_Display.item(row).isSelected():
                item = self.ui.listWidget_Display.item(row)
                if not item.txt:
                    item.setText('- %s' % item.encounter.to_string())
                    item.txt = 1
                else:
                    item.setText('+ %s' % item.encounter.get_option('name'))
                    item.txt = 0

    def open_dialog(self):
        print("open_dialog")
        fileName = QFileDialog.getOpenFileName(self,
                                               "Open Save Files",
                                               "~",
                                               "Pickles (*.pickle)")
        if fileName:
            self.load_encounters(fileName)

    def save_dialog(self):
        print("save_dialog")
        fileName = QFileDialog.getSaveFileName(self,
                                               "Save File Name",
                                               "encounters.pickle",
                                               "Pickles (*.pickle)")
        if fileName:
            self.save_encounters(fileName)

    def save_encounters(self,fh=None):
        print("save_encounters")
        try:
            if fh:
                fh = open(fh,'wb')
            else:
                fh = open('encounters.pickle','wb')
            pack = {}
            pack['encounters'] = [] #items in encounter window?
            for row in range(0, len(self.ui.listWidget_Display)):
                item = self.ui.listWidget_Display.item(row)
                if item:
                    pack['encounters'].append(item.encounter)
            pack['itemID'] = self.itemID
            pickle.dump(pack, fh, 2)
            fh.close()
        except:
            QMessageBox.question(self,
                                 'Wisdom.',
                                 'Unable to write file',
                                 QMessageBox.Ok)

    def load_encounters(self,fh=None):
        print("load_encounters")
        try:
            if fh:
                fh = open(fh, 'rb')
            else:
                fh = open('encounters.pickle', 'rb')
            pack = pickle.load(fh)
            #for row in range(0, len(self.ui.listWidget_Display)):
            #    self.ui.listWidget_Display.takeItem(0)
            for encounter in pack['encounters']:
                self.add_item(encounter)
        except:
            QMessageBox.question(self,
                                 'Wisdom.',
                                 'Sorry no save 0_o',
                                 QMessageBox.Ok)

    def summon_item(self,encounter=False):
        print("summon_item")
        '''set display item for main window.'''
        for row in range(0,len(self.ui.listWidget_Display)):
            if self.ui.listWidget_Display.item(row).isSelected():
                item = self.ui.listWidget_Display.item(row)
                encItem = QListWidgetItem('***')
                encItem.encounter = item.encounter.copy()
                update_text(encItem)
                self.main.ui.listWidget_Encounter.addItem(encItem)

    def delete_item(self):
        print("delete_item")
        unSummonList = {}
        Remove = []
        #find selected items to delete
        for row in range(0,len(self.ui.listWidget_Display)):
            if self.ui.listWidget_Display.item(row).isSelected():
                #follow me here an item has it's position. But also
                #has an identifier I can use to track down copies
                #check out self.add_item().
                unSummonList[row] = self.ui.listWidget_Display.item(row).encounter.get_option('id')
                for mainWindowRow in range(0,len(self.main.ui.listWidget_Encounter)):
                    cur_Item = self.main.ui.listWidget_Encounter.item(mainWindowRow)
                    if cur_Item.encounter.get_option('id') == unSummonList[row]:
                        Remove.append(mainWindowRow)

        #be careful to not change the index of the items
        #you found as you remove them. So remove from the end first.
        #we don't need those values anymore though
        unSummonList = list(unSummonList.keys())
        unSummonList.sort()
        unSummonList.reverse()
        Remove.sort()
        Remove.reverse()

        #remove items from the encounter applet
        for row in unSummonList:
            self.ui.listWidget_Display.takeItem(row)
        #remove items from the initive window (main)
        for row in Remove:
            self.main.ui.listWidget_Encounter.takeItem(row)

    def unsummon_item(self):
        print("unsummon_item")
        unSummonList = {}
        Remove = []
        #find selected items to delete
        for row in range(0,len(self.ui.listWidget_Display)):
            if self.ui.listWidget_Display.item(row).isSelected():
                #follow me here an item has it's position. But also
                #has an identifier I can use to track down copies
                #check out self.add_item() .
                unSummonList[row] = self.ui.listWidget_Display.item(row).encounter.get_option('id')
                for mainWindowRow in range(0,len(self.main.ui.listWidget_Encounter)):
                    cur_Item = self.main.ui.listWidget_Encounter.item(mainWindowRow)
                    if cur_Item.encounter.get_option('id') == unSummonList[row]:
                        Remove.append(mainWindowRow)
        #things in the list change position as you remove them. So i
        #must arrange for the deletion to happen in the right order.
        Remove.sort()
        Remove.reverse()
        #remove items from the initive window (main)
        for row in Remove:
            self.main.ui.listWidget_Encounter.takeItem(row)


class EncounterSelectorDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.vault = parent
        self.ui = Ui_configurator()
        self.ui.setupUi(self)
        self.update_options_list()
        self.ui.pushButton_back.clicked.connect(self.close)
        self.ui.listWidget_catagory.itemSelectionChanged.connect(self.show_hide_options)
        self.ui.lineEdit_search.textChanged.connect(self.auto_search)
        self.ui.pushButton_reset.clicked.connect(self.reset_selected)
        self.ui.pushButton_clear.clicked.connect(self.reset_stats)
        self.ui.comboBox_type.currentIndexChanged.connect(self.change_type)
        self.ui.pushButton_create.clicked.connect(self.add_item)

        # Initalize this combo box with sizes
        sizes = ['tiny', 'small','medium', 'large','huge', 'gargantuan']
        for size in sizes:
            self.ui.comboBox_size.addItem(size)
        self.ui.comboBox_size.setCurrentIndex(2)
        # Pull a list of options for speed.
        self.locomotives = {'walk':30,'fly':0,'swim':0}
        for locomotive in self.locomotives.keys():
            self.ui.comboBox_speed.addItem(locomotive)
        self.ui.comboBox_speed.setCurrentIndex(2)
        self.ui.spinBox_speed.setValue(30)
        self.ui.comboBox_speed.currentIndexChanged.connect(
            self.link_save_and_change_speed)
        self.ui.spinBox_speed.valueChanged.connect(
            self.link_save_new_speed)

    def reset_stats(self):
        print("reset_stats")
        self.ui.spinBox_STR.setProperty("value", 10)
        self.ui.spinBox_DEX.setProperty("value", 10)
        self.ui.spinBox_CON.setProperty("value", 10)
        self.ui.spinBox_WIS.setProperty("value", 10)
        self.ui.spinBox_INT.setProperty("value", 10)
        self.ui.spinBox_CHA.setProperty("value", 10)

    def change_type(self):
        print("change_type")
        enc_type = self.ui.comboBox_type.currentText()
        if enc_type == 'creature':
            self.show_speed()
            self.show_stats()
        elif enc_type == 'trap':
            self.hide_speed()
            self.hide_stats()
        elif enc_type == 'social':
            self.show_speed()
            self.show_stats()
        self.ui_s.update_options_list()

    def hide_speed(self):
        print("hide_speed")
        self.ui.label_speed.hide()
        self.ui.comboBox_speed.hide()
        self.ui.spinBox_speed.hide()

    def show_speed(self):
        print("show_speed")
        self.ui.label_speed.hide()
        self.ui.comboBox_speed.hide()
        self.ui.spinBox_speed.hide()

    def hide_stats(self):
        print("hide_stats")
        self.ui.label_STR.hide()
        self.ui.spinBox_STR.hide()
        self.ui.label_DEX.hide()
        self.ui.spinBox_DEX.hide()
        self.ui.label_CON.hide()
        self.ui.spinBox_CON.hide()
        self.ui.label_WIS.hide()
        self.ui.spinBox_WIS.hide()
        self.ui.label_INT.hide()
        self.ui.spinBox_INT.hide()
        self.ui.label_CHA.hide()
        self.ui.spinBox_CHA.hide()
        self.ui.pushButton_clear.hide()

    def show_stats(self):
        print("show_stats")
        self.ui.label_STR.show()
        self.ui.spinBox_STR.show()
        self.ui.label_DEX.show()
        self.ui.spinBox_DEX.show()
        self.ui.label_CON.show()
        self.ui.spinBox_CON.show()
        self.ui.label_WIS.show()
        self.ui.spinBox_WIS.show()
        self.ui.label_INT.show()
        self.ui.spinBox_INT.show()
        self.ui.label_CHA.show()
        self.ui.spinBox_CHA.show()
        self.ui.pushButton_clear.show()

    def link_save_new_speed(self):
        print("link_save_new_speed")
        'if the spinbox changes value save it here'
        locomotive = str(self.ui.comboBox_speed.itemText(
            self.ui.comboBox_speed.currentIndex()))
        self.locomotives[locomotive] = self.ui.spinBox_speed.value()

    def link_save_and_change_speed(self):
        print("link_save_and_change_speed")
        'set spinbox to new value according to my model'
        locomotive = str(self.ui.comboBox_speed.itemText(
            self.ui.comboBox_speed.currentIndex()))
        self.ui.spinBox_speed.setValue(
            self.locomotives[locomotive])

    def sqrt(self,num):
        if (num // 2) > 1:
            return num // 2
        else:
            return 0

    def gen_creature(self):
        print("gen_creature")
        new_creature = Encounter()
        template = preset_data()
        enc_type = self.ui.comboBox_type.itemText(
            self.ui.comboBox_type.currentIndex())
        attributes = template.get_options(enc_type,'attribute')
        attacks = template.get_options(enc_type,'weapon')
        misc  = template.get_options(enc_type,'misc')
        cr_from_ui = self.ui.spinBox_CR.value()
        num_in_group = self.ui.spinBox_group.value()
        TargetCR = cr_from_ui - self.sqrt(num_in_group)
        new_creature.set_option('speed',self.locomotives)
        new_creature.set_option('size', str(self.ui.comboBox_size.itemText(
            self.ui.comboBox_size.currentIndex())))
        new_creature.set_option('name', str(self.ui.lineEdit_Name.text()))
        new_creature.set_option('encountergroupOf', int(self.ui.spinBox_group.value()))
        new_creature.set_option('cr', TargetCR)
        stats = template.get(TargetCR)
        for stat in stats.keys():
            new_creature.set_option(stat, stats[stat])
        options = self.help_collect_options()
        print("things after")
        for opt in options:
            print("option")
            for attribute in attributes:
                # print("attribute")
                if opt in attribute[0]:
###################################################                    # wtf??
                    self.data['abilities'].append(attribute[0])
                    # maybe
                    # .......
###################################################
            pos_atk = opt[0:-8]
            for weapon in attacks:
                # print("weapon")
                if pos_atk in weapon[2:]:
                    attacks = new_creature.get_option('atk_weapon')
                    if not weapon in attacks:
                        attacks.append(weapon)
                        new_creature.set_option('atk_weapon', attacks)
            pos_misc = opt[0:-5]
            for action in misc:
                # print("actions")
                if pos_misc in action[2:]:
                    misc_actions = new_creature.get_option('misc_actions')
                    if not misc in misc_actions:
                        misc_actions.append(misc)
                        new_creature.set_option('misc_actions',
                                                 misc_actions)
        print("after loops")
        new_creature.set_option('STR',self.ui.spinBox_STR.value())
        new_creature.set_option('DEX',self.ui.spinBox_DEX.value())
        new_creature.set_option('CON',self.ui.spinBox_CON.value())
        new_creature.set_option('WIS',self.ui.spinBox_WIS.value())
        new_creature.set_option('INT',self.ui.spinBox_INT.value())
        new_creature.set_option('CHA',self.ui.spinBox_CHA.value())
        new_creature.gen_actions()
        print("after gen_actions")
        return new_creature

    def add_item(self,encounter=False):
        print("add_item")
        if not encounter:
            dice_caddy = dice.dice()
            encounter = self.gen_creature()
            print("encounter built")
            #roll initiatives
            dex_mod = (encounter.get_option('DEX') - 10) / 2
            encounter.set_option('initiative',
                                dice_caddy.roll('1d20+%s' % (dex_mod)))
            groupHP = []
            print("initiatives rolled")
            if encounter.get_option('groupOf') > 1:
                print("creating group HP divergence")
                for creature in range(0,encounter.get_option('groupOf')):
                    print("for the hoard!")
                    print("to_dice={}".format( encounter.to_dice() ))
                    groupHP.append(dice_caddy.roll('%s' % encounter.to_dice()))
                encounter.set_option('groupHP', groupHP)
            else:
                print("HP for one plx.")
                print("to_dice={}".format(encounter.to_dice()))
                hp = dice_caddy.roll('%s' % encounter.to_dice())
                print("hp created: {}".format(hp))
                encounter.set_option('hp', hp)
                print("encounter hp set")
            encounter.set_option('type', self.ui.comboBox_type.currentText())
            print("encounter type set")
        print("after option dice roll sets")
        # add item to encounter window
        item = QListWidgetItem("+ %s" % encounter.get_option('name'))
        print("QListWidgetItem created")
        item.txt = 0
        item.setToolTip("%s" % encounter.to_string())
        item.encounter = encounter
        item.encounter.set_option('id', self.vault.itemID)
        self.vault.ui.listWidget_Display.addItem(item)
        print("item added to ui list")
        self.vault.itemID += 1
        #help keyboard users to get back to name
        self.close()


    def reset_selected(self):
        print("reset_selected")
        for row in range(0,len(self.ui.listWidget_catagory)):
            item = self.ui.listWidget_catagory.item(row)
            if item.isSelected():
                item.setSelected(False)
        self.ui.listWidget_options.clear()

    def auto_search(self):
        print("auto_search")
        items = []
        if len(self.ui.lineEdit_search.text()) > 3:
            items = self.ui.listWidget_catagory.findItems(
                             self.ui.lineEdit_search.text(),
                             Qt.MatchFlags(1))
        if items:
            for row in range(0,len(self.ui.listWidget_catagory)):
                item = self.ui.listWidget_catagory.item(row)
                if not item in items:
                    self.ui.listWidget_catagory.setItemHidden(item,True)
                else:
                    self.ui.listWidget_catagory.setItemHidden(item,False)
        else:
            for row in range(0,len(self.ui.listWidget_catagory)):
                item = self.ui.listWidget_catagory.item(row)
                self.ui.listWidget_catagory.setItemHidden(item,False)

    def show_hide_options(self):
        print("show_hide_options")
        enc_type = self.ui.comboBox_type.currentText()
        selection = []
        for row in range(0,len(self.ui.listWidget_catagory)):
            if self.ui.listWidget_catagory.item(row).isSelected():
                selection.append((self.ui.listWidget_catagory.item(row).text(),
                                  self.ui.listWidget_catagory.item(row).background())
                                )

        self.ui.listWidget_options.clear()
        for (eachthing,background) in selection:
            item = QListWidgetItem(eachthing)
            #print background
            item.setBackground(background)
            self.ui.listWidget_options.addItem(item)

    def update_options_list(self):
        print("update_options_list")
        self.ui.listWidget_catagory.clear()
        pd = preset_data()
        enc_type = self.ui.comboBox_type.currentText()
        attribute = pd.get_options(enc_type, 'attribute')
        attacks = pd.get_options(enc_type, 'weapon')
        misc  = pd.get_options(enc_type, 'misc')

        for options in sorted(attribute, key=lambda x: x[0]):
            item = QListWidgetItem(" ".join(options))
            (red,green,blue)=(166, 244, 175)
            painter = QBrush(QColor(red,green,blue))
            item.setBackground(painter)
            self.ui.listWidget_catagory.addItem(item)

        weapon_catagories = {}

        for weapon in attacks:
            for i in weapon[2:]:
                weapon_catagories[i] = 1
        if len(weapon_catagories.keys()) > 0:
            for catagory in sorted(weapon_catagories.keys()):
                item = QListWidgetItem("%s weapons" % catagory)
                item.catagory = catagory
                (red,green,blue)=(244, 178, 166)

        misc_catagories = {}
        for thing in misc:
            for i in thing[2:]:
                if ';' not in i:
                    misc_catagories[i] = 1

        if len(misc_catagories.keys()) > 0:
            #print weapon_catagories.keys()
            for catagory in sorted(misc_catagories.keys()):
                item = QListWidgetItem("%s misc" % catagory)
                item.catagory = catagory
                (red,green,blue)=(166, 179, 244)
                painter = QBrush(QColor(red,green,blue))
                item.setBackground(painter)
                self.ui.listWidget_catagory.addItem(item)
                painter = QBrush(QColor(red,green,blue))
                item.setBackground(painter)
                self.ui.listWidget_catagory.addItem(item)

        misc_catagories = {}
        for thing in misc:
            for i in thing[2:]:
                if ';' not in i:
                    misc_catagories[i] = 1

        if len(misc_catagories.keys()) > 0:
            #print weapon_catagories.keys()
            for catagory in sorted(misc_catagories.keys()):
                item = QListWidgetItem("%s misc" % catagory)
                item.catagory = catagory
                (red,green,blue)=(166, 179, 244)
                painter = QBrush(QColor(red,green,blue))
                item.setBackground(painter)
                self.ui.listWidget_catagory.addItem(item)

    def help_collect_options(self):
        print("help_collect_options")
        rlist = []
        option_list = []
        for row in range(0,len(self.ui.listWidget_catagory)):
            if self.ui.listWidget_catagory.item(row).isSelected():
                rlist.append(row)
        for row in rlist:
            option_list.append(self.ui.listWidget_catagory.item(row).text())
        return option_list


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MW = MainWindow()
    MW.load_session()
    MW.show()
    sys.exit(app.exec_())
