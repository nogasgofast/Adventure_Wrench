#!/usr/bin/python
import sys
import dice
import pickle
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from w_main import Ui_MainWindow
from d_encounter import Ui_Encounter
from d_configurator import Ui_configurator
from d_player import Ui_Player
from encounter import Encounter, option_list
from display_utils import update_text

class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_e = MyDialog(self)
        self.ui_e.setModal(True)
        self.ui.pushButton_Encounter.clicked.connect(self.ui_e.show)
        self.ui_p = MyPlayer(self)
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
        for row in range(0,len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.isItemSelected(
            self.ui.listWidget_Encounter.item(row)):        
                item = self.ui.listWidget_Encounter.item(row)
                new = (item.encounter.get_option(kind) + 1) % cycle
                item.encounter.set_option(kind,new)
                update_text(item)

    def closeEvent(self, event):
        quit_msg = "Replace default save file ?"
        reply = QMessageBox.question(self, 'Message', 
                        quit_msg, QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.save_session()
            event.accept()
        else:
            event.accept()
            
    def kill_remove(self):
        remove_these = []
        for row in range(0,len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.isItemSelected(
            self.ui.listWidget_Encounter.item(row)):
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
        fileName = QFileDialog.getOpenFileName(self,
                                               "Open Save Files",
                                               "~",
                                               "Pickles (*.pickle)")
        if fileName:
            self.load_session(fileName)

    def save_dialog(self):
        fileName = QFileDialog.getSaveFileName(self,
                                               "Save File Name",
                                               "MyGame.pickle",
                                               "Pickles (*.pickle)")
        if fileName:
            self.save_session(fileName)

    def save_session(self,fh=None):
        try:
            if fh:
                fh = open(fh,'w')
            else:
                fh = open('saved_session.pickle','w')
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
            pickle.dump(pack, fh, 2)
            fh.close()
        except:
            QMessageBox.question(self,
                                 'Wisdom.',
                                 'Unable to write file',
                                 QMessageBox.Ok)           

    def load_session(self,fh=None):
        try:
            if fh:
                fh = open(fh)
            else:
                fh = open('saved_session.pickle')
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
        self.suppress_spinbox_update = True
        for row in range(0,len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.isItemSelected(
            self.ui.listWidget_Encounter.item(row)):
                item = self.ui.listWidget_Encounter.item(row)
                self.ui.spinBox_main_initiative.setValue(
                    item.encounter.get_option('initiative'))
                self.ui.spinBox_main_hp.setValue(
                    item.encounter.get_option('hp'))
        self.suppress_spinbox_update = False

    def  update_creature_initiative(self):
        if self.suppress_spinbox_update:
            pass
        else:
            for row in range(0,len(self.ui.listWidget_Encounter)):
                if self.ui.listWidget_Encounter.isItemSelected(
                self.ui.listWidget_Encounter.item(row)):
                    item = self.ui.listWidget_Encounter.item(row)
                    item.encounter.set_option('initiative',
                        self.ui.spinBox_main_initiative.value())
                    update_text(item)

    def  update_creature_hp(self):
        if self.suppress_spinbox_update:
            pass
        else:
            newHP = self.ui.spinBox_main_hp.value()
            for row in range(0,len(self.ui.listWidget_Encounter)):
                if self.ui.listWidget_Encounter.isItemSelected(
                self.ui.listWidget_Encounter.item(row)):
                    item = self.ui.listWidget_Encounter.item(row)
                    if item.encounter.get_option('groupOf') == 1:
                        item.encounter.set_option('hp', newHP)
                    if item.encounter.get_option('maxHP') < newHP: 
                        item.encounter.set_option('maxHP', newHP)
                    update_text(item)

    def damage_thing(self,damage):
        for row in range(0,len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.isItemSelected(
            self.ui.listWidget_Encounter.item(row)):
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
        for row in range(0,len(self.ui.listWidget_Encounter)):
            if self.ui.listWidget_Encounter.isItemSelected(
            self.ui.listWidget_Encounter.item(row)):
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
        self.ui.listView_Encounter()

    def advance_initiative(self):
        flag = False
        initiative = 0
        E = self.ui.listWidget_Encounter
        for row in range(0,len(E)):
            if E.isItemSelected(E.item(row)):
                initiative = E.item(row).encounter.get_option('initiative')
                E.setItemSelected(E.item(row), False)
                flag = True
                break
        self.sort_initiative()
        if flag:
            flag2 = False
            for row in range(0,len(E)):
                if E.item(row).encounter.get_option('initiative') < initiative:
                    E.setItemSelected( E.item(row), True)
                    flag2 = True
                    break
            if not flag2:
                E.setItemSelected(E.item(0), True)
        else:
            E.setItemSelected(E.item(0), True)

    def sort_initiative(self):
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

class MyPlayer(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.main = parent
        self.ui = Ui_Player()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.add_player)
        self.ui.pushButton_delete.clicked.connect(self.remove_player)


    def add_player(self):
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


class MyDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.main = parent    
        self.ui = Ui_Encounter()
        self.ui.setupUi(self)
        self.ui_s = MySelector(self)
        self.ui_s.setModal(True)
        self.ui.pushButton_Summon.clicked.connect(self.summon_item)
        self.ui.pushButton_UnSummon.clicked.connect(self.unsummon_item)
        self.ui.pushButton_create.clicked.connect(self.add_item)
        self.ui.pushButton_delete.clicked.connect(self.delete_item)
        self.ui.pushButton_UnSummon.clicked.connect(self.unsummon_item)
        self.ui.pushButton_clear.clicked.connect(self.reset_stats)
        self.ui.pushButton_Select.clicked.connect(self.ui_s.show)
        self.ui.pushButton_save.clicked.connect(self.save_dialog)
        self.ui.pushButton_load.clicked.connect(self.open_dialog)
        self.ui.pushButton_back.clicked.connect(self.close)
        self.ui.comboBox_type.currentIndexChanged.connect(self.change_type)
        self.ui.listWidget_Display.itemDoubleClicked.connect(self.toggle_item_view)
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
        # Set this value to keep track of my listItems
        self.itemID = 1

#    def add_update_callback(self,update_callback):
#        self.main_window_callback = update_callback

    def toggle_item_view(self):
        for row in range(0,len(self.ui.listWidget_Display)):
            if self.ui.listWidget_Display.isItemSelected(
            self.ui.listWidget_Display.item(row)):
                item = self.ui.listWidget_Display.item(row)
                if not item.txt:
                    item.setText('- %s' % item.encounter.to_string())
                    item.txt = 1
                else:
                    item.setText('+ %s' % item.encounter.get_option('name'))
                    item.txt = 0

    def open_dialog(self):
        fileName = QFileDialog.getOpenFileName(self,
                                               "Open Save Files",
                                               "~",
                                               "Pickles (*.pickle)")
        if fileName:
            self.load_encounters(fileName)

    def save_dialog(self):
        fileName = QFileDialog.getSaveFileName(self,
                                               "Save File Name",
                                               "encounters.pickle",
                                               "Pickles (*.pickle)")
        if fileName:
            self.save_encounters(fileName)

    def save_encounters(self,fh=None):
        try:
            if fh:
                fh = open(fh,'w')
            else:
                fh = open('encounters.pickle','w')
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
        try:
            if fh:
                fh = open(fh)
            else:
                fh = open('encounters.pickle')
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

    def change_type(self):
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
        self.ui.label_speed.hide()
        self.ui.comboBox_speed.hide()
        self.ui.spinBox_speed.hide()

    def show_speed(self):
        self.ui.label_speed.hide()
        self.ui.comboBox_speed.hide()
        self.ui.spinBox_speed.hide()

    def hide_stats(self):
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
        'if the spinbox changes value save it here'
        locomotive = str(self.ui.comboBox_speed.itemText(
            self.ui.comboBox_speed.currentIndex()))
        self.locomotives[locomotive] = self.ui.spinBox_speed.value()
    
    def link_save_and_change_speed(self):
        'set spinbox to new value according to my model'
        locomotive = str(self.ui.comboBox_speed.itemText(
            self.ui.comboBox_speed.currentIndex()))
        self.ui.spinBox_speed.setValue(
            self.locomotives[locomotive])

    def sqrt(self,num):
        if (num / 2) > 1:
            return num / 2
        else:
            return 0

    def gen_creature(self):
        new_creature = Encounter()
        cr_from_ui = self.ui.spinBox_CR.value()
        num_in_group = self.ui.spinBox_group.value()
        TargetCR = cr_from_ui - self.sqrt(num_in_group)
        new_creature.set_option('speed',self.locomotives)
        new_creature.set_option('size', str(self.ui.comboBox_size.itemText(
            self.ui.comboBox_size.currentIndex())))
        new_creature.set_option('name', str(self.ui.lineEdit_Name.text()))
        new_creature.set_option('groupOf', int(self.ui.spinBox_group.value()))
        new_creature.import_cr(TargetCR)
        new_creature.import_options(self.ui_s.help_collect_options())
        new_creature.import_stats(
            self.ui.spinBox_STR.value(),
            self.ui.spinBox_DEX.value(),
            self.ui.spinBox_CON.value(),
            self.ui.spinBox_WIS.value(),
            self.ui.spinBox_INT.value(),
            self.ui.spinBox_CHA.value())
        new_creature.gen_actions()
        return new_creature

    def add_item(self,encounter=False):
        if not encounter:
            dice_caddy = dice.dice()
            encounter = self.gen_creature()
            #roll initiatives
            dex_mod = (encounter.data['stats']['DEX'] - 10) / 2
            encounter.set_option('initiative',
                                dice_caddy.roll('1d20+%s' % (dex_mod)))
            groupHP = []
            if encounter.get_option('groupOf') > 1:
                for creature in range(0,encounter.get_option('groupOf')):
                    #print "to_dice=%s"% (encounter.to_dice())
                    groupHP.append(dice_caddy.roll('%s' % encounter.to_dice()))
                encounter.set_option('groupHP', groupHP)
            else:
                #print "to_dice=%s"% (encounter.to_dice())
                hp = dice_caddy.roll('%s' % encounter.to_dice())
                encounter.set_option('hp', hp)
            encounter.set_option('type', self.ui.comboBox_type.currentText())
        # add item to encounter window
        item = QListWidgetItem("+ %s" % encounter.get_option('name'))
        item.txt = 0
        item.setToolTip("%s" % encounter.to_string())
        item.encounter = encounter
        item.encounter.set_option('id', self.itemID)
        self.ui.listWidget_Display.addItem(item)
        self.itemID += 1
        #help keyboard users to get back to name
        self.ui.lineEdit_Name.setFocus()

    def summon_item(self,encounter=False):
        '''set display item for main window.'''
        for row in range(0,len(self.ui.listWidget_Display)):
            if self.ui.listWidget_Display.isItemSelected(self.ui.listWidget_Display.item(row)):
                item = self.ui.listWidget_Display.item(row)
                encItem = QListWidgetItem('***')
                encItem.encounter = item.encounter.copy()
                update_text(encItem)
                self.main.ui.listWidget_Encounter.addItem(encItem)

    def delete_item(self):
        unSummonList = {}
        Remove = []
        #find selected items to delete
        for row in range(0,len(self.ui.listWidget_Display)):
            if self.ui.listWidget_Display.isItemSelected(
            self.ui.listWidget_Display.item(row)):
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
        unSummonList = unSummonList.keys()
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
        unSummonList = {}
        Remove = []
        #find selected items to delete
        for row in range(0,len(self.ui.listWidget_Display)):
            if self.ui.listWidget_Display.isItemSelected(
            self.ui.listWidget_Display.item(row)):
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

    def reset_stats(self):
        self.ui.spinBox_STR.setProperty("value", 10)
        self.ui.spinBox_DEX.setProperty("value", 10)
        self.ui.spinBox_CON.setProperty("value", 10)
        self.ui.spinBox_WIS.setProperty("value", 10)
        self.ui.spinBox_INT.setProperty("value", 10)
        self.ui.spinBox_CHA.setProperty("value", 10)


class MySelector(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.encounter = parent
        self.ui = Ui_configurator()
        self.ui.setupUi(self)
        self.update_options_list()
        self.ui.pushButton_back.clicked.connect(self.close)
        self.ui.listWidget_catagory.itemSelectionChanged.connect(self.show_hide_options)
        self.ui.lineEdit_search.textChanged.connect(self.auto_search)
        self.ui.pushButton_reset.clicked.connect(self.reset_selected)

    def reset_selected(self):
        for row in range(0,len(self.ui.listWidget_catagory)):
            item = self.ui.listWidget_catagory.item(row)
            if self.ui.listWidget_catagory.isItemSelected(item):
                self.ui.listWidget_catagory.setItemSelected(item,False)
        self.ui.listWidget_options.clear()

    def auto_search(self):
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
        ol = option_list()
        enc_type = self.encounter.ui.comboBox_type.currentText()
        selection = []
        for row in range(0,len(self.ui.listWidget_catagory)):
            if self.ui.listWidget_catagory.isItemSelected(
              self.ui.listWidget_catagory.item(row)):
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
        self.ui.listWidget_catagory.clear()
        ol = option_list()
        enc_type = self.encounter.ui.comboBox_type.currentText()
        attribute = ol.get_options(enc_type, 'attribute')
        attacks = ol.get_options(enc_type, 'weapon')
        misc  = ol.get_options(enc_type, 'misc')
        
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
        if weapon_catagories.keys() > 0:
            for catagory in sorted(weapon_catagories.keys()):
                item = QListWidgetItem("%s weapons" % catagory)
                item.catagory = catagory
                (red,green,blue)=(244, 178, 166)
                painter = QBrush(QColor(red,green,blue))
                item.setBackground(painter)
                self.ui.listWidget_catagory.addItem(item)

        misc_catagories = {}
        for thing in misc:
            for i in thing[2:]:
                if ';' not in i:
                    misc_catagories[i] = 1

        if misc_catagories.keys() > 0:
            #print weapon_catagories.keys()
            for catagory in sorted(misc_catagories.keys()):
                item = QListWidgetItem("%s misc" % catagory)
                item.catagory = catagory
                (red,green,blue)=(166, 179, 244)
                painter = QBrush(QColor(red,green,blue))
                item.setBackground(painter)
                self.ui.listWidget_catagory.addItem(item)

    def help_collect_options(self):
        rlist = []
        option_list = []
        for row in range(0,len(self.ui.listWidget_catagory)):
            if self.ui.listWidget_catagory.isItemSelected(
            self.ui.listWidget_catagory.item(row)):
                rlist.append(row)
        for row in rlist:
            option_list.append(self.ui.listWidget_catagory.item(row).text())
        return option_list


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyWindow()
    mainWindow.load_session()
    mainWindow.show()
    sys.exit(app.exec_())
        
