# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QDialog
from ui.TheShop_Dialog import Ui_TheShop


class TheShopDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.vault = parent
        self.ui = Ui_TheShop()
        self.ui.setupUi(self)
