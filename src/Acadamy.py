
from pony.orm import db_session, commit, desc
from PySide6.QtWidgets import (QDialog, QListWidgetItem,
                               QTreeWidgetItem, QMessageBox)
from PySide6.QtCore import Qt, QSignalBlocker
from ui.Acadamy_Dialog import Ui_acadamy_dialog


class AcadamyDialog(QDialog):
    # TODO add button focus changes to form page changes
    # Hitting enter should always do the right thing.
    # I may have to look at this for all other windows and pages.
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui_vault = parent
        self.ui = Ui_acadamy_dialog()
        self.ui.setupUi(self)
        self.ui.verticalStackedWidget_forms.setCurrentIndex(0)

        self.ui.pushButton_new_template.clicked.connect(self.new_template)
        self.ui.pushButton_add_detail.clicked.connect(self.add_detail)
        self.ui.pushButton_add_item_roll_table.clicked.connect(self.add_item_roll_table)
        self.ui.pushButton_stack_template.clicked.connect(self.stack_template)
        self.ui.pushButton_back.clicked.connect(self.close)
        # deletion buttons
        self.ui.pushButton_delete_item_roll_table.clicked.connect(self.delete_item_roll_table)
        self.ui.pushButton_delete_lore.clicked.connect(self.delete_detail)
        self.ui.pushButton_delete_attribute.clicked.connect(self.delete_detail)
        self.ui.pushButton_delete_stats.clicked.connect(self.delete_detail)
        self.ui.pushButton_delete_item.clicked.connect(self.delete_detail)
        self.ui.pushButton_delete_template.clicked.connect(self.delete_template)
        self.ui.pushButton_delete_action.clicked.connect(self.delete_detail)
        self.ui.pushButton_delete_roll_table.clicked.connect(self.delete_detail)
        # Add another buttons
        self.ui.pushButton_add_another_template.clicked.connect(self.new_template)
        self.ui.pushButton_add_another_lore.clicked.connect(lambda: self.add_detail('Lore'))
        self.ui.pushButton_add_another_stats.clicked.connect(lambda: self.add_detail('Stat Modification'))
        self.ui.pushButton_add_another_attribute.clicked.connect(lambda: self.add_detail('Attributes'))
        self.ui.pushButton_add_another_item.clicked.connect(lambda: self.add_detail('Items'))
        self.ui.pushButton_add_another_action.clicked.connect(lambda: self.add_detail('Actions'))
        self.ui.pushButton_add_another_roll_table.clicked.connect(lambda: self.add_detail('Roll Table'))
        # Next buttons
        self.ui.pushButton_next_lore.clicked.connect(self.next_buttons)
        self.ui.pushButton_next_stats.clicked.connect(self.next_buttons)
        self.ui.pushButton_next_attribute.clicked.connect(self.next_buttons)
        self.ui.pushButton_next_item.clicked.connect(self.next_buttons)
        self.ui.pushButton_next_action.clicked.connect(self.next_buttons)
        self.ui.pushButton_next_roll_table.clicked.connect(self.next_buttons)
        # template to random tempalte converter
        self.ui.pushButton_randomize_template.clicked.connect(self.template_to_random)
        # This is how I auto-update a bunch of things.
        self.ui.treeWidget_all_templates.itemClicked.connect(self.select_template)

        self.ui.listWidget_table_roll_table.clicked.connect(self.rt_item_select)

        self.ui.lineEdit_template_name.textEdited.connect(self.update_template_name)
        self.ui.lineEdit_name_lore.textEdited.connect(self.update_template_name)
        self.ui.lineEdit_name_attribute.textEdited.connect(self.update_template_name)
        self.ui.lineEdit_name_item.textEdited.connect(self.update_template_name)
        self.ui.lineEdit_name_action.textEdited.connect(self.update_template_name)
        self.ui.lineEdit_name_roll_table.textEdited.connect(self.update_template_name)

        self.ui.lineEdit_content_stats.textEdited.connect(self.update_content_stats)
        self.ui.lineEdit_content_attribute.textEdited.connect(self.update_content_attribute)

        self.ui.lineEdit_weight_item.textEdited.connect(self.update_weight_item)
        self.ui.lineEdit_cost_action.textEdited.connect(self.update_cost_action)
        self.ui.lineEdit_limitations_action.textEdited.connect(self.update_limitations_action)
        self.ui.lineEdit_dice_roll_table.textEdited.connect(self.update_dice_roll_table)

        self.ui.spinBox_quantity_item.valueChanged.connect(self.update_quantity_item)

        self.ui.textEdit_content_lore.textChanged.connect(self.update_content_lore)
        self.ui.textEdit_description_item.textChanged.connect(self.update_description_item)
        self.ui.textEdit_result_action.textChanged.connect(self.update_result_action)

        self.ui.comboBox_name_stats.currentIndexChanged.connect(self.update_name_stats)

        self.ui.checkBox_israndom_roll_table.stateChanged.connect(self.update_israndom_roll_table)
        self.ui.checkBox_interpret_roll_table.stateChanged.connect(self.update_immutable_roll_table)
        self.ui.checkBox_is_folder_template.stateChanged.connect(self.update_is_folder)

        # This mapping lets me diss-connect combobox positions from pageIndex.
        # and instead use page names directly.
        self.pageIndex = {'splash': 0,
                          'template': 1,
                          'Lore': 2,
                          'Stat Modification': 3,
                          'Attributes': 4,
                          'Items': 5,
                          'Actions': 6,
                          'Roll Table': 7}
        self.load_acadamy()


    @db_session
    def create_fingerprint(self):
        'Not used, maybe later'
        db = self.ui_vault.main.db
        templates = self.ui.treeWidget_all_templates
        template = templaste.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        fingerprint = ''
        section_filled = False
        # create stat area
        for i in dbObj.under_me.select(detail_type = 'stat').count():
            fingerprint += 's'
            section_filled = True
        if section_filled:
            fingerprint += ','
            section_filled = False
        # create attribute area
        for i in dbObj.under_me.select(detail_type = 'attribute').count():
            fingerprint += 'a'
            section_filled = True
        if section_filled:
            fingerprint += ','
            section_filled = False
        for i in dbObj.under_me.select(detail_type = 'action').count():
            fingerprint += 'w'
            section_filled = True
        if section_filled:
            fingerprint += ','
            section_filled = False
        for i in dbObj.under_me.select(detail_type = 'lore').count():
            fingerprint += 'l'
            section_filled = True
        if section_filled:
            fingerprint += ','
            section_filled = False
        for i in dbObj.under_me.select(detail_type = 'item').count():
            fingerprint += 'i'
            section_filled = True
        if section_filled:
            fingerprint += ','
            section_filled = False
        for i in dbObj.under_me.select(detail_type = 'rtable').count():
            fingerprint += 'r'
            section_filled = True
        if section_filled:
            fingerprint += ','
            section_filled = False
        for i in dbObj.under_me.select(detail_type = 'template').count():
            fingerprint += 't'
            section_filled = True
        if section_filled:
            fingerprint += ','
            section_filled = False
        return f'[{fingerprint}]'


    @db_session
    def rt_item_select(self):
        db = self.ui_vault.main.db
        roll_table_view = self.ui.listWidget_table_roll_table
        match_field = self.ui.lineEdit_item_match_roll_table
        option_field = self.ui.comboBox_options_roll_table

        for row in range(0, roll_table_view.count()):
            item = roll_table_view.item(row)
            if item.isSelected():
                dbObj = db.Rtable_items[item.dbObj.id]
                match_field.setText(dbObj.match)
                name = self.construct_detail_name(dbObj.table_item)
                index = option_field.findText(name)
                option_field.setCurrentIndex(index)


    @db_session
    def template_to_random(self):
        'converts any template to randomized template'
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        template = all_templates.currentItem()
        oldTemplate = db.Templates[template.dbObj.id]
        if oldTemplate.is_folder:
            return
        forms = self.ui.verticalStackedWidget_forms

        # create a new template with this templates name
        new_template = db.Templates(name=oldTemplate.name, detail_type='template')
        commit()

        # set this templates is_folder property
        oldTemplate.is_folder = True
        commit()
        # Update oldTemplate name in ui.
        self.update_template_name(oldTemplate.name)

        # create rollTable
        new_roll_table = new_template.under_me.create(detail_type='rtable',
                                                      name=oldTemplate.name)
        commit()
        # import each high level item into a roll table. Count them.
        count = 0
        for thing in oldTemplate.under_me:
            count += 1
            rt_item = new_roll_table.roll_table_items.create(match=str(count),
                                                             table_item=thing)
            commit()
            rt_item.rtable = new_roll_table

        # set the number of sites for the dice
        roll = '1d' + str(count)
        new_roll_table.dice_roll = roll
        # create a new list item for a template
        new_template_view = QTreeWidgetItem(all_templates)
        new_template_view.dbObj = new_template
        new_template_view.setText(0, new_template.name)
        # create a child under this template.
        child_view = QTreeWidgetItem(new_template_view)
        child_view.dbObj = new_roll_table
        child_view.setText(0, self.construct_detail_name(new_roll_table))
        # select the child for editing and viewing
        all_templates.setCurrentItem(child_view)
        all_templates.sortItems(0, Qt.AscendingOrder)
        # change side panel to display child
        self.select_template(child_view, 0)



    def next_buttons(self):
        forms = self.ui.verticalStackedWidget_forms
        item = self.ui.treeWidget_all_templates.currentItem()
        parent = item.parent()
        self.ui.treeWidget_all_templates.setCurrentItem(parent)
        forms.setCurrentIndex(self.pageIndex['template'])


    @db_session
    def update_is_folder(self):
        db = self.ui_vault.main.db
        templates = self.ui.treeWidget_all_templates
        template = templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.is_folder = self.ui.checkBox_is_folder_template.isChecked()
        if dbObj.is_folder:
            template.setText(0, f"Folder: {dbObj.name}")
        else:
            template.setText(0, f"{dbObj.name}")


    @db_session
    def stack_template(self):
        db = self.ui_vault.main.db
        template_selecter = self.ui.comboBox_stack_template
        all_templates = self.ui.treeWidget_all_templates
        template_view = all_templates.currentItem()

        template = db.Templates[template_view.dbObj.id]

        # pull child data
        copy_target = template_selecter.currentData()
        copy_target = db.Templates[copy_target.id]

        # TODO: prevent duplicates of any template appearing as a
        # ancester or parent of the base template I am staking ontop of.
        blocklist=list()
        # deeply copy template to stack
        if not copy_target.id in blocklist:
            copied_obj = self.deep_template_copy(copy_target, blocklist)
        else:
            return None
        template.under_me.add(copied_obj)
        commit()

        # create child list item (it's a template so no special naming)
        child_view = QTreeWidgetItem(template_view)
        child_view.setText(0, copied_obj.name)
        child_view.dbObj = copied_obj

        # copy objexts to treewidget
        def add_level(parent):
            for dbObj in parent.dbObj.under_me.select():
                item = QTreeWidgetItem(parent)
                item.dbObj = dbObj
                item.setText(0, self.construct_detail_name(dbObj))
                if len(dbObj.under_me) > 0:
                    add_level(item)
        add_level(child_view)


    @db_session
    def deep_template_copy(self, target, blocklist):
        db = self.ui_vault.main.db

        def copy_layer(target, destination, blocklist):
            for template in target.under_me:
                if not template.id in blocklist:
                    blocklist.append(template.id)
                    tcopy = template.to_dict(exclude=[
                                        'id',
                                        'vault',
                                        'over_me',
                                        'under_me',
                                        'rtable_over_me',
                                        'roll_table_items'])
                    child_copy = destination.under_me.create(**tcopy)
                    commit()
                    copy_layer(template, child_copy, blocklist)
            for rtItem in target.roll_table_items:
                if not rtItem.table_item.id in blocklist:
                    blocklist.append(rtItem.table_item.id)
                    rtiCopy = destination.roll_table_items.create(
                                                match=rtItem.match)
                    rtTmplDict = rtItem.table_item.to_dict(exclude=[
                                                        'id',
                                                        'vault',
                                                        'over_me',
                                                        'under_me',
                                                        'rtable_over_me',
                                                        'roll_table_items'])
                    rtTmplCopy = db.Templates(**rtTmplDict)
                    commit()
                    rtiCopy.table_item = rtTmplCopy
                    commit()
                    copy_layer(rtItem.table_item, rtTmplCopy, blocklist)

        target = db.Templates[target.id]
        copy_tgt_dict = target.to_dict(exclude=['id',
                                                'vault',
                                                'over_me',
                                                'under_me',
                                                'rtable_over_me',
                                                'roll_table_items'])
        top = db.Templates(**copy_tgt_dict)
        commit()
        copy_layer(target, top, blocklist)
        return top


    @db_session
    def update_israndom_roll_table(self):
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        template = all_templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.is_random = self.ui.checkBox_israndom_roll_table.isChecked()


    @db_session
    def update_immutable_roll_table(self):
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        template = all_templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.onlyPrint = self.ui.checkBox_interpret_roll_table.isChecked()


    @db_session
    def update_dice_roll_table(self):
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        template = all_templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.dice_roll = self.ui.lineEdit_dice_roll_table.text()


    @db_session
    def add_item_roll_table(self):
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        template = all_templates.currentItem()
        rollTable = db.Templates[template.dbObj.id]
        match  = self.ui.lineEdit_item_match_roll_table.text()
        child = self.ui.comboBox_options_roll_table.currentData()
        child = db.Templates[child.id]
        rtItem = rollTable.roll_table_items.create(match=match,
                                                   table_item=child)
        commit()
        item = QListWidgetItem(self.construct_roll_table_name(rtItem))
        item.dbObj = rtItem
        self.ui.listWidget_table_roll_table.addItem(item)

    @db_session
    def delete_item_roll_table(self):
        db = self.ui_vault.main.db
        rollTable = self.ui.listWidget_table_roll_table
        # select one
        for row in range(0, rollTable.count()):
            if rollTable.item(row).isSelected():
                table_entry = rollTable.takeItem(row)
                break
        dbObj = db.Rtable_items[table_entry.dbObj.id]
        dbObj.delete()
        commit()


    @db_session
    def update_cost_action(self):
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        template = all_templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.cost = self.ui.lineEdit_cost_action.text()


    @db_session
    def update_limitations_action(self):
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        template = all_templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.limitations = self.ui.lineEdit_limitations_action.text()


    @db_session
    def update_result_action(self):
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        template = all_templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.result = self.ui.textEdit_result_action.toPlainText()


    @db_session
    def update_weight_item(self):
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        template = all_templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.weight = self.ui.lineEdit_weight_item.text()


    @db_session
    def update_quantity_item(self):
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        template = all_templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.quantity = self.ui.spinBox_quantity_item.value()


    @db_session
    def update_description_item(self):
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        template = all_templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.description = self.ui.textEdit_description_item.toPlainText()


    @db_session
    def update_content_attribute(self):
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        template = all_templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.description = self.ui.lineEdit_content_attribute.text()


    @db_session
    def update_content_stats(self):
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        template = all_templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.description = self.ui.lineEdit_content_stats.text()


    @db_session
    def delete_template(self):
        db = self.ui_vault.main.db
        forms = self.ui.verticalStackedWidget_forms
        all_templates = self.ui.treeWidget_all_templates
        template_view = all_templates.currentItem()
        parent_view = template_view.parent()
        dbObj = db.Templates[template_view.dbObj.id]
        # delete child stuff that's not templates contained here.
        def remove_level(target):
            if len(target.under_me) > 0:
                for item in target.under_me:
                    remove_level(item)
            if len(target.roll_table_items) > 0:
                for rtable_item in target.roll_table_items:
                    rtable_item.delete()
                commit()
            target.delete()
        remove_level(dbObj)

        if parent_view:
            parent_view.removeChild(template_view)
        else:
            index = all_templates.indexOfTopLevelItem(template_view)
            all_templates.takeTopLevelItem(index)
        current = all_templates.currentItem()
        if current:
            self.select_template(current, 0)
        else:
            forms.setCurrentIndex(self.pageIndex['splash'])


    @db_session
    def delete_detail(self):
        'deletes any detail in detail_view'
        db = self.ui_vault.main.db
        forms = self.ui.verticalStackedWidget_forms
        templates = self.ui.treeWidget_all_templates
        template = templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.delete()
        commit()
        parent = template.parent()
        parent.removeChild(template)
        templates.setCurrentItem(parent)
        # pre-emptivly changed to the templates page in case we can't select
        # anything else.
        forms.setCurrentIndex(self.pageIndex['template'])


    @db_session
    def update_content_lore(self):
        db = self.ui_vault.main.db
        templates = self.ui.treeWidget_all_templates
        template = templates.currentItem()
        dbObj = db.Templates[template.dbObj.id]
        dbObj.description = self.ui.textEdit_content_lore.toPlainText()


    @db_session
    def select_template(self, itemClicked, column):
        'sets self.detail_target and changes the form page'
        db = self.ui_vault.main.db
        templates = self.ui.treeWidget_all_templates
        forms = self.ui.verticalStackedWidget_forms

        item = db.Templates[itemClicked.dbObj.id]
        self.init_page(itemClicked.dbObj.id)
        match item.detail_type:
            case 'lore':
                forms.setCurrentIndex(self.pageIndex['Lore'])
            case 'stat':
                forms.setCurrentIndex(self.pageIndex['Stat Modification'])
            case 'attribute':
                forms.setCurrentIndex(self.pageIndex['Attributes'])
            case 'action':
                forms.setCurrentIndex(self.pageIndex['Actions'])
            case 'item':
                forms.setCurrentIndex(self.pageIndex['Items'])
            case 'rtable':
                forms.setCurrentIndex(self.pageIndex['Roll Table'])
            case 'template':
                forms.setCurrentIndex(self.pageIndex['template'])


    @db_session
    def load_acadamy(self):
        'initialize templates view'
        db = self.ui_vault.main.db
        templates_view = self.ui.treeWidget_all_templates
        templates_view.clear()
        def add_level(parent):
            for dbObj in parent.dbObj.under_me.select():
                item = QTreeWidgetItem(parent)
                item.dbObj = dbObj
                if dbObj.is_folder:
                    item.setText(0, f"Folder: {dbObj.name}")
                else:
                    item.setText(0, self.construct_detail_name(dbObj))
                if len(dbObj.under_me) > 0:
                    add_level(item)
        # Build the tree
        for dbObj in db.Templates.select(detail_type='template'):
            if len(dbObj.over_me) == 0:
                item = QTreeWidgetItem(templates_view)
                item.dbObj = dbObj
                if dbObj.is_folder:
                    item.setText(0, f"Folder: {dbObj.name}")
                else:
                    item.setText(0, dbObj.name)
                if len(dbObj.under_me) > 0:
                    add_level(item)
        templates_view.sortItems(0, Qt.AscendingOrder)


    @db_session
    def update_template_name(self, newText):
        'pretty self explanitory, it is for a text field update'
        db = self.ui_vault.main.db
        currentItem = self.ui.treeWidget_all_templates.currentItem()
        # Get Name
        name = newText
        # update database
        dbObj = db.Templates[currentItem.dbObj.id]
        dbObj.name = name
        commit()
        # update current item
        if dbObj.is_folder:
            currentItem.setText(0, f"Folder: {dbObj.name}")
        else:
            currentItem.setText(0, dbObj.name)

    @db_session
    def update_name_stats(self, newComboIndex):
        newName = self.ui.comboBox_name_stats.currentText()
        self.update_template_name(newName)


    @db_session
    def add_detail(self, selection=None):
        'add a template component to the selected template'
        print(f"function input: {selection}")
        if not selection:
            selection = self.ui.comboBox_type_templates_page.currentText()
        print(f"selection {selection}")
        db = self.ui_vault.main.db
        forms = self.ui.verticalStackedWidget_forms
        templates = self.ui.treeWidget_all_templates
        template = templates.currentItem()
        selected_item = db.Templates[template.dbObj.id]
        if selected_item.detail_type == 'template':
            parent = template
        else:
            parent = template.parent()
        parent_item = db.Templates[parent.dbObj.id]
        match selection:
            case 'Lore':
                dbObj = parent_item.under_me.create(detail_type='lore')
            case 'Stat Modification':
                dbObj = parent_item.under_me.create(detail_type='stat')
            case 'Attributes':
                dbObj = parent_item.under_me.create(detail_type='attribute')
            case 'Items':
                dbObj = parent_item.under_me.create(detail_type='item')
            case 'Actions':
                dbObj = parent_item.under_me.create(detail_type='action')
            case 'Roll Table':
                dbObj = parent_item.under_me.create(detail_type='rtable')
        commit()

        item = QTreeWidgetItem(parent)
        item.dbObj = dbObj
        # ititialize stuff
        templates.setCurrentItem(item)
        templates.sortItems(0, Qt.AscendingOrder)
        self.select_template(item, 0)


    @db_session
    def construct_detail_name(self, dbObj):
        # print(f"contruct_detail_name {dbObj.name}")
        db = self.ui_vault.main.db
        name = ''
        match dbObj.detail_type:
            case 'lore':
                dbObj = db.Templates[dbObj.id]
                name = f'Lore: {dbObj.name}'
            case 'stat':
                dbObj = db.Templates[dbObj.id]
                name = f'Ability Score: {dbObj.name} {dbObj.description}'
            case 'attribute':
                dbObj = db.Templates[dbObj.id]
                if dbObj.description:
                    name = f'Attribute: {dbObj.name}: {dbObj.description}'
                else:
                    name = f'Attribute: {dbObj.name}'
            case 'item':
                dbObj = db.Templates[dbObj.id]
                name = f'Item: {dbObj.name} No.{dbObj.quantity} weight: {dbObj.weight} '
            case 'action':
                dbObj = db.Templates[dbObj.id]
                name = f'Action: {dbObj.name}'
            case 'rtable':
                dbObj = db.Templates[dbObj.id]
                name = f'Roll Table: {dbObj.name} {dbObj.dice_roll}'
            case 'template':
                dbObj = db.Templates[dbObj.id]
                if dbObj.is_folder:
                    name = f'Folder: {dbObj.name}'
                else:
                    name = f'Template: {dbObj.name}'
        return name


    @db_session
    def new_template(self, x=False, template=None):
        'creates template and updates ui'
        db = self.ui_vault.main.db
        all_templates = self.ui.treeWidget_all_templates
        if template is None:
            dbObj = db.Templates(name='*new template*',
                                 detail_type='template')
            commit()
        else:
            dbObj = db.Templates[template.id]
        item = QTreeWidgetItem(all_templates)
        item.dbObj = dbObj
        if template is None:
            item.setText(0, "*new template*")
        else:
            item.setText(0,template.name)

        all_templates.setCurrentItem(item)
        all_templates.sortItems(0, Qt.AscendingOrder)
        self.select_template(item, 0)


    @db_session
    def construct_roll_table_name(self, rtItem):
        'private method for name construction'
        db = self.ui_vault.main.db
        rtItem = db.Rtable_items[rtItem.id]
        item_child = rtItem.table_item
        child_name = self.construct_detail_name(item_child)
        return f'{rtItem.match}: {child_name}'


    @db_session
    def init_page(self, dbObj):
        'all your setup needs for every panel in this applet'
        db = self.ui_vault.main.db
        dbObj = db.Templates[dbObj]
        match dbObj.detail_type:
            case 'lore':
                name = QSignalBlocker(self.ui.lineEdit_name_lore)
                self.ui.lineEdit_name_lore.setText(dbObj.name)
                content = QSignalBlocker(self.ui.textEdit_content_lore)
                self.ui.textEdit_content_lore.setPlainText(dbObj.description)
            case 'stat':
                index = self.ui.comboBox_name_stats.findText(dbObj.name)
                name = QSignalBlocker(self.ui.comboBox_name_stats)
                self.ui.comboBox_name_stats.setCurrentIndex(index)
                content = QSignalBlocker(self.ui.lineEdit_content_stats)
                self.ui.lineEdit_content_stats.setText(dbObj.description)
            case 'attribute':
                name = QSignalBlocker(self.ui.lineEdit_name_attribute)
                self.ui.lineEdit_name_attribute.setText(dbObj.name)
                content = QSignalBlocker(self.ui.lineEdit_content_attribute)
                self.ui.lineEdit_content_attribute.setText(dbObj.description)
            case 'action':
                name = QSignalBlocker(self.ui.lineEdit_name_action)
                self.ui.lineEdit_name_action.setText(dbObj.name)
                cost = QSignalBlocker(self.ui.lineEdit_cost_action)
                self.ui.lineEdit_cost_action.setText(dbObj.cost)
                limitations = QSignalBlocker(self.ui.lineEdit_limitations_action)
                self.ui.lineEdit_limitations_action.setText(dbObj.limitations)
                result = QSignalBlocker(self.ui.textEdit_result_action)
                self.ui.textEdit_result_action.setPlainText(dbObj.result)
            case 'item':
                name = QSignalBlocker(self.ui.lineEdit_name_item)
                self.ui.lineEdit_name_item.setText(dbObj.name)
                weight = QSignalBlocker(self.ui.lineEdit_weight_item)
                self.ui.lineEdit_weight_item.setText(str(dbObj.weight))
                if dbObj.quantity:
                    quantity = QSignalBlocker(self.ui.spinBox_quantity_item)
                    self.ui.spinBox_quantity_item.setValue(dbObj.quantity)
                else:
                    quantity = QSignalBlocker(self.ui.spinBox_quantity_item)
                    self.ui.spinBox_quantity_item.setValue(1)
                description = QSignalBlocker(self.ui.textEdit_description_item)
                self.ui.textEdit_description_item.setPlainText(dbObj.description)
            case 'rtable':
                table = []
                for i in dbObj.roll_table_items:
                    if i.table_item:
                        newItem = QListWidgetItem(self.construct_roll_table_name(i))
                        newItem.dbObj = i
                        table.append(newItem)
                    else:
                        i.delete()
                cBoxItems = [ x for x in db.Templates.select()]
                name = QSignalBlocker(self.ui.lineEdit_name_roll_table)
                self.ui.lineEdit_name_roll_table.setText(dbObj.name)
                israndom = QSignalBlocker(self.ui.checkBox_israndom_roll_table)
                self.ui.checkBox_israndom_roll_table.setChecked(dbObj.is_random)
                interpret = QSignalBlocker(self.ui.checkBox_interpret_roll_table)
                self.ui.checkBox_interpret_roll_table.setChecked(dbObj.onlyPrint)
                dice_roll = QSignalBlocker(self.ui.lineEdit_dice_roll_table)
                self.ui.lineEdit_dice_roll_table.setText(dbObj.dice_roll)
                item_match = QSignalBlocker(self.ui.lineEdit_item_match_roll_table)
                self.ui.lineEdit_item_match_roll_table.clear()
                options = QSignalBlocker(self.ui.comboBox_options_roll_table)
                self.ui.comboBox_options_roll_table.clear()
                for obj in cBoxItems:
                    self.ui.comboBox_options_roll_table.addItem(
                        self.construct_detail_name(obj), obj)
                self.ui.listWidget_table_roll_table.clear()
                for list_item in table:
                    self.ui.listWidget_table_roll_table.addItem(list_item)
            case 'template':
                name = QSignalBlocker(self.ui.lineEdit_template_name)
                self.ui.lineEdit_template_name.setText(dbObj.name)
                is_folder = QSignalBlocker(self.ui.checkBox_is_folder_template)
                self.ui.checkBox_is_folder_template.setChecked(dbObj.is_folder)
                stack = QSignalBlocker(self.ui.comboBox_stack_template)
                self.ui.comboBox_stack_template.clear()
                # just templates please
                all_templates = db.Templates.select(detail_type='template')
                # NOT this template please.
                all_templates = [ t for t in all_templates if not t.name == dbObj.name ]
                for template in all_templates:
                    if not template.is_folder:
                        self.ui.comboBox_stack_template.addItem(template.name,
                                                                userData=template)
