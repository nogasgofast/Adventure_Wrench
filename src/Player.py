
from ui.Player_Dialog import Ui_Player
from PySide6.QtWidgets import QDialog, QListWidgetItem
from pony.orm import db_session, commit

class PlayerDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.main = parent
        self.target = None
        self.ui = Ui_Player()
        self.ui.setupUi(self)

        self.ui.pushButton_delete.clicked.connect(self.remove_player)
        self.ui.pushButton_back.clicked.connect(self.close)

        self.ui.spinBox_hp.valueChanged.connect(self.update_hp)
        self.ui.spinBox_initiative.valueChanged.connect(self.update_inititive)

        self.ui.lineEdit_name.textChanged.connect(self.update_name)

        self.ui.textEdit_description.textChanged.connect(self.update_description)


    @db_session
    def update_player(self):
        # this may make more sense in main.py if I decide to add update
        # functionality to Other types of objects
        E = self.main.ui.listWidget_Encounter
        for row in range(0, E.count()):
            if E.item(row).isSelected():
                item = E.item(row)
                item.dbObj = self.main.db.Active[item.dbObj.id]
                self.target = item
                self.ui.lineEdit_name.setText(item.dbObj.name)
                self.ui.spinBox_hp.setValue(item.dbObj.hp)
                self.ui.spinBox_initiative.setValue(item.dbObj.initiative)
                self.ui.textEdit_description.setText(item.dbObj.stat_block)
                self.show()


    @db_session
    def update_name(self):
        name = self.ui.lineEdit_name.text()
        # reaquire state from db. Pony implementation requires this.
        self.target.dbObj = self.main.db.Active[self.target.dbObj.id]
        self.target.dbObj.name = name
        commit()
        self.main.update_encounter_text(self.target)

    @db_session
    def update_hp(self):
        hp = self.ui.spinBox_hp.value()
        self.main.ui.spinBox_main_hp.setValue(hp)
        # self.main.update_hp(hp)

    @db_session
    def update_inititive(self):
        initiative = self.ui.spinBox_initiative.value()
        self.main.ui.spinBox_main_initiative.setValue(initiative)
        # self.main.update_initiative(initiative)

    @db_session
    def update_description(self):
        text = self.ui.textEdit_description.toPlainText()
        # there is a race condition where this update gets called
        # immediatly when the first player ui is spawned. Not sure
        # why it does not happen for the other updates ^ ??
        if self.target:
            # reaquire state from db. Pony implementation requires this.
            dbObj = self.main.db.Active[self.target.dbObj.id]
            dbObj.stat_block = text
            commit()
            self.main.update_encounter_text(self.target)

    @db_session
    def add_player(self):
        player = self.main.db.Active(player=True)
        commit()
        item = QListWidgetItem("{player.initiative} | {player.name} | hp:{player.hp}")
        item.dbObj = player
        commit()
        self.main.update_encounter_text(item)
        self.target = item
        self.main.ui.listWidget_Encounter.addItem(item)
        # clear ui for adding a new player
        self.ui.lineEdit_name.setText('')
        self.ui.lineEdit_name.setFocus()
        self.ui.spinBox_hp.setValue(1)
        self.ui.spinBox_initiative.setValue(1)
        self.ui.textEdit_description.setText('')
        self.show()

    @db_session
    def remove_player(self):
        # reaquire state from db. Pony implementation requires this.
        self.target.dbObj = self.main.db.Active[self.target.dbObj.id]
        self.target.dbObj.delete()
        commit()
        index = self.main.ui.listWidget_Encounter.indexFromItem(self.target)
        self.main.ui.listWidget_Encounter.takeItem(index.row())
        self.close()
