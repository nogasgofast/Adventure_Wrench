
from pony.orm import db_session, commit
from PySide6.QtWidgets import (QDialog, QListWidgetItem, QMessageBox)
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
        self.ui.pushButton_delete_lore.clicked.connect(self.delete_detail)
        self.ui.pushButton_delete_stats.clicked.connect(self.delete_detail)
        self.ui.pushButton_add_detail.clicked.connect(self.add_detail)
        self.ui.pushButton_delete_template.clicked.connect(self.delete_template)
        self.ui.pushButton_delete_attribute.clicked.connect(self.delete_detail)
        self.ui.pushButton_delete_item.clicked.connect(self.delete_detail)
        self.ui.pushButton_delete_action.clicked.connect(self.delete_detail)
        self.ui.pushButton_add_item_roll_table.clicked.connect(self.add_item_roll_table)
        self.ui.pushButton_delete_item_roll_table.clicked.connect(self.delete_item_roll_table)
        self.ui.pushButton_delete_roll_table.clicked.connect(self.delete_detail)
        self.ui.pushButton_stack_template.clicked.connect(self.stack_template)
        self.ui.pushButton_back.clicked.connect(self.close)
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


        self.ui.listWidget_all_templates.clicked.connect(self.select_template)
        self.ui.listWidget_template.clicked.connect(self.select_detail)
        self.ui.listWidget_table_roll_table.clicked.connect(self.rt_item_select)

        self.ui.lineEdit_template_name.textEdited.connect(self.update_template_name)
        self.ui.lineEdit_name_lore.textEdited.connect(self.update_name_lore)
        self.ui.lineEdit_content_stats.textEdited.connect(self.update_content_stats)
        self.ui.lineEdit_name_attribute.textEdited.connect(self.update_name_attribute)
        self.ui.lineEdit_content_attribute.textEdited.connect(self.update_content_attribute)
        self.ui.lineEdit_name_item.textEdited.connect(self.update_name_item)
        self.ui.lineEdit_weight_item.textEdited.connect(self.update_weight_item)
        self.ui.lineEdit_name_action.textEdited.connect(self.update_name_action)
        self.ui.lineEdit_cost_action.textEdited.connect(self.update_cost_action)
        self.ui.lineEdit_limitations_action.textEdited.connect(self.update_limitations_action)
        self.ui.lineEdit_name_roll_table.textEdited.connect(self.update_name_roll_table)
        self.ui.lineEdit_dice_roll_table.textEdited.connect(self.update_dice_roll_table)

        self.ui.spinBox_quantity_item.valueChanged.connect(self.update_quantity_item)

        self.ui.textEdit_content_lore.textChanged.connect(self.update_content_lore)
        self.ui.textEdit_description_item.textChanged.connect(self.update_description_item)
        self.ui.textEdit_result_action.textChanged.connect(self.update_result_action)

        self.ui.comboBox_name_stats.currentIndexChanged.connect(self.update_name_stats)

        self.ui.checkBox_israndom_roll_table.stateChanged.connect(self.update_israndom_roll_table)
        self.ui.checkBox_interpret_roll_table.stateChanged.connect(self.update_immutable_roll_table)
        self.ui.checkBox_is_folder_template.stateChanged.connect(self.update_is_folder)

        self.target = None
        self.detail_target = None
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
        dbObj = db.Templates[self.target.dbObj.id]
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
        dbObj = db.Templates[self.target.dbObj.id]
        if dbObj.is_folder:
            return
        all_templates = self.ui.listWidget_all_templates
        forms = self.ui.verticalStackedWidget_forms

        # create a new template with this templates name
        new_template = db.Templates(name=dbObj.name, detail_type='template')
        commit()
        # set this templates is_folder property
        dbObj.is_folder = True
        commit()
        self.update_template_name()
        # create rollTable
        new_roll_table = new_template.under_me.create(detail_type='rtable',
                                                      name=dbObj.name)
        commit()
        # import each high level item into a roll table. Count them.
        count = 0
        for thing in dbObj.under_me:
            count += 1
            rt_item = new_roll_table.roll_table_items.create(match=str(count),
                                                             table_item=thing)
            commit()
            rt_item.rtable = new_roll_table

        # lastly set the number of sites for the dice
        roll = '1d' + str(count)
        new_roll_table.dice_roll = roll
        # finally change page to new template.
        self.new_template(x=False, template=new_template)
        # refresh all templates view
        self.select_template()


    def next_buttons(self):
        forms = self.ui.verticalStackedWidget_forms
        for item in self.ui.listWidget_template.selectedItems():
            item.setSelected(False)
        self.ui.listWidget_template.item(0).setSelected(True)
        forms.setCurrentIndex(self.pageIndex['template'])


    @db_session
    def update_is_folder(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.target.dbObj.id]
        dbObj.is_folder = self.ui.checkBox_is_folder_template.isChecked()
        if dbObj.is_folder:
            self.target.setText(f"Folder: {dbObj.name}")
        else:
            self.target.setText(f"{dbObj.name}")
        self.init_detail_view()


    @db_session
    def stack_template(self):
        db = self.ui_vault.main.db
        template_selecter = self.ui.comboBox_stack_template
        template = db.Templates[self.target.dbObj.id]
        child = template_selecter.currentData()
        child = db.Templates[child.id]
        template.under_me.add(child)
        self.init_detail_view()


    @db_session
    def update_name_roll_table(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.name = self.ui.lineEdit_name_roll_table.text()
        commit()
        self.update_detail(dbObj)

    @db_session
    def update_israndom_roll_table(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.is_random = self.ui.checkBox_israndom_roll_table.isChecked()


    @db_session
    def update_immutable_roll_table(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.onlyPrint = self.ui.checkBox_interpret_roll_table.isChecked()


    @db_session
    def update_dice_roll_table(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.dice_roll = self.ui.lineEdit_dice_roll_table.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def add_item_roll_table(self):
        db = self.ui_vault.main.db
        rollTable = db.Templates[self.detail_target.dbObj.id]
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
    def update_name_action(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.name = self.ui.lineEdit_name_action.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_cost_action(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.cost = self.ui.lineEdit_cost_action.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_limitations_action(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.limitations = self.ui.lineEdit_limitations_action.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_result_action(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.result = self.ui.textEdit_result_action.toPlainText()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_name_item(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.name = self.ui.lineEdit_name_item.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_weight_item(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.weight = self.ui.lineEdit_weight_item.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_quantity_item(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.quantity = self.ui.spinBox_quantity_item.value()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_description_item(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.description = self.ui.textEdit_description_item.toPlainText()
        commit()
        self.update_detail(dbObj)

    @db_session
    def update_name_attribute(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.name = self.ui.lineEdit_name_attribute.text()
        commit()
        self.update_detail(dbObj)

    @db_session
    def update_content_attribute(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.description = self.ui.lineEdit_content_attribute.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_name_stats(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.name = self.ui.comboBox_name_stats.currentText()
        commit()
        self.update_detail(dbObj)

    @db_session
    def update_content_stats(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.description = self.ui.lineEdit_content_stats.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def delete_template(self):
        db = self.ui_vault.main.db
        forms = self.ui.verticalStackedWidget_forms
        all_templates = self.ui.listWidget_all_templates
        dbObj = db.Templates[self.target.dbObj.id]
        # delete child stuff that's not templates contained here.
        [ t.delete() for t in dbObj.under_me if not t.detail_type == 'template' ]
        commit()
        dbObj.delete()
        commit()
        index = all_templates.indexFromItem(self.target)
        all_templates.item(index.row()).setSelected(False)
        all_templates.takeItem(index.row())
        forms.setCurrentIndex(self.pageIndex['splash'])
        self.ui.listWidget_template.clear()
        self.select_template()


    @db_session
    def update_name_lore(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.name = self.ui.lineEdit_name_lore.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_content_lore(self):
        db = self.ui_vault.main.db
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.description = self.ui.textEdit_content_lore.toPlainText()


    @db_session
    def delete_detail(self):
        'deletes any detail in detail_view'
        db = self.ui_vault.main.db
        forms = self.ui.verticalStackedWidget_forms
        detail_templates = self.ui.listWidget_template
        dbObj = db.Templates[self.detail_target.dbObj.id]
        dbObj.delete()
        commit()
        detail_templates = self.ui.listWidget_template
        index = detail_templates.indexFromItem(self.detail_target)
        detail_templates.takeItem(index.row())
        # pre-emptivly changed to the templates page in case we can't select
        # anything else.
        forms.setCurrentIndex(self.pageIndex['template'])
        self.select_detail()


    @db_session
    def select_detail(self):
        'sets self.detail_target and changes the form page'
        db = self.ui_vault.main.db
        detail_templates = self.ui.listWidget_template
        forms = self.ui.verticalStackedWidget_forms
        item = None
        for row in range(0, detail_templates.count()):
            if detail_templates.item(row).isSelected():
                item = detail_templates.item(row)
                break
        if not item:
            return
        self.detail_target = item
        self.init_page(item.dbObj)
        match item.dbObj.detail_type:
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
                all_temp_view = self.ui.listWidget_all_templates
                # for all rows
                dbObj = db.Templates[item.dbObj.id]
                for row in range(0, all_temp_view.count()):
                    template_item = all_temp_view.item(row)
                    template_item.dbObj = db.Templates[template_item.dbObj.id]
                    # if we found the matching object in the other view
                    if template_item.dbObj == dbObj:
                        for selection in all_temp_view.selectedItems():
                            selection.setSelected(False)
                        all_temp_view.item(row).setSelected(True)
                        self.target = template_item
                        self.init_page(template_item.dbObj)
                        self.init_detail_view()
                        forms.setCurrentIndex(self.pageIndex['template'])
                        break



    def select_template(self):
        'sets self.target and changes to the templates page'
        templates_view = self.ui.listWidget_all_templates
        forms = self.ui.verticalStackedWidget_forms
        for row in range(0, templates_view.count()):
            if templates_view.item(row).isSelected():
                item = templates_view.item(row)
                self.target = item
                self.init_page(self.target.dbObj)
                self.init_detail_view()
                forms.setCurrentIndex(self.pageIndex['template'])

    @db_session
    def load_acadamy(self):
        'initialize templates view'
        db = self.ui_vault.main.db
        self.ui.listWidget_template.clear()
        templates_view = self.ui.listWidget_all_templates
        templates_view.clear()
        for dbObj in db.Templates.select(detail_type='template'):
            if dbObj.is_folder:
                item = QListWidgetItem(f"Folder: {dbObj.name}")
            else:
                item = QListWidgetItem(dbObj.name)
            item.dbObj = dbObj
            templates_view.addItem(item)


    @db_session
    def update_template_name(self):
        'pretty self explanitory, it is for a text field update'
        db = self.ui_vault.main.db
        name = self.ui.lineEdit_template_name.text()
        self.target.dbObj = db.Templates[self.target.dbObj.id]
        self.target.dbObj.name = name
        commit()
        if self.target.dbObj.is_folder:
            self.target.setText(f"Folder: {name}")
        else:
            self.target.setText(f"{name}")
        self.init_detail_view()


    def update_detail(self, dbObj):
        'change name of one item in template panel'
        indent = 0
        oldName = self.detail_target.text()
        newName = self.detail_target.text().removeprefix('    ')
        while not oldName == newName:
            indent += 1
            oldName = newName
            newName = oldName.removeprefix('    ')
        title = ('    ' * indent) + self.construct_detail_name(dbObj)
        self.detail_target.setText(title)


    @db_session
    def add_detail(self, selection=None):
        'add a template component to the selected template'
        if not selection:
            selection  = self.ui.comboBox_type_templates_page.currentText()
        db = self.ui_vault.main.db
        parent = db.Templates[self.target.dbObj.id]
        forms = self.ui.verticalStackedWidget_forms
        match selection:
            case 'Lore':
                dbObj = parent.under_me.create(detail_type='lore')
            case 'Stat Modification':
                dbObj = parent.under_me.create(detail_type='stat')
            case 'Attributes':
                dbObj = parent.under_me.create(detail_type='attribute')
            case 'Items':
                dbObj = parent.under_me.create(detail_type='item')
            case 'Actions':
                dbObj = parent.under_me.create(detail_type='action')
            case 'Roll Table':
                dbObj = parent.under_me.create(detail_type='rtable')
        commit()
        name = '    ' + self.construct_detail_name(dbObj)
        item = QListWidgetItem(name)
        item.dbObj = dbObj
        self.detail_target = item
        self.ui.listWidget_template.addItem(item)
        item.setSelected(True)
        self.init_page(dbObj)
        forms.setCurrentIndex(self.pageIndex[selection])


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
    def init_detail_view(self):
        'destrutive rebuilding of the detail_view'
        db = self.ui_vault.main.db
        template_detail = self.ui.listWidget_template
        template_detail.clear()
        template = db.Templates[self.target.dbObj.id]
        self.detail_target = template
        parent = QListWidgetItem(self.construct_detail_name(template))
        parent.dbObj = template
        template_detail.addItem(parent)

        indent = 1
        def create_detail_view(template, indent):
            for row in template.under_me:
                title = ('    ' * indent) + self.construct_detail_name(row)
                item = QListWidgetItem(title)
                item.dbObj = row
                template_detail.addItem(item)
                # TODO this does not recurse right under the new regime
                if row.detail_type == 'template':
                    create_detail_view(row, indent + 1)
        create_detail_view(template, indent)



    @db_session
    def new_template(self, x=False, template=None):
        'creates template and updates ui'
        db = self.ui_vault.main.db
        if template is None:
            new_template = db.Templates(name='*new template*',
                                        detail_type='template')
            commit()
        else:
            new_template = db.Templates[template.id]
        all_templates = self.ui.listWidget_all_templates
        forms = self.ui.verticalStackedWidget_forms

        if template is None:
            item = QListWidgetItem("*new template*")
        else:
            item = QListWidgetItem(new_template.name)
        item.dbObj = new_template
        self.target = item
        all_templates.addItem(item)
        index = all_templates.indexFromItem(item)
        all_templates.item(index.row()).setSelected(True)

        self.init_page(item.dbObj)
        # change right side page to new template editor
        forms.setCurrentIndex(self.pageIndex['template'])
        self.init_detail_view()


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
        dbObj = db.Templates[dbObj.id]
        match dbObj.detail_type:
            case 'lore':
                self.ui.lineEdit_name_lore.setText(dbObj.name)
                self.ui.textEdit_content_lore.setPlainText(dbObj.description)
            case 'stat':
                index = self.ui.comboBox_name_stats.findText(dbObj.name)
                self.ui.comboBox_name_stats.setCurrentIndex(index)
                self.ui.lineEdit_content_stats.setText(dbObj.description)
            case 'attribute':
                self.ui.lineEdit_name_attribute.setText(dbObj.name)
                self.ui.lineEdit_content_attribute.setText(dbObj.description)
            case 'action':
                self.ui.lineEdit_name_action.setText(dbObj.name)
                self.ui.lineEdit_cost_action.setText(dbObj.cost)
                self.ui.lineEdit_limitations_action.setText(dbObj.limitations)
                self.ui.textEdit_result_action.setPlainText(dbObj.result)
            case 'item':
                self.ui.lineEdit_name_item.setText(dbObj.name)
                self.ui.lineEdit_weight_item.setText(str(dbObj.weight))
                if dbObj.quantity:
                    self.ui.spinBox_quantity_item.setValue(dbObj.quantity)
                else:
                    self.ui.spinBox_quantity_item.setValue(1)
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
                self.ui.lineEdit_name_roll_table.setText(dbObj.name)
                self.ui.checkBox_israndom_roll_table.setChecked(dbObj.is_random)
                self.ui.checkBox_interpret_roll_table.setChecked(dbObj.onlyPrint)
                self.ui.lineEdit_dice_roll_table.setText(dbObj.dice_roll)
                self.ui.lineEdit_item_match_roll_table.clear()
                self.ui.comboBox_options_roll_table.clear()
                for obj in cBoxItems:
                    self.ui.comboBox_options_roll_table.addItem(
                        self.construct_detail_name(obj), obj)
                self.ui.listWidget_table_roll_table.clear()
                for list_item in table:
                    self.ui.listWidget_table_roll_table.addItem(list_item)
            case 'template':
                self.ui.lineEdit_template_name.setText(dbObj.name)
                self.ui.checkBox_is_folder_template.setChecked(dbObj.is_folder)
                self.ui.comboBox_stack_template.clear()
                # just templates please
                all_templates = db.Templates.select(detail_type='template')
                # NOT this template please.
                all_templates = [ t for t in all_templates if not t.name == dbObj.name ]
                for template in all_templates:
                    if not template.is_folder:
                        self.ui.comboBox_stack_template.addItem(template.name,
                                                                userData=template)
