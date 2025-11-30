# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import (QDialog, QListWidgetItem, QMessageBox)
from PySide6.QtCore import Qt
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
        self.display_target = None
        self.spinboxLock = False
        self.debug_count = 0
        self.dice_tower = Dice_factory()

        # self.ui.pushButton_roll_stats.clicked.connect(self.roll_stats)
        self.ui.pushButton_back.clicked.connect(self.close)
        self.ui.pushButton_add_templates.clicked.connect(self.add_template)
        self.ui.pushButton_delete_shop.clicked.connect(self.delete_vault_item)
        self.ui.pushButton_remove_templates.clicked.connect(self.remove_template)
        #TODO needs update
        self.ui.pushButton_reset_stat_block.clicked.connect(self.update_stat_block)

        # self.ui.spinBox_cr.valueChanged.connect(self.update_cr)
        # self.ui.spinBox_group_of.valueChanged.connect(self.update_group_of)
        # self.ui.spinBox_STR.valueChanged.connect(lambda x: self.update_stat('STR', x))
        # self.ui.spinBox_DEX.valueChanged.connect(lambda x: self.update_stat('DEX', x))
        # self.ui.spinBox_CON.valueChanged.connect(lambda x: self.update_stat('CON', x))
        # self.ui.spinBox_INT.valueChanged.connect(lambda x: self.update_stat('INT', x))
        # self.ui.spinBox_WIS.valueChanged.connect(lambda x: self.update_stat('WIS', x))
        # self.ui.spinBox_CHA.valueChanged.connect(lambda x: self.update_stat('CHA', x))
        self.ui.lineEdit_name.textEdited.connect(self.update_name)
        # This is fine but I have to block signals anywhere I use this textEdit
        self.ui.textEdit_stat_block.textChanged.connect(self.save_stat_block_Changes)



#     @db_session
#     def update_cr(self):
#         if self.spinboxLock:
#             return
#         db = self.vault.main.db
#         dbObj = db.Vault[self.target.id]
#         dbObj.cr = self.ui.spinBox_cr.value()
#         self.update_stat_block()


#     @db_session
#     def update_group_of(self):
#         if self.spinboxLock:
#             return
#         db = self.vault.main.db
#         dbObj = db.Vault[self.target.id]
#         dbObj.group_of = self.ui.spinBox_group_of.value()
#         self.update_stat_block()


#     @db_session
#     def update_stat(self, stat, value):
#         # Locks updates from happening on loads or just whenever i like.
#         # easier then using the spinbox's blocksignal function since i handle
#         # many spinboxes here.
#         if self.spinboxLock:
#             return
#         db = self.vault.main.db
#         dbObj = db.Vault[self.target.id]
#         match stat:
#             case 'STR':
#                 dbObj.ability_str = int(value)
#             case 'DEX':
#                 dbObj.ability_dex = int(value)
#             case 'CON':
#                 dbObj.ability_con = int(value)
#             case 'WIS':
#                 dbObj.ability_wis = int(value)
#             case 'INT':
#                 dbObj.ability_int = int(value)
#             case 'CHA':
#                 dbObj.ability_cha = int(value)
#         commit()
#         self.update_stat_block()


    @db_session
    def save_stat_block_Changes(self):
        db = self.vault.main.db
        dbObj = db.Vault[self.target.id]
        dbObj.stat_block = self.ui.textEdit_stat_block.toPlainText()
        self.display_target.setToolTip(dbObj.stat_block)


    @db_session
    def load_vault_item(self, display_target_index):
        # init values
        db = self.vault.main.db
        vault = self.vault.ui.listWidget_vault
        self.display_target = vault.itemFromIndex(display_target_index)
        self.target = self.display_target.dbObj
        self.target = db.Vault[self.target.id]

        # Load Name
        self.ui.lineEdit_name.blockSignals(True)
        self.ui.lineEdit_name.setText(self.target.name)
        self.ui.lineEdit_name.blockSignals(False)

        # self.spinboxLock = True
        # self.ui.spinBox_cr.setValue(self.target.cr)
        # self.ui.spinBox_group_of.setValue(self.target.count)
        # self.ui.spinBox_STR.setValue(self.target.ability_str)
        # self.ui.spinBox_DEX.setValue(self.target.ability_dex)
        # self.ui.spinBox_CON.setValue(self.target.ability_con)
        # self.ui.spinBox_WIS.setValue(self.target.ability_wis)
        # self.ui.spinBox_INT.setValue(self.target.ability_int)
        # self.ui.spinBox_CHA.setValue(self.target.ability_cha)
        # self.spinboxLock = False

        self.ui.textEdit_stat_block.blockSignals(True)
        self.ui.textEdit_stat_block.setPlainText(self.target.stat_block)
        self.ui.textEdit_stat_block.blockSignals(False)

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
        self.target = db.Vault()
        commit()
        item = QListWidgetItem('* * *')
        self.ui.lineEdit_name.setText('* * *')
        item.dbObj = self.target
        # Add Items
        self.vault.ui.listWidget_vault.addItem(item)
        self.display_target = item
        self.update_selector_templates()
        self.update_stat_block()
        self.ui.listWidget_templates.clear()
        self.show()


    def get_auto_values(self, text, scores):
        'computes and replaces template variables'
        score_keys = list(scores.keys())
        score_keys.sort(key=lambda x: len(x), reverse=True)
        while True:
            # search template for stats and replace.
            # stat = r'%(str|dex|con|wis|int|cha)'
            stat = '%('
            for name in score_keys:
                search += f'{name}|'
            search += ')'
            m = re.search(stat, text)

            if m:
                which_stat = m.group(1).lower()
                search = f'%{which_stat}'
                # print(r'stuff: ', search, scores, stat, text)
                text = re.sub(search, str(scores[which_stat]),
                              text, count=1)
                # print(r'Replacement: ', text)
                continue

            # Calculate Dice expressions inside %{ } brackets
            m = re.search(r'%{(.*)}', text)
            if m:
                result = self.dice_tower.roll(m.group(1))
                text = re.sub('%{.*}', str(result), text, count=1)
                continue

            #TODO Detect division 2-9?
#             m = re.search(r'%/([2-9])?', text)
#             if m:
#                 if m.group(1):
#                     HP = (cr_info["hp"] // group_of) // int(m.group(1))
#                     HP_view = (f'{HP} '
#                                f'({self.dice_tower.to_dice(HP)})')
#                     text = re.sub('%h[2-9]', str(HP_view), text, count=1)
#                     continue
#                 else:
#                     HP = cr_info["hp"] // group_of
#                     HP_view = (f'{HP} '
#                                f'({self.dice_tower.to_dice(HP)})')
#                     text = re.sub('%h', str(HP_view), text, count=1)
#                     continue

#             #TODO Detect multiplication 2-9?
#             m = re.search(r'%a', text)
#             if m:
#                 attack_bonus = cr_info["atkBonus"]
#                 text = re.sub('%a', str(attack_bonus), text, count=1)
#                 continue
# 
#             # Detect Damage per round division.
#             m = re.search(r'%d([2-9])?', text)
#             if m:
#                 dam_per_round = cr_info["damPerRound"] // group_of
#                 if m.group(1):
#                     # print('found group ', m.group(1) )
#                     adjusted_damage = dam_per_round // int(m.group(1))
#                     damage_view = (f'{adjusted_damage} '
#                                  f'({self.dice_tower.to_dice(adjusted_damage)})')
#                     text = re.sub(r'%d[2-9]', damage_view, text, count=1)
#                     continue
#                 else:
#                     # print('no group found ')
#                     damage_view = (f'{dam_per_round} '
#                                  f'({self.dice_tower.to_dice(dam_per_round)})')
#                     text = re.sub(r'%d', damage_view, text, count=1)
#                     continue

#             # Detect Spell Save DC
#             m = re.search(r'%s', text)
#             if m:
#                 spellSaveDC = cr_info['saveDC']
#                 text = re.sub('%s', str(spellSaveDC), text, count=1)
#                 continue
            break
        return text


    def compile_attr(self, native_attr, stat_mod):
        'combine a defined template score with a stat'
        # print(stat_mod)
        if stat_mod is None:
            # print('none')
            return int(native_attr)
        if '+' not in stat_mod and '-' not in stat_mod:
            # print(f'change to: {stat_mod}')
            return int(stat_mod)
        else:
            # print('doin maths')
            return int(native_attr) + int(stat_mod)


    def load_scores(self, stat_block):
        system_stats = self.vault.main.system_stats
        system_macros = self.vault.main.system_macros
        scores = dict() 
        macros = dict()
        for stat in system_stats:
            full_name = system_stats[stat]["name"]
            scores[stat] = self.compile_attr(
                                    system_stats[stat]['value'],
                                    stat_block['stat'].get(full_name))
        
        for macro in system_macros:
            # print(f"macro: {macro} = {system_macros[macro]}")
            macros[macro] = self.dice_tower.roll(self.get_auto_values(system_macros[macro], scores))

        scores = scores | macros
        # print(f"load scores: {scores}")
        return scores

    def resolve_template_values(self, template):
        pass
        # load all 


    @db_session
    def update_stat_block(self):
        'responsible for creating stat blocks'
        # print("updating stat block")
        db = self.vault.main.db
        env = self.vault.main.templEnv
        template = env.get_template("5e.jinja")
        dbObj = db.Vault[self.target.id]

        sections = ('lore', 'attribute',
                    'item', 'action',
                    'rtable' )


        # stack all templates
        stat_block = self.stack_template_data()

        # add the name in
        stat_block['name'] = self.ui.lineEdit_name.text()

        # Load default stat values
        scores = self.load_scores(stat_block)

        # calculate hp
        dbObj.hp = stat_block['hp'] = scores['hp']


        # read templates and replace stats and marcos
        # then compute them as well.
        stat_block["sections"] = dict()
        for section in sections:
            for key, text in stat_block[section].items():
                if text:
                    stat_block["sections"][section] = dict()
                    stat_block["sections"][section]["text"] = self.get_auto_values(text, scores)
                    # print(stat_block["sections"][section]["text"])
        
        # draw all the data into this over all template
        stat_block_text = template.render(data=stat_block, sc=scores)

        self.ui.textEdit_stat_block.blockSignals(True)
        self.ui.textEdit_stat_block.setPlainText(stat_block_text)
        self.ui.textEdit_stat_block.blockSignals(False)
        # updates the vault item in the database and other pages.
        self.save_stat_block_Changes()



#     @db_session
#     def update_stat_block(self):
#         'responsible for creating stat blocks'
#         print("updating stat block")
#         db = self.vault.main.db
#         head_templ = self.vault.main.system_config['header']['template']
#         sect_templ = self.vault.main.system_config['sections']['template']
#         tail_templ = self.vault.main.system_config['footer']['template']
#         dbObj = db.Vault[self.target.id]
#         dice_tower = Dice_factory()
# 
#         stat_block = self.compile_templates()
#         scores = self.load_scores(stat_block)
# 
#         # calculate hp
#         HP = self.compile_attr(cr_info["hp"] // group_of,
#         #                 stat_block['stat'].get('Hit Points'))
# 
#         dbObj.hp = HP
#         HP_view = f'{HP} ({dice_tower.to_dice(HP)})'
# 
#         # calculate AC
#         AC = self.compile_attr(cr_info["ac"],
#                         stat_block['stat'].get('Armor Class'))
# 
#         # get the name
#         name = self.ui.lineEdit_name.text()
# 
#         mods = ''
#         for key, value in stat_block['stat'].items():
#            mods += f'{key}: {value}\n'
# 
#         # get stat_block template filled
#         stat_block_text = (f'{name}\n'
#                            f'CR: {cr}\n'
#                            f'AC: {AC}\n'
#                            f'HP: {HP_view}\n'
#                            f'{final_scores}\n'
#                            f'{mods}')
# 
#         sections = ('lore', 'attribute',
#                     'item', 'action',
#                     'rtable' )
# 
#         for section in sections:
#             if stat_block[section]:
#                 # print(f"stat_block: {sections[section]}")
#                 stat_block_text += f'\n====[ {section} ]====\n'
#                 for key, text in stat_block[section].items():
#                     # print(f'{key}:{text}:{group_of}:{cr_info}:{scores}:{dice_tower}')
#                     text = self.get_auto_values(text, group_of,
#                                                 cr_info, scores,
#                                                 dice_tower)
#                     stat_block_text += f'\n{text}\n'
#                 stat_block_text += '\n'
# 
#         self.ui.textEdit_stat_block.blockSignals(True)
#         self.ui.textEdit_stat_block.setPlainText(stat_block_text)
#         self.ui.textEdit_stat_block.blockSignals(False)
#         # updates the vault item in the database and other pages.
#         self.save_stat_block_Changes()


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
    def stack_template_data(self):
        # print("entering compile_templates")
        db = self.vault.main.db
        details = {'lore':{},
                   'stat':{},
                   'attribute':{},
                   'item': {},
                   'action': {},
                   'rtable': {} }

        def stack_rtable(details, rtable, deny_list):
            'only works on detail_type="rtable"'
            if rtable.onlyPrint:
                # do nothing but print the table.
                # Does not count items as duplicates.
                # Does not stack items with other stuff.
                items = []
                for rtable_xfer in rtable.roll_table_items:
                    rtable_item = rtable_xfer.table_item
                    if rtable_item.id not in deny_list:
                        deny_list.append(rtable_item.id)
                        items.append((rtable_xfer.match, rtable_item.to_display()))
                items = [f'{x[0]}: {x[1]}' for x in items]
                display = f'==[{rtable.dice_roll}: {rtable.name}]==\n\n' + \
                           '\n\n'.join(sorted(items))
                details['rtable'][rtable.id] = display
            elif rtable.is_random:
                # get a list of the items ignore matching.
                items = [ x for x in rtable.roll_table_items.table_item]
                # Roll the table dice
                times_to_roll = self.dice_tower.roll(rtable.dice_roll)
                # pick from the table this many times.
                for i in range(0, times_to_roll):
                    rolled_dice = self.dice_tower.roll('1d' + \
                                             str(len(items)))
                    item_index = rolled_dice - 1
                    # pick this item from the list without matching.
                    item = items[item_index]
                    if item.id not in deny_list:
                            deny_list.append(item.id)
                            details, deny_list = stack(details,
                                                       item,
                                                       deny_list)
            else:
                # roll the table dice
                result = self.dice_tower.roll(rtable.dice_roll)
                # check all matches
                rolled_dice = self.dice_tower.roll(rtable.dice_roll)
                for rtable_xfer in rtable.roll_table_items:
                    item = rtable_xfer.table_item
                    if rolled_dice in self.read_match(rtable_xfer.match) and item.id not in deny_list:
                        deny_list.append(item.id)
                        details, deny_list = stack(details,
                                                   item,
                                                   deny_list)
            return details, deny_list

        def stack_details(details, template, deny_list):
            match template.detail_type:
                case 'stat':
                    display = template.description
                    details[template.detail_type][template.name] = display
                case 'lore' | 'attribute' | 'item' | 'action':
                    display = template.to_display()
                    details[template.detail_type][template.id] = display
                case 'rtable':
                    details, deny_list = stack_rtable(details, template, deny_list)
                case 'template':
                    details, deny_list = stack(details, template, deny_list)
            return details, deny_list

        def stack(details, template, deny_list=[]):
            'stack should only act on detail_type="templates"'
            # from here we need to go down one level and read members.
            # print(f'detail_type: {template.detail_type}')
            if template.detail_type not in ['template', 'rtable']:
                details, deny_list = stack_details(details, template, deny_list)
            elif template.detail_type == 'rtable':
                details, deny_list = stack_rtable(details, template, deny_list)
            else:
                for sub_template in template.under_me:
                    if sub_template.id not in deny_list:
                        # print(f"ACCESS=>{sub_template.name}")
                        deny_list.append(sub_template.id)
                        details, deny_list = stack(details, sub_template, deny_list)
            return details, deny_list

        vault_item = db.Vault[self.target.id]
        deny_list = []
        # vault item members should ONLY be templates
        for template in vault_item.templates:
            if template.id not in deny_list:
                deny_list.append(template.id)
                details, deny_list = stack(details, template, deny_list)
        # print(f'OUTPUT:{details}\n[{deny_list}]')
        return details


#     @db_session
#     def roll_stats(self):
#         db = self.vault.main.db
#         dbObj = db.Vault[self.target.id]
#         dice_tower = Dice_factory()
#         # roll 4d6 but keep the top 3
#         stats = tuple([ dice_tower.roll('4d6t3') for r in range(6)])
#         self.ui.spinBox_STR.setValue(stats[0])
#         dbObj.ability_str = stats[0]
#         self.ui.spinBox_DEX.setValue(stats[1])
#         dbObj.ability_dex = stats[1]
#         self.ui.spinBox_CON.setValue(stats[2])
#         dbObj.ability_con = stats[2]
#         self.ui.spinBox_WIS.setValue(stats[3])
#         dbObj.ability_wis = stats[3]
#         self.ui.spinBox_INT.setValue(stats[4])
#         dbObj.ability_int = stats[4]
#         self.ui.spinBox_CHA.setValue(stats[5])
#         dbObj.ability_cha = stats[5]
#         commit()
#         self.update_stat_block()

    @db_session
    def update_selector_templates(self):
        db = self.vault.main.db
        all_templates = db.Templates.select(detail_type='template')
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

        if not templates_list.findItems(dbObj.name, Qt.MatchStartsWith):
            # print("add_template func")
            vault_item.templates.add(dbObj)
            item = QListWidgetItem(dbObj.name)
            item.dbObj = dbObj
            templates_list.addItem(item)
            self.update_stat_block()
        else:
            msgBox = QMessageBox()
            msgBox.setText("No duplicate templates allowed at this time")
            msgBox.exec()


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


#     @db_session
#     def update_target_cr(self):
#         db = self.vault.main.db
#         self.target = vault_item = db.Vault[self.target.id]
#         vault_item.cr = self.ui.spinBox_cr.value()
#         self.update_stat_block()

#     @db_session
#     def update_group_of(self):
#         db = self.vault.main.db
#         self.target = vault_item = db.Vault[self.target.id]
#         vault_item.count = self.ui.spinBox_group_of.value()
#         self.update_stat_block()

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
        # self.update_stat_block()
