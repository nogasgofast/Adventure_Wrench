# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import (QDialog, QListWidgetItem)
from ui.TheShop_Dialog import Ui_TheShop
from pony.orm import db_session, commit
from lib.dice import dice


class TheShopDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.vault = parent
        self.ui = Ui_TheShop()
        self.ui.setupUi(self)
        self.target = None

        self.ui.pushButton_roll_stats.clicked.connect(self.roll_stats)
        self.ui.pushButton_back.clicked.connect(self.close)
        self.ui.pushButton_add_templates.clicked.connect(self.add_template)
        self.ui.pushButton_delete_shop.clicked.connect(self.delete_vault_item)
        self.ui.pushButton_remove_templates.clicked.connect(self.remove_template)

        self.ui.lineEdit_name.textEdited.connect(self.update_name)
        self.ui.textEdit_stat_block.textChanged.connect(self.save_stat_block_Changes)

    @db_session
    def save_stat_block_Changes(self):
        db = self.vault.main.db
        dbObj = db.Vault[self.target.id]
        dbObj.stat_block = self.ui.textEdit_stat_block.toPlainText()


    @db_session
    def load_vault_item(self):
        db = self.vault.main.db
        vault = self.vault.ui.listWidget_vault
        for row in range(0, vault.count()):
            item = vault.item(row)
            if item.isSelected():
                self.target = item.dbObj
                break
        self.target = db.Vault[self.target.id]
        # TODO update individual things
        self.ui.lineEdit_name.setText(self.target.name)
        self.ui.spinBox_cr.setValue(self.target.cr)
        self.ui.spinBox_group_of.setValue(self.target.count)
        stats = self.target.attributes.split(',')
        stats = [ int(x) for x in stats ]
        self.ui.spinBox_STR.setValue(stats[0])
        self.ui.spinBox_DEX.setValue(stats[1])
        self.ui.spinBox_CON.setValue(stats[2])
        self.ui.spinBox_WIS.setValue(stats[3])
        self.ui.spinBox_INT.setValue(stats[4])
        self.ui.spinBox_CHA.setValue(stats[5])
        self.ui.textEdit_stat_block.setPlainText(self.target.stat_block)
        self.update_applied_templates()
        self.update_selector_templates()
        self.show()

    @db_session
    def update_applied_templates(self):
        db = self.vault.main.db
        self.ui.listWidget_templates.clear()
        vault_item = db.Vault[self.target.id]
        for template in vault_item.templates:
            item  = QListWidgetItem(template.name)
            item.dbObj = template
            self.ui.listWidget_templates.addItem(item)

    @db_session
    def new_vault_item(self):
        db = self.vault.main.db
        self.target = db.Vault(name='*new vault item*',
                               cr=1,
                               count=1,
                               attributes='10,10,10,10,10,10')
        commit()
        item = QListWidgetItem('*new vault item*')
        item.dbObj = self.target
        self.vault.ui.listWidget_vault.addItem(item)
        self.update_stat_block()
        self.show()


    @db_session
    def update_name(self):
        db = self.vault.main.db
        self.target = db.Vault[self.target.id]
        self.target.name = self.ui.lineEdit_name.text()
        self.vault.update_vault_item(self.target)
        self.update_stat_block()


    @db_session
    def update_stat_block(self):
        'responsible for Stat Block on The Shop'
        db = self.vault.main.db
        dbObj = db.Vault[self.target.id]
        stat_block = self.compile_templates()

        # pull in The Shop's stats to compile with these
        def compile_attr(attribute, stat_mod):
            if stat_mod is None:
                return int(attribute)
            if '+' not in stat_mod and '-' not in stat_mod:
                print(stat_mod)
                return int(stat_mod)
            else:
                return int(attribute) + int(stat_mod)

        base_attributes = dbObj.attributes.split(',')
        scores = base_attributes
        names = ('Strength', 'Dexterity',
                 'Constitution', 'Wisdom',
                 'Intelligence', 'Charisma')
        for row in range(0, 6):
            scores[row] = compile_attr(scores[row],
                                       stat_block['stats'].get(names[row]))

        heading = ('STR', 'DEX',
                   'CON', 'WIS',
                   'INT', 'CHA')
        final_scores = ''
        for row in range(0, 6):
            final_scores += f'{heading[row]}:{scores[row]:02}    '
        name = self.ui.lineEdit_name.text()

        plainText = f'{name}\n{final_scores}'

        sections = ('lore', 'attributes',
                    'items', 'actions',
                    'roll_tables' )
        for section in range(0, len(sections)):
            for key, text in stat_block[sections[section]].items():
                print(text)
                plainText += f'\n{text}'
        self.ui.textEdit_stat_block.setPlainText(plainText)

    @db_session
    def compile_templates(self):
        db = self.vault.main.db
        details = {'lore':{},
                   'stats':{},
                   'attributes':{},
                   'items': {},
                   'actions': {},
                   'roll_tables': {} }

        def stack_details(details, template):
            for item in template.lore:
                details['lore'][item.name] = item.to_strings()
            for item in template.stats:
                details['stats'][item.name] = item.description
            for item in template.attributes:
                details['attributes'][item.name] = item.to_strings()
            for item in template.items:
                details['items'][item.name] = item.to_strings()
            for item in template.actions:
                details['actions'][item.name] = item.to_strings()
            for item in template.rtables:
                details['roll_tables'][item.name] = item.to_strings()
            return details

        def stack(details, template):
            # start with the template we were given.
            details = stack_details(details, template)
            # compile all the templates under that.
            for sub_template in template.under:
                details = stack(details, sub_template)
            return details

        vault_item = db.Vault[self.target.id]
        for template in vault_item.templates:
            details = stack(details, template)
        return details


    @db_session
    def roll_stats(self):
        db = self.vault.main.db
        dbObj = db.Vault[self.target.id]
        dice_tower = dice()
        # roll 4d6 but keep the top 3
        stats = [ dice_tower.roll('4d6t3') for r in range(6)]
        # print(stats)
        self.ui.spinBox_STR.setValue(stats[0])
        self.ui.spinBox_DEX.setValue(stats[1])
        self.ui.spinBox_CON.setValue(stats[2])
        self.ui.spinBox_WIS.setValue(stats[3])
        self.ui.spinBox_INT.setValue(stats[4])
        self.ui.spinBox_CHA.setValue(stats[5])
        stats = [ str(s) for s in stats ]
        dbObj.attributes = ','.join(stats)
        commit()
        self.update_stat_block()

    @db_session
    def update_selector_templates(self):
        db = self.vault.main.db
        all_templates = db.Templates.select()
        self.ui.comboBox_selector_templates.clear()
        for template in all_templates:
            self.ui.comboBox_selector_templates.addItem(template.name,
                                                        template)

    @db_session
    def add_template(self):
        db = self.vault.main.db
        templates_list = self.ui.listWidget_templates
        vault_item = db.Vault[self.target.id]
        selected_template = self.ui.comboBox_selector_templates.currentData()
        dbObj = db.Templates[selected_template.id]

        vault_item.templates.add(dbObj)
        item = QListWidgetItem(dbObj.name)
        item.dbObj = dbObj
        templates_list.addItem(item)
        self.update_stat_block()




    @db_session
    def delete_vault_item(self):
        vault = self.vault.ui.listWidget_vault
        db = self.vault.main.db
        self.target = db.Vault[self.target.id]
        for row in range(0, vault.count()):
            item = vault.item(row)
            dbObj = db.Vault[item.dbObj.id]
            if dbObj is self.target:
                vault.takeItem(row)
                dbObj.delete()
                self.target = None
                commit()
                break
        self.close()

    @db_session
    def remove_template(self):
        db = self.vault.main.db
        self.target = vault_item = db.Vault[self.target.id]
        template_view = self.ui.listWidget_templates
        for row in range(0, template_view.count()):
            item = template_view.item(row)
            if item.isSelected():
                template_view.takeItem(row)
                template = db.Templates[item.dbObj.id]
                self.target.templates.remove(template)
                commit()
                break
        self.update_stat_block()

    @db_session
    def update_attributes(self, attribute):
        db = self.vault.main.db
        self.target = vault_item = db.Vault[self.target.id]
        attributes = self.target.attributes.split(',')
        match attribute:
            case 'STR':
                attributes[0] = self.ui.spinBox_STR.value()
            case 'DEX':
                attributes[1] = self.ui.spinBox_DEX.value()
            case 'CON':
                attributes[2] = self.ui.spinBox_CON.value()
            case 'WIS':
                attributes[3] = self.ui.spinBox_WIS.value()
            case 'INT':
                attributes[4] = self.ui.spinBox_INT.value()
            case 'CHA':
                attributes[5] = self.ui.spinBox_CHA.value()
        self.target.attributes = ','.join(attributes)
        commit()
        self.update_stat_block()

    @db_session
    def update_target_cr(self):
        db = self.vault.main.db
        self.target = vault_item = db.Vault[self.target.id]
        vault_item.cr = self.ui.spinBox_cr.value()
        self.update_stat_block()

    @db_session
    def update_group_of(self):
        db = self.vault.main.db
        self.target = vault_item = db.Vault[self.target.id]
        vault_item.count = self.ui.spinBox_group_of.value()
        self.update_stat_block()

    @db_session
    def update_type(self):
        db = self.vault.main.db
        self.target = vault_item = db.Vault[self.target.id]
        vault_item.type = self.ui.comboBox_type.currentText()
        self.update_stat_block()

    @db_session
    def update_name(self):
        db = self.vault.main.db
        self.target = vault_item = db.Vault[self.target.id]
        vault_item.name = self.ui.lineEdit_name.text()
        self.update_stat_block()
