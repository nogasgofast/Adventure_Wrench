
from lib.encounter import Encounter
from ui.Player_Dialog import Ui_Player
from PySide6.QtWidgets import QDialog

class PlayerDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.main = parent
        self.ui = Ui_Player()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.add_player)
        self.ui.pushButton_delete.clicked.connect(self.remove_player)

    def add_player(self):
        # print("add_player")
        # roll initiative
        player = Encounter()
        initiative = self.ui.spinBox_initiative.value()
        player.set_option('initiative', initiative)
        hp = self.ui.spinBox_hp.value()
        player.set_option('hp', hp)
        player.set_option('maxHP', hp)
        # if this seems strange, i have to ensure this function always updates
        # the name combo box. Because comboBox_name.insertPolicy
        # is set to do nothing.
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
        # print("remove_player")
        name = self.ui.comboBox_name.currentText()
        Remove = []
        for row in range(0, len(self.main.ui.listWidget_Encounter)):
            item = self.main.ui.listWidget_Encounter.item(row)
            if item.encounter.get_option('name') == name:
                Remove.append(row)
        Remove.sort()
        Remove.reverse()
        for row in Remove:
            self.main.ui.listWidget_Encounter.takeItem(row)
        self.ui.comboBox_name.removeItem(self.ui.comboBox_name.currentIndex())
