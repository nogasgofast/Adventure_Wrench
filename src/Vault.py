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
        self.ui.pushButton_the_shop.clicked.connect(self.ui_ts.show)
        self.ui.pushButton_acadamy.clicked.connect(self.ui_acadamy.show)
        self.ui.pushButton_add_to_encounter.clicked.connect(
                                       self.add_to_encounter)
        self.ui.pushButton_remove_from_encounter.clicked.connect(
                                       self.remove_from_encounter)
        self.ui.pushButton_delete_selected_items.clicked.connect(
                                       self.delete_from_vault)
        self.ui.pushButton_clear_delete.clicked.connect(
                                       self.clear_delete)
        self.load_vault()


    @db_session
    def load_vault(self):
        all_vault_assets = self.main.db.Vault.select()
        for vault_thing in all_vault_assets:
            item = QListWidgetItem(
                           f'''{vault_thing.name}\n{vault_thing.description}''')
            item.dbObj = vault_thing
            item.type = vault_thing.type
            item.isDeleting = False
            self.ui.listWidget_vault.addItem(item)


    @db_session
    def update_vault_summery(self, item):
        # if the name or description changes
        # we call this function to update the Vault item text.
        (red,green,blue)=(255,255,255)
        if item.isDeleting:
            green = 0
            blue = 0
        painter = QBrush(QColor(red,green,blue))
        item.setBackground(painter)


    # @db_session
    # def new_vault_item(self):
    #     item = QListWidgetItem(' *** ')
    #     vault_item = self.main.db.Vault(group_hp=[1,2,3,4],hp=6, max_hp=40,
    #                                     count=4, type='creature')
    #     item.dbObj = vault_item
    #     item.isDeleting = False
    #     self.update_vault_summery(item)
    #     self.ui.listWidget_vault.addItem(item)


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
    def remove_from_encounter(self):
        print(self.main.pos())
        self.move(50, 50)
        print(self.pos())



    @db_session
    def delete_from_vault(self):
        remove_these = []
        Vault = self.ui.listWidget_vault
        for row in range(0, Vault.count()):
            if Vault.item(row).isSelected():
                item = Vault.item(row)
                item.dbObj = self.main.db.Vault[item.dbObj.id]
                if item.isDeleting:
                    Vault.item(row).setSelected(False)
                    item.dbObj.delete()
                    remove_these.append(row)
                if not item.isDeleting:
                    item.isDeleting = True
                    self.update_vault_summery(item)
        commit()
        remove_these.sort()
        remove_these.reverse()
        for row in remove_these:
            Vault.takeItem(row)


    @db_session
    def clear_delete(self):
        Vault = self.ui.listWidget_vault
        for row in range(0, Vault.count()):
            item = Vault.item(row)
            item.dbObj = self.main.db.Vault[item.dbObj.id]
            item.isDeleting = False
            self.update_vault_summery(item)
