
from pony.orm import db_session, commit
from PySide6.QtWidgets import (QDialog, QListWidgetItem)
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
        # TODO this feature is blocked by a code refactoring see rt_item_select.
        # self.ui.listWidget_table_roll_table.clicked.connect(self.rt_item_select)

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
        self.ui.checkBox_immutable_roll_table.stateChanged.connect(self.update_immutable_roll_table)
        self.ui.checkBox_is_folder_template.stateChanged.connect(self.update_is_folder)

        self.target = None
        self.detail_target = None
        # This mapping lets me diss-connect combobox positions from pageIndex.
        # and instead use page names directly.
        self.pageIndex = {'splash': 0,
                          'template': 1,
                          'Lore': 2,
                          'Ability Scores': 3,
                          'Attributes': 4,
                          'Items': 5,
                          'Actions': 6,
                          'Roll Table': 7}
        self.populate_listWidget_all_templates()


    # TODO rebuild database and everything that uses it.
    # The explicit difference between lore/stats/attricutes/items
    # causes me to make tokenizers all over the place. but because
    # these details are all pretty much just data rows for templates
    # I'll be rebuilding them all into one type of object/table
    # then removing the tokenizers that showed up everywhere.
    # this function does most of what it should beut find_name
    # does not work.
    # @db_session
    # def rt_item_select(self):
    #     db = self.ui_vault.main.db
    #     roll_table_view = self.ui.listWidget_table_roll_table
    #     match_field = self.ui.lineEdit_item_match_roll_table
    #     option_field = self.ui.comboBox_options_roll_table
    #
    #     def find_name(dbObj):
    #         if dbObj.lore:
    #             name = dbObj.lore.to_strings()
    #         elif dbObj.attribute:
    #             name = dbObj.attribute.to_strings()
    #         elif dbObj.stat:
    #             name = dbObj.stat.to_strings()
    #         elif dbObj.item:
    #             name = dbObj.item.to_strings()
    #         elif dbObj.action:
    #             name = dbObj.action.to_strings()
    #         elif dbObj.rtable:
    #             name = dbObj.rtable.to_strings()
    #         else:
    #             raise Exception('Rtable_items object missing details')
    #         print(name)
    #         return name
    #
    #     for row in range(0, roll_table_view.count()):
    #         item = roll_table_view.item(row)
    #         if item.isSelected():
    #             dbObj = db.Rtable_items[item.dbObj.id]
    #             match_field.setText(dbObj.match)
    #             index = option_field.findText(find_name(dbObj))
    #             option_field.setCurrentIndex(index)


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
        new_template = db.Templates(name=dbObj.name)
        commit()
        # set this templates is_folder property
        dbObj.is_folder = True
        commit()
        self.update_template_name()
        # create rollTable
        new_roll_table = new_template.rtables.create(isRandom=False)
        commit()
        # import each high level item into a roll table. Count them.
        count = 0
        for lore in dbObj.lore:
            count += 1
            rt_item = new_roll_table.items.create(match=str(count),
                                                  lore=lore)
            commit()
            rt_item.table = new_roll_table
        for attribute in dbObj.attributes:
            count += 1
            rt_item = new_roll_table.items.create(match=str(count),
                                                  attribute=attribute)
            commit()
            rt_item.table = new_roll_table
        for item in dbObj.items:
            count += 1
            rt_item = new_roll_table.items.create(match=str(count),
                                                  item=item)
            commit()
            rt_item.table = new_roll_table
        for action in dbObj.actions:
            count += 1
            rt_item = new_roll_table.items.create(match=str(count),
                                                  action=action)
            commit()
            rt_item.table = new_roll_table
        for stat in dbObj.stats:
            count += 1
            rt_item = new_roll_table.items.create(match=str(count),
                                                  stat=stat)
            commit()
            rt_item.table = new_roll_table
        for rtable in dbObj.rtables:
            count += 1
            rt_item = new_roll_table.items.create(match=str(count),
                                                  rtable=rtable)
            commit()
            rt_item.table = new_roll_table
        # lastly set the number of sites for the dice
        roll = '1d' + str(count)
        new_roll_table.diceRoll = roll
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
        under = template_selecter.currentData()
        under = db.Templates[under.id]
        if not under is template:
            if not under in template.under:
                template.under.add(under)
        self.init_detail_view()


    @db_session
    def update_name_roll_table(self):
        db = self.ui_vault.main.db
        dbObj = db.Rtables[self.detail_target.dbObj.id]
        dbObj.name = self.ui.lineEdit_name_roll_table.text()
        commit()
        self.update_detail(dbObj)

    @db_session
    def update_israndom_roll_table(self):
        db = self.ui_vault.main.db
        dbObj = db.Rtables[self.detail_target.dbObj.id]
        dbObj.isRandom = self.ui.checkBox_israndom_roll_table.isChecked()

    @db_session
    def update_immutable_roll_table(self):
        db = self.ui_vault.main.db
        dbObj = db.Rtables[self.detail_target.dbObj.id]
        dbObj.immutable = self.ui.checkBox_immutable_roll_table.isChecked()

    @db_session
    def update_dice_roll_table(self):
        db = self.ui_vault.main.db
        dbObj = db.Rtables[self.detail_target.dbObj.id]
        dbObj.diceRoll = self.ui.lineEdit_dice_roll_table.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def add_item_roll_table(self):
        db = self.ui_vault.main.db
        rollTable = db.Rtables[self.detail_target.dbObj.id]
        match  = self.ui.lineEdit_item_match_roll_table.text()
        child = self.ui.comboBox_options_roll_table.currentData()
        rtItem = rollTable.items.create(match=match)
        match type(child):
            case db.Lore:
                child = db.Lore[child.id]
                rtItem.lore = child
            case db.Stats:
                child = db.Stats[child.id]
                rtItem.stat = child
            case db.Attributes:
                child = db.Attributes[child.id]
                rtItem.attribute = child
            case db.Items:
                child = db.Items[child.id]
                rtItem.item = child
            case db.Actions:
                child = db.Actions[child.id]
                rtItem.action = child
            case db.Rtables:
                child = db.Rtables[child.id]
                rtItem.rtable = child
            case db.Templates:
                child = db.Templates[child.id]
                rtItem.template = child
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
        dbObj = db.Actions[self.detail_target.dbObj.id]
        dbObj.name = self.ui.lineEdit_name_action.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_cost_action(self):
        db = self.ui_vault.main.db
        dbObj = db.Actions[self.detail_target.dbObj.id]
        dbObj.cost = self.ui.lineEdit_cost_action.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_limitations_action(self):
        db = self.ui_vault.main.db
        dbObj = db.Actions[self.detail_target.dbObj.id]
        dbObj.limitations = self.ui.lineEdit_limitations_action.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_result_action(self):
        db = self.ui_vault.main.db
        dbObj = db.Actions[self.detail_target.dbObj.id]
        dbObj.result = self.ui.textEdit_result_action.toPlainText()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_name_item(self):
        db = self.ui_vault.main.db
        dbObj = db.Items[self.detail_target.dbObj.id]
        dbObj.name = self.ui.lineEdit_name_item.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_weight_item(self):
        db = self.ui_vault.main.db
        dbObj = db.Items[self.detail_target.dbObj.id]
        dbObj.weight = self.ui.lineEdit_weight_item.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_quantity_item(self):
        db = self.ui_vault.main.db
        dbObj = db.Items[self.detail_target.dbObj.id]
        dbObj.quantity = self.ui.spinBox_quantity_item.value()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_description_item(self):
        db = self.ui_vault.main.db
        dbObj = db.Items[self.detail_target.dbObj.id]
        dbObj.description = self.ui.textEdit_description_item.toPlainText()
        commit()
        self.update_detail(dbObj)

    @db_session
    def update_name_attribute(self):
        db = self.ui_vault.main.db
        dbObj = db.Attributes[self.detail_target.dbObj.id]
        dbObj.name = self.ui.lineEdit_name_attribute.text()
        commit()
        self.update_detail(dbObj)

    @db_session
    def update_content_attribute(self):
        db = self.ui_vault.main.db
        dbObj = db.Attributes[self.detail_target.dbObj.id]
        dbObj.content = self.ui.lineEdit_content_attribute.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_name_stats(self):
        db = self.ui_vault.main.db
        dbObj = db.Stats[self.detail_target.dbObj.id]
        dbObj.name = self.ui.comboBox_name_stats.currentText()
        commit()
        self.update_detail(dbObj)

    @db_session
    def update_content_stats(self):
        db = self.ui_vault.main.db
        dbObj = db.Stats[self.detail_target.dbObj.id]
        dbObj.description = self.ui.lineEdit_content_stats.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def delete_template(self):
        db = self.ui_vault.main.db
        forms = self.ui.verticalStackedWidget_forms
        all_templates = self.ui.listWidget_all_templates
        dbObj = db.Templates[self.target.dbObj.id]
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
        dbObj = db.Lore[self.detail_target.dbObj.id]
        dbObj.name = self.ui.lineEdit_name_lore.text()
        commit()
        self.update_detail(dbObj)


    @db_session
    def update_content_lore(self):
        db = self.ui_vault.main.db
        dbObj = db.Lore[self.detail_target.dbObj.id]
        dbObj.description = self.ui.textEdit_content_lore.toPlainText()


    @db_session
    def delete_detail(self):
        'deletes any detail in detail_view'
        db = self.ui_vault.main.db
        forms = self.ui.verticalStackedWidget_forms
        detail_templates = self.ui.listWidget_template
        match type(self.detail_target.dbObj):
            case db.Lore:
                dbObj = db.Lore[self.detail_target.dbObj.id]
            case db.Stats:
                dbObj = db.Stats[self.detail_target.dbObj.id]
            case db.Attributes:
                dbObj = db.Attributes[self.detail_target.dbObj.id]
            case db.Actions:
                dbObj = db.Actions[self.detail_target.dbObj.id]
            case db.Items:
                dbObj = db.Items[self.detail_target.dbObj.id]
            case db.Templates:
                dbObj = db.Templates[self.detail_target.dbObj.id]
            case db.Rtables:
                dbObj = db.Rtables[self.detail_target.dbObj.id]
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
        for row in range(0, detail_templates.count()):
            if detail_templates.item(row).isSelected():
                item = detail_templates.item(row)
                match type(item.dbObj):
                    case db.Lore:
                        self.detail_target = item
                        self.init_page(item.dbObj)
                        forms.setCurrentIndex(self.pageIndex['Lore'])
                    case db.Stats:
                        self.detail_target = item
                        self.init_page(item.dbObj)
                        forms.setCurrentIndex(self.pageIndex['Ability Scores'])
                    case db.Attributes:
                        self.detail_target = item
                        self.init_page(item.dbObj)
                        forms.setCurrentIndex(self.pageIndex['Attributes'])
                    case db.Actions:
                        self.detail_target = item
                        self.init_page(item.dbObj)
                        forms.setCurrentIndex(self.pageIndex['Actions'])
                    case db.Items:
                        self.detail_target = item
                        self.init_page(item.dbObj)
                        forms.setCurrentIndex(self.pageIndex['Items'])
                    case db.Templates:
                        all_temp = self.ui.listWidget_all_templates
                        # for all rows
                        item.dbObj = db.Templates[item.dbObj.id]
                        for row in range(0, all_temp.count()):
                            template = all_temp.item(row)
                            # if we found the matching object in the other view
                            template.dbObj = db.Templates[template.dbObj.id]
                            if template.dbObj == item.dbObj:
                                for selection in all_temp.selectedItems():
                                    selection.setSelected(False)
                                all_temp.item(row).setSelected(True)
                                self.target = template
                                self.init_page(template.dbObj)
                                forms.setCurrentIndex(self.pageIndex['template'])
                                break
                    case db.Rtables:
                        self.detail_target = item
                        self.init_page(item.dbObj)
                        forms.setCurrentIndex(self.pageIndex['Roll Table'])



    @db_session
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
    def populate_listWidget_all_templates(self):
        'initialize templates view'
        db = self.ui_vault.main.db
        templates_view = self.ui.listWidget_all_templates
        for dbObj in db.Templates.select():
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
                dbObj = parent.lore.create()
            case 'Stat Modification':
                dbObj = parent.stats.create()
            case 'Attributes':
                dbObj = parent.attributes.create()
            case 'Items':
                dbObj = parent.items.create(quantity=1)
            case 'Actions':
                dbObj = parent.actions.create()
            case 'Roll Table':
                dbObj = parent.rtables.create(isRandom=False)
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
        db = self.ui_vault.main.db
        name = ''
        match type(dbObj):
            case db.Lore:
                dbObj = db.Lore[dbObj.id]
                name = f'Lore: {dbObj.name}'
            case db.Stats:
                dbObj = db.Stats[dbObj.id]
                name = f'Ability Score: {dbObj.name} {dbObj.description}'
            case db.Attributes:
                dbObj = db.Attributes[dbObj.id]
                if dbObj.content:
                    name = f'Attribute: {dbObj.name}: {dbObj.content}'
                else:
                    name = f'Attribute: {dbObj.name}'
            case db.Items:
                dbObj = db.Items[dbObj.id]
                name = f'Item: {dbObj.name} No.{dbObj.quantity} weight: {dbObj.weight} '
            case db.Actions:
                dbObj = db.Actions[dbObj.id]
                name = f'Action: {dbObj.name}'
            case db.Templates:
                dbObj = db.Templates[dbObj.id]
                if dbObj.is_folder:
                    name = f'Folder: {dbObj.name}'
                else:
                    name = f'Template: {dbObj.name}'
            case db.Rtables:
                dbObj = db.Rtables[dbObj.id]
                name = f'Roll Table: {dbObj.name} {dbObj.diceRoll}'
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

        def get_details(template):
            details = []
            for row in template.lore:
                details.append(row)
            for row in template.attributes:
                details.append(row)
            for row in template.items:
                details.append(row)
            for row in template.actions:
                details.append(row)
            for row in template.stats:
                details.append(row)
            for row in template.rtables:
                details.append(row)
            for row in template.under:
                details.append(row)
            return details

        indent = 1
        def create_detail_view(template, indent):
            for row in get_details(template):
                title = ('    ' * indent) + self.construct_detail_name(row)
                item = QListWidgetItem(title)
                item.dbObj = row
                template_detail.addItem(item)
                if type(row) is db.Templates:
                    create_detail_view(row, indent + 1)
        create_detail_view(template, indent)



    @db_session
    def new_template(self, x=False, template=None):
        'creates template and updates ui'
        print(template)
        db = self.ui_vault.main.db
        if template is None:
            new_template = db.Templates(name='*new template*')
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
    def construct_roll_table_name(self, dbObj):
        'private method for name construction'
        db = self.ui_vault.main.db
        item = db.Rtable_items[dbObj.id]
        item_child = ''
        if item.lore:
            item_child = item.lore
        if item.attribute:
            item_child = item.attribute
        if item.stat:
            item_child = item.stat
        if item.item:
            item_child = item.item
        if item.action:
            item_child = item.action
        item_child = self.construct_detail_name(item_child)
        return f'{item.match}: {item_child}'


    @db_session
    def init_page(self, dbObj):
        'all your setup needs for every panel in this applet'
        db = self.ui_vault.main.db
        match type(dbObj):
            case db.Lore:
                lore = db.Lore[dbObj.id]
                self.ui.lineEdit_name_lore.setText(lore.name)
                self.ui.textEdit_content_lore.setPlainText(lore.description)
            case db.Stats:
                stat = db.Stats[dbObj.id]
                index = self.ui.comboBox_name_stats.findText(stat.name)
                self.ui.comboBox_name_stats.setCurrentIndex(index)
                self.ui.lineEdit_content_stats.setText(stat.description)
            case db.Attributes:
                attribute = db.Attributes[dbObj.id]
                self.ui.lineEdit_name_attribute.setText(attribute.name)
                self.ui.lineEdit_content_attribute.setText(attribute.content)
            case db.Actions:
                action = db.Actions[dbObj.id]
                self.ui.lineEdit_name_action.setText(action.name)
                self.ui.lineEdit_cost_action.setText(action.cost)
                self.ui.lineEdit_limitations_action.setText(action.limitations)
                self.ui.textEdit_result_action.setPlainText(action.result)
            case db.Items:
                item = db.Items[dbObj.id]
                self.ui.lineEdit_name_item.setText(item.name)
                self.ui.lineEdit_weight_item.setText(str(item.weight))
                if item.quantity:
                    self.ui.spinBox_quantity_item.setValue(item.quantity)
                else:
                    self.ui.spinBox_quantity_item.setValue(1)
                self.ui.textEdit_description_item.setPlainText(item.description)
            case db.Templates:
                dbObj = db.Templates[dbObj.id]
                self.ui.lineEdit_template_name.setText(dbObj.name)
                self.ui.checkBox_is_folder_template.setChecked(dbObj.is_folder)
                self.ui.lineEdit_filter_templates_page.clear()
                self.ui.comboBox_stack_template.clear()
                all_templates = db.Templates.select()
                for template in all_templates:
                    if not template.is_folder:
                        self.ui.comboBox_stack_template.addItem(template.name,
                                                                userData=template)
            case db.Rtables:
                dbObj = db.Rtables[dbObj.id]
                table = []
                for i in dbObj.items:
                    newItem = QListWidgetItem(self.construct_roll_table_name(i))
                    newItem.dbObj = i
                    table.append(newItem)
                cBoxItems = [ x for x in db.Lore.select()]
                cBoxItems += [ x for x in db.Stats.select()]
                cBoxItems += [ x for x in db.Attributes.select()]
                cBoxItems += [ x for x in db.Items.select()]
                cBoxItems += [ x for x in db.Actions.select()]
                self.ui.lineEdit_name_roll_table.setText(dbObj.name)
                self.ui.checkBox_israndom_roll_table.setChecked(dbObj.isRandom)
                self.ui.checkBox_immutable_roll_table.setChecked(dbObj.immutable)
                self.ui.lineEdit_dice_roll_table.setText(dbObj.diceRoll)
                self.ui.lineEdit_item_match_roll_table.clear()
                self.ui.comboBox_options_roll_table.clear()
                for obj in cBoxItems:
                    self.ui.comboBox_options_roll_table.addItem(
                        self.construct_detail_name(obj), obj)
                self.ui.listWidget_table_roll_table.clear()
                for list_item in table:
                    self.ui.listWidget_table_roll_table.addItem(list_item)
