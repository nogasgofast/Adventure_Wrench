
from ui.Vault_Dialog import Ui_Vault
from PySide6.QtWidgets import QDialog

class VaultDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.main = parent
        self.ui = Ui_Vault()
        self.ui.setupUi(self)
        # self.ui_s = EncounterSelectorDialog(self)
        # self.ui_s.setModal(True)
        self.ui.pushButton_Summon.clicked.connect(self.summon_item)
        self.ui.pushButton_UnSummon.clicked.connect(self.unsummon_item)
        self.ui.pushButton_delete.clicked.connect(self.delete_item)

        # self.ui.pushButton_New.clicked.connect(self.ui_s.show)
        # self.ui.pushButton_save.clicked.connect(self.save_dialog)
        # self.ui.pushButton_load.clicked.connect(self.open_dialog)
        # self.ui.pushButton_back.clicked.connect(self.close)
        self.ui.listWidget_Display. \
            itemDoubleClicked.connect(self.toggle_item_view)
        # Set this value to keep track of my listItems
        self.itemID = 1

#   # def add_update_callback(self,update_callback):
#   #     self.main_window_callback = update_callback

    def toggle_item_view(self):
        # print("toggle_item_view")
        for row in range(0, len(self.ui.listWidget_Display)):
            if self.ui.listWidget_Display.item(row).isSelected():
                item = self.ui.listWidget_Display.item(row)
                if item.ViewTxt:
                    item.setText('- %s' % item.encounter.to_string())
                else:
                    item.setText('+ %s' % item.encounter.get_option('name'))
                item.ViewTxt = not item.ViewTxt

    def open_dialog(self):
        # print("open_dialog")
        fileName = QFileDialog.getOpenFileName(self,
                                               "Open Save Files",
                                               "~",
                                               "Pickles (*.pickle)")
        if fileName:
            self.load_encounters(fileName)

    def save_dialog(self):
        # print("save_dialog")
        fileName = QFileDialog.getSaveFileName(self,
                                               "Save File Name",
                                               "encounters.pickle",
                                               "Pickles (*.pickle)")
        if fileName:
            self.save_encounters(fileName)

    def save_encounters(self, fh=None):
        # print("save_encounters")
        # try:
        if fh:
            fh = open(fh, 'wb')
        else:
            fh = open('encounters.pickle', 'wb')
        pack = {}
        # items in encounter window?
        pack['encounters'] = []
        for row in range(0, len(self.ui.listWidget_Display)):
            item = self.ui.listWidget_Display.item(row)
            if item:
                pack['encounters'].append(item.encounter)
        pack['itemID'] = self.itemID
        pickle.dump(pack, fh, 2)
        fh.close()
        # except:
        #     QMessageBox.question(self,
        #                          'Wisdom.',
        #                          'Unable to write file',
        #                          QMessageBox.Ok)

    def load_encounters(self, fh=None):
        # print("load_encounters")
        # try:
        if fh:
            fh = open(fh, 'rb')
        else:
            fh = open('encounters.pickle', 'rb')
        pack = pickle.load(fh)
        # for row in range(0, len(self.ui.listWidget_Display)):
        #    self.ui.listWidget_Display.takeItem(0)
        for encounter in pack['encounters']:
            self.add_item(encounter)
        # except:
        #     QMessageBox.question(self,
        #                          'Wisdom.',
        #                          'Sorry no save 0_o',
        #                          QMessageBox.Ok)

    def summon_item(self, encounter=False):
        # print("summon_item")
        '''set display item for main window.'''
        for row in range(0, self.ui.listWidget_Display.count()):
            if self.ui.listWidget_Display.item(row).isSelected():
                item = self.ui.listWidget_Display.item(row)
                encItem = QListWidgetItem('***')
                encItem.encounter = item.encounter.copy()
                update_text(encItem)
                self.main.ui.listWidget_Encounter.addItem(encItem)

    def delete_item(self):
        # print("delete_item")
        unSummonList = {}
        Remove = []
        # find selected items to delete
        for row in range(0, len(self.ui.listWidget_Display)):
            if self.ui.listWidget_Display.item(row).isSelected():
                # follow me here an item has it's position. But also
                # has an identifier I can use to track down copies
                # check out self.add_item().
                unSummonList[row] = self.ui.listWidget_Display. \
                    item(row).encounter.get_option('id')
                for mainWindowRow in range(0,
                                           len(self.main.ui.
                                               listWidget_Encounter)):
                    cur_Item = self.main.ui. \
                        listWidget_Encounter.item(mainWindowRow)
                    if cur_Item.encounter. \
                            get_option('id') == unSummonList[row]:
                        Remove.append(mainWindowRow)

        # be careful to not change the index of the items
        # you found as you remove them. So remove from the end first.
        # we don't need those values anymore though
        unSummonList = list(unSummonList.keys())
        unSummonList.sort()
        unSummonList.reverse()
        Remove.sort()
        Remove.reverse()

        # remove items from the encounter applet
        for row in unSummonList:
            self.ui.listWidget_Display.takeItem(row)
        # remove items from the initive window (main)
        for row in Remove:
            self.main.ui.listWidget_Encounter.takeItem(row)

    def unsummon_item(self):
        # print("unsummon_item")
        unSummonList = {}
        Remove = []
        # find selected items to delete
        for row in range(0, len(self.ui.listWidget_Display)):
            if self.ui.listWidget_Display.item(row).isSelected():
                # follow me here an item has it's position. But also
                # has an identifier I can use to track down copies
                # check out self.add_item() .
                unSummonList[row] = self.ui. \
                    listWidget_Display.item(row).encounter.get_option('id')
                for mainWindowRow in range(0,
                                           len(self.main.ui.
                                               listWidget_Encounter)):
                    cur_Item = self.main.ui. \
                        listWidget_Encounter.item(mainWindowRow)
                    if cur_Item.encounter. \
                            get_option('id') == unSummonList[row]:
                        Remove.append(mainWindowRow)
        # things in the list change position as you remove them. So i
        # must arrange for the deletion to happen in the right order.
        Remove.sort()
        Remove.reverse()
        # remove items from the initive window (main)
        for row in Remove:
            self.main.ui.listWidget_Encounter.takeItem(row)
