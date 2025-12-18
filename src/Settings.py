
from ui.Settings_Dialog import Ui_Settings
from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6.QtCore import QStandardPaths
from pony.orm import db_session, commit
import os

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.main = parent
        self.ui = Ui_Settings()
        self.ui.setupUi(self)
        self.ui.pushButton_back.clicked.connect(self.save_and_close)
        self.default_templ = '''AC: <>
STR: 10    DEX: 10    CON: 10    WIS: 10    INT: 10    CHA: 10

====[ Status Effects ]====
====[ Attributes ]====
====[ Actions ]====
=[Action 1]=:
    cost: 1 action
    limitations: targets 1, melee
    <> to hit
    On hit: <>'''
        self.load()

    @db_session
    def load(self):
        settings = self.main.db.Settings
        cbox_sys = self.ui.comboBox_system

        templ_setting = settings.get(name='pc_npc_template')
        pnp_system_name = settings.get(name='pnp_system_name')
        default_save_dir = QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation)

        for fname in os.listdir(default_save_dir):
            if '.ini' in fname[-4:]:
                cbox_sys.addItem(fname[:-4])

        if templ_setting:
            self.ui.plainTextEdit_template.setPlainText(templ_setting.value)
        else:
            self.ui.plainTextEdit_template.setPlainText(self.default_templ)
        if pnp_system_name:
            cbox_sys.setCurrentIndex(cbox_sys.findText(pnp_system_name.value))


    @db_session
    def save_and_close(self):
        # Write player_npc_template to config file. 
        # Write system selection to config file.
        settings = self.main.db.Settings
        cbox_sys = self.ui.comboBox_system

        templ_setting = settings.get(name='pc_npc_template')
        pnp_system_name = settings.get(name='pnp_system_name')
        if templ_setting:
            if not self.ui.plainTextEdit_template.toPlainText() == '':
                templ_setting.value = self.ui.plainTextEdit_template.toPlainText()
            else:
                self.ui.plainTextEdit_template.setPlainText(self.default_templ)
                templ_setting.value = self.default_templ
        else:
            settings(name='pc_npc_template',value=self.ui.plainTextEdit_template.toPlainText())

        if pnp_system_name:
            pnp_system_name.value = cbox_sys.currentText()
        else:
            settings(name='pnp_system_name',value=cbox_sys.currentText())
        self.update()
        self.close()
