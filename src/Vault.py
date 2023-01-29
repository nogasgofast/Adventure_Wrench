from pony.orm import db_session, commit
from ui.Vault_Dialog import Ui_Vault
from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6.QtGui import QBrush, QColor
from Acadamy import AcadamyDialog
from TheShop import TheShopDialog

class VaultDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.main = parent
        self.ui = Ui_Vault()
        self.ui.setupUi(self)
        self.ui_acadamy = AcadamyDialog(self)
        self.ui_ts = TheShopDialog(self)
        self.ui.pushButton_the_shop.clicked.connect(self.ui_ts.new_vault_item)
        self.ui.pushButton_acadamy.clicked.connect(self.ui_acadamy.show)
        self.ui.pushButton_add_to_encounter.clicked.connect(
                                       self.add_to_encounter)
        self.ui.pushButton_remove_from_encounter.clicked.connect(
                                       self.remove_from_encounter)
        self.ui.pushButton_delete_selected_items.clicked.connect(
                                       self.delete_from_vault)

        self.ui.listWidget_vault.doubleClicked.connect(self.ui_ts.load_vault_item)
        self.load_vault()


    @db_session
    def remove_from_encounter(self):
        pass

    @db_session
    def load_vault(self):
        all_vault_items = self.main.db.Vault.select()
        for vault_item in all_vault_items:
            item = QListWidgetItem(
                           f'{vault_item.name}')
            item.dbObj = vault_item
            self.ui.listWidget_vault.addItem(item)

    @db_session
    def update_vault_item(self, target):
        vault = self.ui.listWidget_vault
        for row in range(0, vault.count()):
            item = vault.item(row)
            dbObj = db.Vault[item.dbObj.id]
            target = db.Vault[target.dbObj.id]
            if dbObj == target:
                item.setText(dbObj.name)


    @db_session
    def add_to_encounter(self):
        enc_list = self.main.ui.listWidget_Encounter
        Vault = self.ui.listWidget_vault
        for row in range(0, Vault.count()):
            if Vault.item(row).isSelected():
                item = Vault.item(row)
                item.dbObj = self.main.db.Vault[item.dbObj.id]
                new_item = QListWidgetItem()
                new_item.dbObj = self.main.db.Active(
                                name = item.dbObj.name,
                                description = item.dbObj.description,
                                initiative = item.dbObj.initiative,
                                hp = item.dbObj.hp,
                                max_hp = item.dbObj.max_hp,
                                group_hp = item.dbObj.group_hp,
                                count = item.dbObj.count,
                                type = item.dbObj.type)
                commit()
                self.main.update_encounter_text(new_item)
                self.main.ui.listWidget_Encounter.addItem(new_item)


    @db_session
    def delete_from_vault(self):
        remove_these = []
        Vault = self.ui.listWidget_vault
        for row in range(0, Vault.count()):
            if Vault.item(row).isSelected():
                item = Vault.item(row)
                item.dbObj = self.main.db.Vault[item.dbObj.id]
                item.dbObj.delete()
                remove_these.append(row)
                commit()
                Vault.takeItem(row)
                break
