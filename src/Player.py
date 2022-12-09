
from lib.display_utils import update_text
from lib.encounter import Encounter
from ui.Player_Dialog import Ui_Player
from PySide6.QtWidgets import QDialog, QListWidgetItem

class PlayerDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.main = parent
        self.target = None
        self.ui = Ui_Player()
        self.ui.setupUi(self)
        self.ui.lineEdit_name.textChanged.connect(self.update_name)
        self.ui.spinBox_hp.valueChanged.connect(self.update_hp)
        self.ui.spinBox_initiative.valueChanged.connect(self.update_inititive)
        self.ui.textEdit_description.textChanged.connect(self.update_description)
        self.ui.pushButton_delete.clicked.connect(self.remove_player)

    def update_player(self):
        # this may make more sense in main.py if I decide to add update
        # functionality to Other types of objects
        for row in range(0, self.main.ui.listWidget_Encounter.count()):
            if self.main.ui.listWidget_Encounter.item(row).isSelected():
                item = self.main.ui.listWidget_Encounter.item(row)
                if item.encounter.get_option('type') == 'pc':
                    self.target = item
                    self.ui.lineEdit_name.setText(item.encounter.get_option('name'))
                    self.ui.spinBox_hp.setValue(item.encounter.get_option('hp'))
                    self.ui.spinBox_initiative.setValue(item.encounter.get_option('initiative'))
                    text = "\n".join(item.encounter.get_option('abilities'))
                    self.ui.textEdit_description.setText(text)
                    self.show()
                else:
                    # we detected this as not a player so we don't do nothin.
                    pass

    def update_name(self):
        # if this seems strange, i have to ensure this function always updates
        # the name combo box. Because lineEdit_name.insertPolicy
        # is set to do nothing.
        name = self.ui.lineEdit_name.text()
        self.target.encounter.set_option('name', name)
        update_text(self.target)

    def update_hp(self):
        hp = self.ui.spinBox_hp.value()
        self.target.encounter.set_option('hp', hp)
        self.target.encounter.set_option('maxHP', hp)
        update_text(self.target)

    def update_inititive(self):
        initiative = self.ui.spinBox_initiative.value()
        self.target.encounter.set_option('initiative', initiative)
        update_text(self.target)

    def update_description(self):
        text = self.ui.textEdit_description.toPlainText().split('\n')
        # there is a race condition where this update gets called
        # immediatly when the first player ui is spawned. Not sure
        # why it does not happen for the other updates ^ ??
        if self.target:
            self.target.encounter.set_option('abilities', text)
            update_text(self.target)

    def add_player(self):
        # prepare a new container for the item
        player = Encounter()
        player.set_option('hp', 1)
        player.set_option('maxHP', 1)
        player.set_option('groupOf', 1)
        initiative = 1
        hp = 1
        name = ' *** '
        item = QListWidgetItem("%s | %s | hp:%s" % (
                                    initiative,
                                    name,
                                    hp))
        # initiative window requires these attributes be added to items
        item.encounter = player
        item.encounter.set_option('type', 'pc')
        update_text(item)
        self.main.ui.listWidget_Encounter.addItem(item)
        self.target = item
        # clear ui for adding a new player
        self.ui.lineEdit_name.setText('')
        self.ui.lineEdit_name.setFocus()
        self.ui.spinBox_hp.setValue(1)
        self.ui.spinBox_initiative.setValue(1)
        self.ui.textEdit_description.setText('')
        self.show()

    def remove_player(self):
        # print("remove_player")
        index = self.main.ui.listWidget_Encounter.indexFromItem(self.target)
        print(index)
        self.main.ui.listWidget_Encounter.takeItem(index.row())
        self.close()

#        name = self.ui.lineEdit_name.text()
#        Remove = []
#        for row in range(0, self.main.ui.listWidget_Encounter.count):
#            item = self.main.ui.listWidget_Encounter.item(row)
#            if item.encounter.get_option('name') == name:
#                Remove.append(row)
#        Remove.sort()
#        Remove.reverse()
#        for row in Remove:
#            self.main.ui.listWidget_Encounter.takeItem(row)
#        self.ui.lineEdit_name.removeItem(self.ui.lineEdit_name.currentIndex())
