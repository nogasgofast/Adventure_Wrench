
from ui.Player_Dialog import Ui_Player
from PySide6.QtWidgets import QDialog, QListWidgetItem
from pony.orm import db_session, commit

class PlayerDialog(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.main = parent
        self.display_target = None
        self.target = None
        self.ui = Ui_Player()
        self.ui.setupUi(self)
        self.suppress_spinbox_update = False

        self.ui.pushButton_delete.clicked.connect(self.remove_player)
        self.ui.pushButton_back.clicked.connect(self.close)

        self.ui.checkBox_initiative_alarm.stateChanged.connect(self.update_isAlarm)

        self.ui.spinBox_hp.valueChanged.connect(self.update_hp)
        self.ui.spinBox_initiative.valueChanged.connect(self.update_initiative)

        self.ui.lineEdit_name.textChanged.connect(self.update_name)

        self.ui.textEdit_description.textChanged.connect(self.update_description)


    @db_session
    def update_player(self, display_target):
        # this may make more sense in main.py if I decide to add update
        # functionality to Other types of objects
        E = self.main.ui.listWidget_Encounter
        self.display_target = display_target
        self.target = self.main.db.Active[self.display_target.dbObj.id]
        self.ui.lineEdit_name.setText(self.target.name)
        self.ui.spinBox_hp.setValue(self.target.hp)
        self.ui.spinBox_initiative.setValue(self.target.initiative)
        self.ui.textEdit_description.setText(self.target.stat_block)
        self.ui.checkBox_initiative_alarm.setChecked(self.target.isAlarm)
        self.show()

    @db_session
    def update_isAlarm(self):
        dbObj = self.main.db.Active[self.target.id]
        ui_isAlarm = self.ui.checkBox_initiative_alarm
        dbObj.isAlarm = ui_isAlarm.isChecked()
        

    @db_session
    def update_name(self):
        name = self.ui.lineEdit_name.text()
        # require state from db. Pony implementation requires this.
        self.target = self.main.db.Active[self.target.id]
        self.target.name = name
        commit()
        self.main.update_encounter_text(self.display_target)


    @db_session
    def update_hp(self):
        if not self.suppress_spinbox_update:
            self.suppress_spinbox_update = True
            newHP = self.ui.spinBox_hp.value()
            dbObj = self.main.db.Active[self.target.id]
            if dbObj.count > 1:
               all_hp = dbObj.group_hp
               hp_sum = sum(all_hp)
               while hp_sum != newHP:
                   if hp_sum < newHP:
                       min_value = all_hp.index(min(all_hp))
                       value = all_hp.pop(min_value)
                       value += 1
                       hp_sum += 1
                       all_hp.append(value)
                   else:
                       max_value = all_hp.index(max(all_hp))
                       value = all_hp.pop(max_value)
                       value -= 1
                       hp_sum -= 1
                       all_hp.append(value)
               all_hp = [ hp for hp in all_hp if hp > 0 ]
               dbObj.count = len(all_hp)
               dbObj.group_hp = all_hp
            else:
                dbObj.hp = newHP
            if dbObj.max_hp < newHP:
                dbObj.max_hp = newHP
            commit()
            self.main.update_encounter_text(self.display_target)
            self.main.suppress_spinbox_update = True
            self.main.ui.spinBox_main_hp.setValue(newHP)
            self.main.suppress_spinbox_update = False
            self.suppress_spinbox_update = False


    @db_session
    def update_initiative(self):
        if not self.suppress_spinbox_update:
            self.suppress_spinbox_update = True
            init_value = self.ui.spinBox_initiative.value()
            self.target = self.main.db.Active[self.target.id]
            self.target.initiative = init_value
            commit()
            self.main.update_encounter_text(self.display_target)
            self.main.suppress_spinbox_update = True
            self.main.ui.spinBox_main_initiative.setValue(init_value)
            self.main.suppress_spinbox_update = False
            self.suppress_spinbox_update = False

    @db_session
    def update_description(self):
        text = self.ui.textEdit_description.toPlainText()
        # there is a race condition where this update gets called
        # immediatly when the first player ui is spawned. Not sure
        # why it does not happen for the other updates ^ ??
        if self.display_target:
            # reaquire state from db. Pony implementation requires this.
            dbObj = self.main.db.Active[self.target.id]
            dbObj.stat_block = text
            commit()
            self.main.update_encounter_text(self.display_target)

    @db_session
    def add_player(self):
        'adds a new entery to the initiative tracker'
        settings = self.main.db.Settings
        self.target = self.main.db.Active(player=True)
        commit()
        self.display_target = QListWidgetItem("{player.initiative} | {player.name} | hp:{player.hp}")
        self.display_target.dbObj = self.target
        self.main.update_encounter_text(self.display_target)
        self.main.ui.listWidget_Encounter.addItem(self.display_target)
        # clear ui for adding a new player
        self.ui.lineEdit_name.setText('')
        self.ui.lineEdit_name.setFocus()
        self.ui.spinBox_hp.setValue(1)
        self.ui.spinBox_initiative.setValue(1)

        pc_npc_templ = settings.get(name='pc_npc_template')
        if pc_npc_templ:
            self.ui.textEdit_description.setText(pc_npc_templ.value)
        else:    
            self.ui.textEdit_description.setText(self.main.ui_s.default_templ)
        self.show()

    @db_session
    def remove_player(self):
        # reaquire state from db. Pony implementation requires this.
        self.target = self.main.db.Active[self.target.id]
        self.target.delete()
        commit()
        index = self.main.ui.listWidget_Encounter.indexFromItem(self.display_target)
        self.main.ui.listWidget_Encounter.takeItem(index.row())
        self.close()
