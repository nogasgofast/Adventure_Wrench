
from ui.Template_Dialog import Ui_template_editor

class EncounterSelectorDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.vault = parent
        self.templateEditor = TemplateEditorDialog(self)
        self.ui = Ui_configurator()
        self._view_stats = False
        self.ui.setupUi(self)
        self.update_options_list()
        self.ui.pushButton_back.clicked.connect(self.close)
        # self.ui.listWidget_catagory. \
        #     itemSelectionChanged.connect(self.show_hide_options)
        self.ui.pushButton_init_stats.clicked.connect(self.stats_toggler)
        self.ui.lineEdit_search.textChanged.connect(self.auto_search)
        self.ui.pushButton_create_example.clicked.connect(self.add_preview)
        self.ui.comboBox_type.currentIndexChanged.connect(self.change_type)
        self.ui.pushButton_create.clicked.connect(self.add_item)
        self.ui.pushButton_add.clicked.connect(self.templateEditor.show)
        self.hide_stats()

        # Initalize this combo box with sizes
        sizes = ['tiny', 'small', 'medium', 'large', 'huge', 'gargantuan']
        for size in sizes:
            self.ui.comboBox_size.addItem(size)
        self.ui.comboBox_size.setCurrentIndex(2)
        # Pull a list of options for speed.
        self.locomotives = {'walk': 30, 'fly': 0, 'swim': 0}
        for locomotive in self.locomotives.keys():
            self.ui.comboBox_speed.addItem(locomotive)
        self.ui.comboBox_speed.setCurrentIndex(2)
        self.ui.spinBox_speed.setValue(30)
        self.ui.comboBox_speed.currentIndexChanged.connect(
            self.link_save_and_change_speed)
        self.ui.spinBox_speed.valueChanged.connect(
            self.link_save_new_speed)

    def reset_stats(self):
        # print("reset_stats")
        self.ui.spinBox_STR.setProperty("value", 10)
        self.ui.spinBox_DEX.setProperty("value", 10)
        self.ui.spinBox_CON.setProperty("value", 10)
        self.ui.spinBox_WIS.setProperty("value", 10)
        self.ui.spinBox_INT.setProperty("value", 10)
        self.ui.spinBox_CHA.setProperty("value", 10)

    def change_type(self):
        # print("change_type")
        enc_type = self.ui.comboBox_type.currentText()
        if enc_type == 'creature':
            self.show_speed()
        elif enc_type == 'trap':
            self.hide_speed()
        elif enc_type == 'social':
            self.show_speed()
        self.update_options_list()

    def hide_speed(self):
        # print("hide_speed")
        self.ui.label_speed.hide()
        self.ui.comboBox_speed.hide()
        self.ui.spinBox_speed.hide()

    def show_speed(self):
        # print("show_speed")
        self.ui.label_speed.hide()
        self.ui.comboBox_speed.hide()
        self.ui.spinBox_speed.hide()

    def hide_stats(self):
        # print("hide_stats")
        self.ui.label_STR.hide()
        self.ui.spinBox_STR.hide()
        self.ui.label_DEX.hide()
        self.ui.spinBox_DEX.hide()
        self.ui.label_CON.hide()
        self.ui.spinBox_CON.hide()
        self.ui.label_WIS.hide()
        self.ui.spinBox_WIS.hide()
        self.ui.label_INT.hide()
        self.ui.spinBox_INT.hide()
        self.ui.label_CHA.hide()
        self.ui.spinBox_CHA.hide()

    def show_stats(self):
        # print("show_stats")
        self.ui.label_STR.show()
        self.ui.spinBox_STR.show()
        self.ui.label_DEX.show()
        self.ui.spinBox_DEX.show()
        self.ui.label_CON.show()
        self.ui.spinBox_CON.show()
        self.ui.label_WIS.show()
        self.ui.spinBox_WIS.show()
        self.ui.label_INT.show()
        self.ui.spinBox_INT.show()
        self.ui.label_CHA.show()
        self.ui.spinBox_CHA.show()

    def link_save_new_speed(self):
        # print("link_save_new_speed")
        'if the spinbox changes value save it here'
        locomotive = str(self.ui.comboBox_speed.itemText(
            self.ui.comboBox_speed.currentIndex()))
        self.locomotives[locomotive] = self.ui.spinBox_speed.value()

    def link_save_and_change_speed(self):
        # print("link_save_and_change_speed")
        'set spinbox to new value according to my model'
        locomotive = str(self.ui.comboBox_speed.itemText(
            self.ui.comboBox_speed.currentIndex()))
        self.ui.spinBox_speed.setValue(
            self.locomotives[locomotive])

    def sqrt(self, num):
        if (num // 2) > 1:
            return num // 2
        else:
            return 0

    def gen_item(self):
        # print("gen a creature npc or trap")
        dice_caddy = dice.dice()
        new_item = Encounter()
        presets = Preset_data()
        # new template engine object
        te = Template_factory(new_item)
        # enc_type = self.ui.comboBox_type.itemText(
        #     self.ui.comboBox_type.currentIndex())

        cr_from_ui = self.ui.spinBox_CR.value()
        num_in_group = self.ui.spinBox_group.value()
        TargetCR = cr_from_ui - self.sqrt(num_in_group)

        new_item.set_option('speed', self.locomotives)
        new_item.set_option('size', str(self.ui.comboBox_size.itemText(
            self.ui.comboBox_size.currentIndex())))

        new_item.set_option('name', str(self.ui.lineEdit_Name.text()))
        new_item.set_option('encountergroupOf',
                            int(self.ui.spinBox_group.value()))

        new_item.set_option('cr', TargetCR)
        stats = presets.get(TargetCR)
        for stat in stats.keys():
            new_item.set_option(stat, stats[stat])

        new_item.set_option('STR',
                            self.ui.spinBox_STR.value())
        new_item.set_option('DEX',
                            self.ui.spinBox_DEX.value())
        new_item.set_option('CON',
                            self.ui.spinBox_CON.value())
        new_item.set_option('WIS',
                            self.ui.spinBox_WIS.value())
        new_item.set_option('INT',
                            self.ui.spinBox_INT.value())
        new_item.set_option('CHA',
                            self.ui.spinBox_CHA.value())

        # from list of templates apply these
        templates_selected = self.help_collect_options()

        # tie in the data we have info the template apply
        for tmp in templates_selected:
            te.read(tmp)
            te.apply(self.ui.radioButton_CR.isChecked())

        # roll initiatives
        dex_mod = (new_item.get_option('DEX') - 10) // 2
        new_item.set_option('initiative',
                            dice_caddy.roll('1d20+%s' % (dex_mod)))
        groupHP = []
        # print("initiatives rolled")
        if new_item.get_option('groupOf') > 1:
            # print("creating group HP divergence")
            for creature in range(0, new_item.get_option('groupOf')):
                # print("for the hoard!")
                groupHP.append(
                    dice_caddy.roll(
                        '%s' % dice_caddy.to_dice(
                            new_item.get_option('maxHP'))))
            new_item.set_option('groupHP', groupHP)
        else:
            # print("HP for one plx.")
            hp = dice_caddy.roll(
                '%s' % dice_caddy.to_dice(
                    new_item.get_option('maxHP')))
            # print("hp created: {}".format(hp))
            new_item.set_option('hp', hp)
            # print("item hp set")
        new_item.set_option('type', self.ui.comboBox_type.currentText())
        # print("item type set")
        return new_item

    def add_preview(self, item=False):
        # self.ui.listWidget_options.clear()
        if not item:
            item = self.gen_item()
        name = item.get_option('name')
        if name == '':
            Qitem = QListWidgetItem("*** a mystery ***")
        else:
            Qitem = QListWidgetItem(f"{item.get_option('name')}")
        # print("QListWidgetItem created")
        Qitem.ViewTxt = False
        Qitem.setToolTip(f"{item.to_string()}")
        Qitem.encounter = item
        self.ui.listWidget_options.addItem(Qitem)

# TODO: Stuff and things
    def add_item(self, item=False):
        # print("add something to vault")
        if item is False:
            for row in range(0, len(self.ui.listWidget_options)):
                item = self.ui.listWidget_options.item(row)
                if item.isSelected():
                    Qitem = QListWidgetItem(
                        f"+ {item.encounter.get_option('name')}")
                    Qitem.ViewTxt = False
                    Qitem.setText(f"+ {item.encounter.get_option('name')}")
                    Qitem.setToolTip(f"{item.encounter.to_string()}")
                    Qitem.encounter = item.encounter.copy()
                    Qitem.encounter.set_option('id', self.vault.itemID)
                    self.vault.itemID += 1
                    self.vault.ui.listWidget_Display.addItem(Qitem)
                    # print(f"{len(self.vault.ui.listWidget_Display)}")
            self.ui.listWidget_options.clear()
        else:
            # print("after option dice roll sets")
            # add item to item window
            Qitem = QListWidgetItem("+ %s" % item.get_option('name'))
            # print("QListWidgetItem created")
            Qitem.ViewTxt = False
            Qitem.setToolTip(f"{item.to_string()}")
            Qitem.encounter = item
            Qitem.encounter.set_option('id', self.vault.itemID)
            self.vault.ui.listWidget_Display.addItem(Qitem)
            # print("item added to ui list")
            self.vault.itemID += 1
            # help keyboard users to get back to name
        self.close()

    def reset_selected(self):
        # print("reset_selected")
        for row in range(0, len(self.ui.listWidget_catagory)):
            item = self.ui.listWidget_catagory.item(row)
            if item.isSelected():
                item.setSelected(False)
        self.ui.listWidget_options.clear()

    def auto_search(self):
        # print("auto_search")
        items = []
        if len(self.ui.lineEdit_search.text()) > 2:
            items = self.ui.listWidget_catagory.findItems(
                             self.ui.lineEdit_search.text(),
                             Qt.MatchContains)
            if items:
                for row in range(0, len(self.ui.listWidget_catagory)):
                    item = self.ui.listWidget_catagory.item(row)
                    # print("hiding some things")
                    if item not in items:
                        item.setHidden(True)
                    else:
                        item.setHidden(False)
            else:
                for row in range(0, len(self.ui.listWidget_catagory)):
                    # print("hiding everything")
                    self.ui.listWidget_catagory.item(row).setHidden(True)
        else:
            for row in range(0, len(self.ui.listWidget_catagory)):
                # print("hiding everything")
                self.ui.listWidget_catagory.item(row).setHidden(False)

    def show_hide_options(self):
        # print("show_hide_options")
        # enc_type = self.ui.comboBox_type.currentText()
        selection = []
        for row in range(0, len(self.ui.listWidget_catagory)):
            if self.ui.listWidget_catagory.item(row).isSelected():
                selection.append((self.ui.listWidget_catagory.item(row).text(),
                                  self.ui.listWidget_catagory.
                                  item(row).background()))
        if selection:
            self.add_preview()

    def stats_toggler(self):
        # print("stats_toggler")
        self._view_stats = not self._view_stats
        # print(f"self _view_stats: {self._view_stats}")
        if self._view_stats is True:
            self.show_stats()
        else:
            self.reset_stats()
            self.hide_stats()

    def update_options_list(self):
        # print("update_options_list")
        self.ui.listWidget_catagory.clear()
        pd = Preset_data()
        enc_type = self.ui.comboBox_type.currentText()
        attribute_tmp_list = pd.templates_that_have(enc_type, 'attributes')
        # actions = pd.templates_that_have(enc_type, 'actions')
        # items  = pd.templates_that_have(enc_type, 'items')
        # spells  = pd.templates_that_have(enc_type, 'spells')

        for fname, name in sorted(attribute_tmp_list, key=lambda x: x[1]):
            item = QListWidgetItem(name)
            item.fname = fname
            (red, green, blue) = (166, 244, 175)
            painter = QBrush(QColor(red, green, blue))
            item.setBackground(painter)
            self.ui.listWidget_catagory.addItem(item)

        weapon_catagories = {}

        for weapon in attacks:
            print(weapon)
            for i in weapon[2:]:
                weapon_catagories[i] = 1
        if len(weapon_catagories.keys()) > 0:
            for catagory in sorted(weapon_catagories.keys()):
                print(catagory)
                item = QListWidgetItem("{} weapons".format(catagory))
                item.catagory = catagory
                (red,green,blue)=(244, 178, 166)
                painter = QBrush(QColor(red,green,blue))
                item.setBackground(painter)
                self.ui.listWidget_catagory.addItem(item)

        misc_catagories = {}
        for thing in misc:
            for i in thing[2:]:
                if ';' not in i:
                    misc_catagories[i] = 1

        if len(misc_catagories.keys()) > 0:
            #print weapon_catagories.keys()
            for catagory in sorted(misc_catagories.keys()):
                item = QListWidgetItem("{} misc".format(catagory))
                item.catagory = catagory
                (red,green,blue)=(166, 179, 244)
                painter = QBrush(QColor(red,green,blue))
                item.setBackground(painter)
                self.ui.listWidget_catagory.addItem(item)
                painter = QBrush(QColor(red,green,blue))
                item.setBackground(painter)
                self.ui.listWidget_catagory.addItem(item)

        misc_catagories = {}
        for thing in misc:
            for i in thing[2:]:
                if ';' not in i:
                    misc_catagories[i] = 1

        if len(misc_catagories.keys()) > 0:
            #print weapon_catagories.keys()
            for catagory in sorted(misc_catagories.keys()):
                item = QListWidgetItem("{} misc".format(catagory))
                item.catagory = catagory
                (red,green,blue)=(166, 179, 244)
                painter = QBrush(QColor(red,green,blue))
                item.setBackground(painter)
                self.ui.listWidget_catagory.addItem(item)

    def help_collect_options(self):
        # print("help_collect_options")
        option_list = []
        for row in range(0, len(self.ui.listWidget_catagory)):
            if self.ui.listWidget_catagory.item(row).isSelected():
                option_list.append(self.ui.listWidget_catagory.item(row).fname)
        return option_list


class TemplateEditorDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.selectorDialog = parent
        self.ui = Ui_template_editor()
        self.ui.setupUi(self)
        self.ui.pushButton_back.clicked.connect(self.close)

    def save_to_file():
        pass
