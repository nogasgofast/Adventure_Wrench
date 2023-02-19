# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import (QDialog, QListWidgetItem)
from ui.TheShop_Dialog import Ui_TheShop
from pony.orm import db_session, commit
from lib.dice import Dice_factory
from lib.encounter import Preset_data
import re


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
        self.ui.pushButton_reset_stat_block.clicked.connect(self.update_stat_block)

        self.ui.spinBox_cr.valueChanged.connect(self.update_cr)
        self.ui.spinBox_group_of.valueChanged.connect(self.update_group_of)
        self.ui.spinBox_STR.valueChanged.connect(lambda x: self.update_stat(0, x))
        self.ui.spinBox_DEX.valueChanged.connect(lambda x: self.update_stat(1, x))
        self.ui.spinBox_CON.valueChanged.connect(lambda x: self.update_stat(2, x))
        self.ui.spinBox_INT.valueChanged.connect(lambda x: self.update_stat(3, x))
        self.ui.spinBox_WIS.valueChanged.connect(lambda x: self.update_stat(4, x))
        self.ui.spinBox_CHA.valueChanged.connect(lambda x: self.update_stat(5, x))

        self.ui.lineEdit_name.textEdited.connect(self.update_name)

        self.ui.textEdit_stat_block.textChanged.connect(self.save_stat_block_Changes)


    @db_session
    def update_cr(self):
        db = self.vault.main.db
        dbObj = db.Vault[self.target.id]
        dbObj.cr = self.ui.spinBox_cr.value()
        self.update_stat_block()


    @db_session
    def update_group_of(self):
        db = self.vault.main.db
        dbObj = db.Vault[self.target.id]
        dbObj.group_of = self.ui.spinBox_group_of.value()
        self.update_stat_block()


    @db_session
    def update_stat(self, stat, val_as_unicode):
        db = self.vault.main.db
        dbObj = db.Vault[self.target.id]
        scores = dbObj.attributes.split(',')
        scores[stat] = str(val_as_unicode)
        dbObj.attributes = ','.join(scores)
        self.update_stat_block()


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
        self.update_selector_templates()
        self.update_stat_block()
        self.show()


    @db_session
    def update_stat_block(self):
        'responsible for creating stat blocks'
        db = self.vault.main.db
        dbObj = db.Vault[self.target.id]
        stat_block = self.compile_templates()
        cr = self.ui.spinBox_cr.value()
        group_of = self.ui.spinBox_group_of.value()
        cr_info = Preset_data().get(cr)
        dice_tower = Dice_factory()
        HP = cr_info["hp"] // group_of
        dbObj.hp = HP
        HP_view = f'{HP} ({dice_tower.to_dice(HP)})'

        # pull in The Shop's stats to compile with these
        def compile_attr(attribute, stat_mod):
            'combines ui ability scores with templates'
            if stat_mod is None:
                return int(attribute)
            if '+' not in stat_mod and '-' not in stat_mod:
                return int(stat_mod)
            else:
                return int(attribute) + int(stat_mod)

        def replace_auto_values(text):
            m = re.search('%h([2-9])', text)
            if m:
                HP = (cr_info["hp"] // group_of) / m.group(1)
                HP_view = (f'{HP} '
                           f'({dice_tower.to_dice(HP)})')
                text = re.sub('%h[2-9]', str(HP_view), text)
            else:
                HP = (cr_info["hp"] // group_of)
                HP_view = (f'{HP} '
                           f'({dice_tower.to_dice(HP)})')
                text = re.sub('%h', str(HP_view), text)
            attack_bonus = cr_info["atkBonus"]
            text = re.sub('%a', str(attack_bonus), text)

            damage = cr_info["damPerRound"] // group_of
            damage_view = (f'{damage} '
                           f'({dice_tower.to_dice(damage)})')
            text = re.sub('%d', damage_view, text)

            m = re.search('%e([2-9])', text)
            if m:
                elementalDamage = damage // m.group(1)
                elem_view = (f'{elementalDamage} '
                             f'({dice_tower.to_dice(elementalDamage)})')
                text = re.sub('%e[2-9]', elem_view, text)
            else:
                elementalDamage = damage // 2
                elem_view = (f'{elementalDamage} '
                             f'({dice_tower.to_dice(elementalDamage)})')
                text = re.sub('%e', elem_view, text)
            spellSaveDC = cr_info['saveDC']
            text = re.sub('%s', str(spellSaveDC), text)
            return text

        scores = dbObj.attributes.split(',')
        names = ('Strength', 'Dexterity',
                 'Constitution', 'Wisdom',
                 'Intelligence', 'Charisma')
        for row in range(0, 6):
            scores[row] = compile_attr(scores[row],
                                       stat_block['Stats'].get(names[row]))
        stat_bar_heading = ('STR', 'DEX',
                            'CON', 'WIS',
                            'INT', 'CHA')
        final_scores = ''
        for row in range(0, 6):
            final_scores += f'{stat_bar_heading[row]}: {scores[row]:02}    '
        name = self.ui.lineEdit_name.text()
        plainText = (f'{name}\n'
                     f'CR: {cr}\n'
                     f'HP: {HP_view}\n'
                     f'{final_scores}\n')
        sections = ('Lore', 'Attributes',
                    'Items', 'Actions',
                    'Roll tables' )
        for section in range(0, len(sections)):
            if stat_block[sections[section]]:
                plainText += f'\n====[ {sections[section]} ]===\n'
                for key, text in stat_block[sections[section]].items():
                    text = replace_auto_values(text)
                    plainText += f'\n{text}\n'
                plainText += '\n'
        self.ui.textEdit_stat_block.setPlainText(plainText)
        # and update vault tool-tip as well.
        vault_list = self.vault.ui.listWidget_vault
        for row in range(0, vault_list.count()):
            item = vault_list.item(row)
            if item.dbObj == self.target:
                item.setToolTip(plainText)

    def read_match(self, matchList):
        matchList = matchList.split(',')
        removeRows = []
        for match in matchList:
            if '-' in str(match):
                removeRows.append(matchList.index(match))
                low, high = match.split('-')
                low = int(low.strip())
                high = int(high.strip())
                matchRange = [ x for x in range(low, high + 1)]
                matchList.extend(matchRange)
        for r in removeRows:
            matchList.pop(r)
        matchList = [ int(x) for x in matchList ]
        return sorted(matchList)

    @db_session
    def compile_templates(self):
        db = self.vault.main.db
        details = {'Lore':{},
                   'Stats':{},
                   'Attributes':{},
                   'Items': {},
                   'Actions': {},
                   'Roll tables': {} }

        def stack_rtable(details, rtable):
            if rtable.immutable:
                details['Roll tables'][rtable.name] = rtable.to_strings()
            else:
                dice_tower = Dice_factory()
                result = dice_tower.roll(rtable.diceRoll)
                for item in rtable.items:
                    if result in self.read_match(item.match):
                        if item.lore:
                            details['Lore'][item.lore.name] = item.lore.to_strings()
                        if item.attribute:
                            details['Attributes'][item.attribute.name] = item.attribute.to_strings()
                        if item.stat:
                            details['Stats'][item.stat.name] = item.stat.description
                        if item.item:
                            details['Items'][item.item.name] = item.item.to_strings()
                        if item.action:
                            details['Actions'][item.action.name] = item.action.to_strings()
                        if item.template:
                            details = stack(details, item.template)
                        if item.rtable:
                            stack_rtable(details, item.rtable)
            return details

        def stack_details(details, template):
            for item in template.lore:
                details['Lore'][item.name] = item.to_strings()
            for item in template.stats:
                details['Stats'][item.name] = item.description
            for item in template.attributes:
                details['Attributes'][item.name] = item.to_strings()
            for item in template.items:
                details['Items'][item.name] = item.to_strings()
            for item in template.actions:
                details['Actions'][item.name] = item.to_strings()
            for table in template.rtables:
                stack_rtable(details, table)
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
        dice_tower = Dice_factory()
        # roll 4d6 but keep the top 3
        stats = [ dice_tower.roll('4d6t3') for r in range(6)]
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
            if not template.is_folder:
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
        self.vault.update_vault_item(self.target)
        self.update_stat_block()
