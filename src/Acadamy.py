
from pony.orm import db_session, commit
from PySide6.QtWidgets import (QDialog, QListWidgetItem)
from ui.Acadamy_Dialog import Ui_acadamy_dialog



class AcadamyDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui_vault = parent
        self.ui = Ui_acadamy_dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_new_template.clicked.connect(self.new_template)
        self.ui.lineEdit_template_name.textChanged.connect(self.update_template_name)
        self.ui.verticalStackedWidget_forms.setCurrentIndex(0)
        self.ui.listWidget_all_templates.clicked.connect(self.select_template)
        self.ui.pushButton_add_type_template.clicked.connect(self.template_page_type_add)
        self.ui.listWidget_template_detail.clicked.connect(self.select_detail)
        self.ui.lineEdit_name_lore.textEdited.connect(self.update_lore_name)
        self.ui.textEdit_content_lore.textChanged.connect(self.update_lore_content)
        self.ui.pushButton_delete_lore.clicked.connect(self.delete_lore)
        # I could probably get this mapping dynamicly from the stacked
        # Widget thing. But for now a manual mapping saves time.
        self.target = None
        self.detail_target = None
        self.pageIndex = {'spalsh': 0,
                          'template': 1,
                          'Lore': 2,
                          'Ability Scores': 3,
                          'Attributes': 4,
                          'Items': 5,
                          'Actions': 6}
        self.populate_listWidget_all_templates()


    @db_session
    def delete_lore(self):
        db = self.ui_vault.main.db
        detail_templates = self.ui.listWidget_template_detail
        dbObj = db.Lore[self.detail_target.dbObj.id]
        dbObj.delete()
        commit()
        detail_templates = self.ui.listWidget_template_detail
        index = detail_templates.indexFromItem(self.detail_target)
        detail_templates.takeItem(index.row())
        self.select_detail()


    @db_session
    def update_lore_content(self):
        db = self.ui_vault.main.db
        dbObj = db.Lore[self.detail_target.dbObj.id]
        dbObj.content = self.ui.textEdit_content_lore.toPlainText()


    @db_session
    def select_detail(self):
        db = self.ui_vault.main.db
        detail_templates = self.ui.listWidget_template_detail
        forms = self.ui.verticalStackedWidget_forms
        for row in range(0, detail_templates.count()):
            if detail_templates.item(row).isSelected():
                item = detail_templates.item(row)
                match type(item.dbObj):
                    case db.Lore:
                        self.detail_target = item
                        self.load_lore_page()
                        forms.setCurrentIndex(self.pageIndex['Lore'])
                    case db.Stats:
                        self.detail_target = item
                        forms.setCurrentIndex(self.pageIndex['Ability Scores'])
                    case db.Attributes:
                        self.detail_target = item
                        forms.setCurrentIndex(self.pageIndex['Attributes'])
                    case db.Actions:
                        self.detail_target = item
                        forms.setCurrentIndex(self.pageIndex['Actions'])
                    case db.Items:
                        self.detail_target = item
                        forms.setCurrentIndex(self.pageIndex['Items'])
                    case db.Templates:
                        self.target = item
                        forms.setCurrentIndex(self.pageIndex['template'])


    @db_session
    def update_lore_name(self):
        db = self.ui_vault.main.db
        self.detail_target.dbObj = db.Lore[self.detail_target.dbObj.id]
        self.detail_target.dbObj.name = self.ui.lineEdit_name_lore.text()
        self.update_detail_view()


    def template_page_type_add(self):
        selection  = self.ui.comboBox_type_templates_page.currentText()
        self.add_child(selection)


    @db_session
    def select_template(self):
        all_templates = self.ui.listWidget_all_templates
        forms = self.ui.verticalStackedWidget_forms
        for row in range(0, all_templates.count()):
            if all_templates.item(row).isSelected():
                item = all_templates.item(row)
                self.target = item
                self.populate_listWidget_template_detail()
                forms.setCurrentIndex(self.pageIndex['template'])
                self.load_template_page()



    @db_session
    def populate_listWidget_all_templates(self):
        db = self.ui_vault.main.db
        all_templates = self.ui.listWidget_all_templates
        for dbObj in db.Templates.select():
            item = QListWidgetItem(dbObj.name)
            item.dbObj = dbObj
            all_templates.addItem(item)

    @db_session
    def populate_listWidget_template_detail(self):
        db = self.ui_vault.main.db
        template_detail = self.ui.listWidget_template_detail
        # clear the listWidget
        template_detail.clear()
        all_templates = self.ui.listWidget_all_templates

        if self.target:
            depth = 0
            parent = db.Templates[self.target.dbObj.id]
            item = QListWidgetItem((' '*depth) + parent.name)
            item.type = 'parent'
            template_detail.addItem(item)

            def draw_items(dbObj, depth):
                dbObj.load()
                for child in dbObj.under:
                    item = QListWidgetItem((' '*depth) + child.name)
                    item.dbObj = child
                    template_detail.addItem(item)
                    for grandchild in child.under:
                        draw_items(dbObj, depth + 1)
            draw_items(parent, depth)


    @db_session
    def update_template_name(self):
        db = self.ui_vault.main.db
        name = self.ui.lineEdit_template_name.text()
        self.target.dbObj = db.Templates[self.target.dbObj.id]
        self.target.dbObj.name = name
        commit()
        self.target.setText(f"{name}")
        self.update_detail_view()



    @db_session
    def add_child(self, selection, child=None):
        db = self.ui_vault.main.db
        parent = db.Templates[self.target.dbObj.id]
        forms = self.ui.verticalStackedWidget_forms
        if selection == 'Lore':
            child = db.Lore(name='*lore*')
            parent.lore.add(child)
            self.update_detail_view()
            self.update_detail_view_select(child)
            self.load_lore_page()
            forms.setCurrentIndex(self.pageIndex[selection])
        elif selection == 'Ability Scores':
            child = db.Stats(name=' *Ability Scores* ')
            parent.lore.create(name=' *lore* ')
            self.load_ability_scores()
            forms.setCurrentIndex(self.pageIndex[selection])
        elif selection == 'Attributes':
            child = db.Attributes(name=' *Attributes* ')
            parent.lore.create(name=' *lore* ')
            self.load_attributes()
            forms.setCurrentIndex(self.pageIndex[selection])
        elif selection == 'Items':
            child = db.Items(name=' *Items* ')
            parent.lore.create(name=' *lore* ')
            self.load_items()
            forms.setCurrentIndex(self.pageIndex[selection])
        elif selection == 'Actions':
            child = db.Actions(name=' *Actions* ')
            parent.lore.create(name=' *lore* ')
            self.load_actions()
            forms.setCurrentIndex(self.pageIndex[selection])
        elif child:
            parent.under.add(child)


    @db_session
    def update_detail_view_select(self, dbObj):
        db = self.ui_vault.main.db
        template_detail = self.ui.listWidget_template_detail
        for row in range(0, template_detail.count()):
            item = template_detail.item(row)
            if item.dbObj == dbObj:
                self.detail_target = item
                template_detail.scrollToItem(item)
                template_detail.setCurrentItem(item)



    @db_session
    def update_detail_view(self):
        db = self.ui_vault.main.db
        template_detail = self.ui.listWidget_template_detail
        template_detail.clear()
        self.target.dbObj = db.Templates[self.target.dbObj.id]
        rows = []
        rows.append(self.target.dbObj)
        for row in self.target.dbObj.lore:
            rows.append(row)
        for row in self.target.dbObj.attributes:
            rows.append(row)
        for row in self.target.dbObj.items:
            rows.append(row)
        for row in self.target.dbObj.actions:
            rows.append(row)
        for row in self.target.dbObj.stats:
            rows.append(row)
        for row in rows:
            item = QListWidgetItem(row.name)
            item.dbObj = row
            template_detail.addItem(item)

    @db_session
    def new_template(self):
        new_template = self.ui_vault.main.db.Templates(name=' *** ')
        all_templates = self.ui.listWidget_all_templates
        forms = self.ui.verticalStackedWidget_forms

        item = QListWidgetItem("*new template*")
        item.dbObj = new_template
        self.target = item
        all_templates.addItem(item)

        self.load_template_page()
        # change right side page to new template editor
        forms.setCurrentIndex(self.pageIndex['template'])

        # turn on or switch Selected Template to details
        self.update_detail_view()


    @db_session
    def load_template_page(self):
        db = self.ui_vault.main.db
        all_templates = db.Templates.select()
        self.target.dbObj = db.Templates[self.target.dbObj.id]
        self.ui.lineEdit_template_name.setText(self.target.dbObj.name)
        self.ui.lineEdit_filter_templates_page.clear()

        self.ui.comboBox_templates_page.clear()
        for template in all_templates:
            self.ui.comboBox_templates_page.addItem(template.name,
                                                    userData=template)


    def load_lore_page(self):
        db = self.ui_vault.main.db
        lore = db.Lore[self.detail_target.dbObj.id]
        self.ui.lineEdit_name_lore.setText(lore.name)
        self.ui.textEdit_content_lore.setText(lore.content)

    def load_ability_scores_page(self):
        pass

    def load_attributes_page(self):
        pass

    def load_items_page(self):
        pass

    def load_actions_page(self):
        pass
