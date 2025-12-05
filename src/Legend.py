
from pony.orm import db_session, commit, desc
from PySide6.QtWidgets import (QDialog, QListWidgetItem,
                               QTreeWidgetItem, QMessageBox)
from PySide6.QtCore import Qt, QSignalBlocker
from ui.Legend_Dialog import Ui_Legend

class LegendDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui_vault = parent
        self.ui = Ui_Legend()
        self.ui.setupUi(self)
        self.ui.pushButton_legend_close.clicked.connect(self.close)
        self.load()


    def load(self):
        self.ui.listWidget_legend.clear()
        for stat in self.ui_vault.main.system_stats:
            name = self.ui_vault.main.system_stats[stat]['name']
            value = self.ui_vault.main.system_stats[stat]['value']
            key = QListWidgetItem(f"%{stat} : {name} defautl: {value}")
            self.ui.listWidget_legend.addItem(key)
        for macro in self.ui_vault.main.system_macros:
            name = self.ui_vault.main.system_macros[macro]
            key = QListWidgetItem(f"%{macro} : {name}")
            self.ui.listWidget_legend.addItem(key)
        custom_notes = {
                "%{}":"any dice notation bewteen { }",
                "%<>N": "any stat/macro can have a multiple between 2-9",
                "%<>/N": "any stat/macro can have a divisor between 2-9"}
        for note in custom_notes:
            key = QListWidgetItem(f"{note} : {custom_notes[note]}")
            self.ui.listWidget_legend.addItem(key)
