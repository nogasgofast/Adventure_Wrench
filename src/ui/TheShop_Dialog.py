# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TheShop_Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_TheShop(object):
    def setupUi(self, TheShop):
        if not TheShop.objectName():
            TheShop.setObjectName(u"TheShop")
        TheShop.resize(898, 586)
        TheShop.setStyleSheet(u"QpushButton { margin: 0,0,0,25 px; }")
        TheShop.setModal(False)
        self.horizontalLayout_2 = QHBoxLayout(TheShop)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_main = QVBoxLayout()
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.horizontalLayout_name = QHBoxLayout()
        self.horizontalLayout_name.setObjectName(u"horizontalLayout_name")
        self.label_name = QLabel(TheShop)
        self.label_name.setObjectName(u"label_name")

        self.horizontalLayout_name.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(TheShop)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.horizontalLayout_name.addWidget(self.lineEdit_name)


        self.verticalLayout_main.addLayout(self.horizontalLayout_name)

        self.horizontallayout_type = QHBoxLayout()
        self.horizontallayout_type.setObjectName(u"horizontallayout_type")
        self.label_type = QLabel(TheShop)
        self.label_type.setObjectName(u"label_type")

        self.horizontallayout_type.addWidget(self.label_type)

        self.comboBox_type = QComboBox(TheShop)
        self.comboBox_type.setObjectName(u"comboBox_type")
        self.comboBox_type.setEditable(True)

        self.horizontallayout_type.addWidget(self.comboBox_type)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontallayout_type.addItem(self.horizontalSpacer)


        self.verticalLayout_main.addLayout(self.horizontallayout_type)

        self.horizontalLayout_group_of = QHBoxLayout()
        self.horizontalLayout_group_of.setObjectName(u"horizontalLayout_group_of")
        self.label_group_of = QLabel(TheShop)
        self.label_group_of.setObjectName(u"label_group_of")

        self.horizontalLayout_group_of.addWidget(self.label_group_of)

        self.spinBox_group_of = QSpinBox(TheShop)
        self.spinBox_group_of.setObjectName(u"spinBox_group_of")
        self.spinBox_group_of.setValue(1)

        self.horizontalLayout_group_of.addWidget(self.spinBox_group_of)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_group_of.addItem(self.horizontalSpacer_5)


        self.verticalLayout_main.addLayout(self.horizontalLayout_group_of)

        self.horizontalLayout_cr = QHBoxLayout()
        self.horizontalLayout_cr.setObjectName(u"horizontalLayout_cr")
        self.label_target_cr = QLabel(TheShop)
        self.label_target_cr.setObjectName(u"label_target_cr")

        self.horizontalLayout_cr.addWidget(self.label_target_cr)

        self.spinBox_cr = QSpinBox(TheShop)
        self.spinBox_cr.setObjectName(u"spinBox_cr")
        self.spinBox_cr.setMaximum(30)
        self.spinBox_cr.setValue(10)

        self.horizontalLayout_cr.addWidget(self.spinBox_cr)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_cr.addItem(self.horizontalSpacer_6)


        self.verticalLayout_main.addLayout(self.horizontalLayout_cr)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_main.addItem(self.verticalSpacer)

        self.groupBox_base_ability_score = QGroupBox(TheShop)
        self.groupBox_base_ability_score.setObjectName(u"groupBox_base_ability_score")
        self.groupBox_base_ability_score.setFlat(True)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_base_ability_score)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_base_stats = QHBoxLayout()
        self.horizontalLayout_base_stats.setObjectName(u"horizontalLayout_base_stats")
        self.verticalLayout_str = QVBoxLayout()
        self.verticalLayout_str.setObjectName(u"verticalLayout_str")
        self.label_STR = QLabel(self.groupBox_base_ability_score)
        self.label_STR.setObjectName(u"label_STR")
        self.label_STR.setEnabled(True)

        self.verticalLayout_str.addWidget(self.label_STR)

        self.spinBox_STR = QSpinBox(self.groupBox_base_ability_score)
        self.spinBox_STR.setObjectName(u"spinBox_STR")
        self.spinBox_STR.setMaximum(30)
        self.spinBox_STR.setValue(10)

        self.verticalLayout_str.addWidget(self.spinBox_STR)


        self.horizontalLayout_base_stats.addLayout(self.verticalLayout_str)

        self.verticalLayout_dex = QVBoxLayout()
        self.verticalLayout_dex.setObjectName(u"verticalLayout_dex")
        self.label_DEX = QLabel(self.groupBox_base_ability_score)
        self.label_DEX.setObjectName(u"label_DEX")

        self.verticalLayout_dex.addWidget(self.label_DEX)

        self.spinBox_DEX = QSpinBox(self.groupBox_base_ability_score)
        self.spinBox_DEX.setObjectName(u"spinBox_DEX")
        self.spinBox_DEX.setMaximum(30)
        self.spinBox_DEX.setValue(10)

        self.verticalLayout_dex.addWidget(self.spinBox_DEX)


        self.horizontalLayout_base_stats.addLayout(self.verticalLayout_dex)

        self.verticalLayout_con = QVBoxLayout()
        self.verticalLayout_con.setObjectName(u"verticalLayout_con")
        self.label_CON = QLabel(self.groupBox_base_ability_score)
        self.label_CON.setObjectName(u"label_CON")

        self.verticalLayout_con.addWidget(self.label_CON)

        self.spinBox_CON = QSpinBox(self.groupBox_base_ability_score)
        self.spinBox_CON.setObjectName(u"spinBox_CON")
        self.spinBox_CON.setMaximum(30)
        self.spinBox_CON.setValue(10)

        self.verticalLayout_con.addWidget(self.spinBox_CON)


        self.horizontalLayout_base_stats.addLayout(self.verticalLayout_con)

        self.verticalLayout_int = QVBoxLayout()
        self.verticalLayout_int.setObjectName(u"verticalLayout_int")
        self.label_INT = QLabel(self.groupBox_base_ability_score)
        self.label_INT.setObjectName(u"label_INT")

        self.verticalLayout_int.addWidget(self.label_INT)

        self.spinBox_INT = QSpinBox(self.groupBox_base_ability_score)
        self.spinBox_INT.setObjectName(u"spinBox_INT")
        self.spinBox_INT.setMaximum(30)
        self.spinBox_INT.setValue(10)

        self.verticalLayout_int.addWidget(self.spinBox_INT)


        self.horizontalLayout_base_stats.addLayout(self.verticalLayout_int)

        self.verticalLayout_wis = QVBoxLayout()
        self.verticalLayout_wis.setObjectName(u"verticalLayout_wis")
        self.label_WIS = QLabel(self.groupBox_base_ability_score)
        self.label_WIS.setObjectName(u"label_WIS")

        self.verticalLayout_wis.addWidget(self.label_WIS)

        self.spinBox_WIS = QSpinBox(self.groupBox_base_ability_score)
        self.spinBox_WIS.setObjectName(u"spinBox_WIS")
        self.spinBox_WIS.setMaximum(30)
        self.spinBox_WIS.setValue(10)

        self.verticalLayout_wis.addWidget(self.spinBox_WIS)


        self.horizontalLayout_base_stats.addLayout(self.verticalLayout_wis)

        self.verticalLayout_cha = QVBoxLayout()
        self.verticalLayout_cha.setObjectName(u"verticalLayout_cha")
        self.label_CHA = QLabel(self.groupBox_base_ability_score)
        self.label_CHA.setObjectName(u"label_CHA")

        self.verticalLayout_cha.addWidget(self.label_CHA)

        self.spinBox_CHA = QSpinBox(self.groupBox_base_ability_score)
        self.spinBox_CHA.setObjectName(u"spinBox_CHA")
        self.spinBox_CHA.setMaximum(30)
        self.spinBox_CHA.setValue(10)

        self.verticalLayout_cha.addWidget(self.spinBox_CHA)


        self.horizontalLayout_base_stats.addLayout(self.verticalLayout_cha)


        self.verticalLayout_2.addLayout(self.horizontalLayout_base_stats)

        self.horizontalLayout_update = QHBoxLayout()
        self.horizontalLayout_update.setObjectName(u"horizontalLayout_update")
        self.pushButton_update = QPushButton(self.groupBox_base_ability_score)
        self.pushButton_update.setObjectName(u"pushButton_update")

        self.horizontalLayout_update.addWidget(self.pushButton_update)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_update.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_update)


        self.verticalLayout_main.addWidget(self.groupBox_base_ability_score)

        self.groupBox = QGroupBox(TheShop)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFlat(True)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_template = QHBoxLayout()
        self.horizontalLayout_template.setObjectName(u"horizontalLayout_template")
        self.verticalLayout_abilities = QVBoxLayout()
        self.verticalLayout_abilities.setObjectName(u"verticalLayout_abilities")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.verticalLayout_abilities.addWidget(self.label)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_abilities.addWidget(self.comboBox)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_abilities.addWidget(self.pushButton_2)


        self.horizontalLayout_template.addLayout(self.verticalLayout_abilities)

        self.verticalLayout_stats_template = QVBoxLayout()
        self.verticalLayout_stats_template.setObjectName(u"verticalLayout_stats_template")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_stats_template.addWidget(self.label_4)

        self.comboBox_4 = QComboBox(self.groupBox)
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.verticalLayout_stats_template.addWidget(self.comboBox_4)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_stats_template.addWidget(self.pushButton_3)


        self.horizontalLayout_template.addLayout(self.verticalLayout_stats_template)

        self.verticalLayout_description_template = QVBoxLayout()
        self.verticalLayout_description_template.setObjectName(u"verticalLayout_description_template")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_description_template.addWidget(self.label_2)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_description_template.addWidget(self.comboBox_2)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_description_template.addWidget(self.pushButton_4)


        self.horizontalLayout_template.addLayout(self.verticalLayout_description_template)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.comboBox_3 = QComboBox(self.groupBox)
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.verticalLayout.addWidget(self.comboBox_3)

        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)


        self.horizontalLayout_template.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.comboBox_5 = QComboBox(self.groupBox)
        self.comboBox_5.setObjectName(u"comboBox_5")

        self.verticalLayout_3.addWidget(self.comboBox_5)

        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.horizontalLayout_template.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addLayout(self.horizontalLayout_template)


        self.verticalLayout_main.addWidget(self.groupBox)

        self.horizontalLayout_display = QHBoxLayout()
        self.horizontalLayout_display.setObjectName(u"horizontalLayout_display")
        self.verticalLayout_display_template = QVBoxLayout()
        self.verticalLayout_display_template.setObjectName(u"verticalLayout_display_template")
        self.label_display_templates = QLabel(TheShop)
        self.label_display_templates.setObjectName(u"label_display_templates")

        self.verticalLayout_display_template.addWidget(self.label_display_templates)

        self.listWidget_display_stat_block = QListWidget(TheShop)
        self.listWidget_display_stat_block.setObjectName(u"listWidget_display_stat_block")

        self.verticalLayout_display_template.addWidget(self.listWidget_display_stat_block)


        self.horizontalLayout_display.addLayout(self.verticalLayout_display_template)

        self.verticalLayout_stat_block = QVBoxLayout()
        self.verticalLayout_stat_block.setObjectName(u"verticalLayout_stat_block")
        self.label_display_stat_block = QLabel(TheShop)
        self.label_display_stat_block.setObjectName(u"label_display_stat_block")

        self.verticalLayout_stat_block.addWidget(self.label_display_stat_block)

        self.listWidget_display_templates = QListWidget(TheShop)
        self.listWidget_display_templates.setObjectName(u"listWidget_display_templates")

        self.verticalLayout_stat_block.addWidget(self.listWidget_display_templates)


        self.horizontalLayout_display.addLayout(self.verticalLayout_stat_block)


        self.verticalLayout_main.addLayout(self.horizontalLayout_display)

        self.horizontalLayout_back = QHBoxLayout()
        self.horizontalLayout_back.setObjectName(u"horizontalLayout_back")
        self.pushButton_back = QPushButton(TheShop)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.horizontalLayout_back.addWidget(self.pushButton_back)

        self.pushButton = QPushButton(TheShop)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_back.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_back.addItem(self.horizontalSpacer_2)


        self.verticalLayout_main.addLayout(self.horizontalLayout_back)


        self.horizontalLayout_2.addLayout(self.verticalLayout_main)


        self.retranslateUi(TheShop)

        QMetaObject.connectSlotsByName(TheShop)
    # setupUi

    def retranslateUi(self, TheShop):
        TheShop.setWindowTitle(QCoreApplication.translate("TheShop", u"The Shop", None))
        self.label_name.setText(QCoreApplication.translate("TheShop", u"Name:", None))
        self.lineEdit_name.setInputMask("")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("TheShop", u"***", None))
        self.label_type.setText(QCoreApplication.translate("TheShop", u"Type:", None))
        self.label_group_of.setText(QCoreApplication.translate("TheShop", u"Group of:", None))
        self.label_target_cr.setText(QCoreApplication.translate("TheShop", u"TARGET CR:", None))
        self.groupBox_base_ability_score.setTitle(QCoreApplication.translate("TheShop", u"Base Ability Scrore", None))
        self.label_STR.setText(QCoreApplication.translate("TheShop", u"STR", None))
        self.label_DEX.setText(QCoreApplication.translate("TheShop", u"DEX", None))
        self.label_CON.setText(QCoreApplication.translate("TheShop", u"CON", None))
        self.label_INT.setText(QCoreApplication.translate("TheShop", u"INT", None))
        self.label_WIS.setText(QCoreApplication.translate("TheShop", u"WIS", None))
        self.label_CHA.setText(QCoreApplication.translate("TheShop", u"CHA", None))
        self.pushButton_update.setText(QCoreApplication.translate("TheShop", u"Save Stats", None))
        self.groupBox.setTitle(QCoreApplication.translate("TheShop", u"Templates", None))
        self.label.setText(QCoreApplication.translate("TheShop", u"Abilities", None))
        self.pushButton_2.setText(QCoreApplication.translate("TheShop", u"Add", None))
        self.label_4.setText(QCoreApplication.translate("TheShop", u"Stats", None))
        self.pushButton_3.setText(QCoreApplication.translate("TheShop", u"Add", None))
        self.label_2.setText(QCoreApplication.translate("TheShop", u"Descriptions", None))
        self.pushButton_4.setText(QCoreApplication.translate("TheShop", u"Add", None))
        self.label_3.setText(QCoreApplication.translate("TheShop", u"Items", None))
        self.pushButton_5.setText(QCoreApplication.translate("TheShop", u"Add", None))
        self.label_5.setText(QCoreApplication.translate("TheShop", u"Actions", None))
        self.pushButton_6.setText(QCoreApplication.translate("TheShop", u"Add", None))
        self.label_display_templates.setText(QCoreApplication.translate("TheShop", u"Resulting stat block", None))
        self.label_display_stat_block.setText(QCoreApplication.translate("TheShop", u"Added Templates", None))
        self.pushButton_back.setText(QCoreApplication.translate("TheShop", u"Back (Esc)", None))
        self.pushButton.setText(QCoreApplication.translate("TheShop", u"Delete", None))
    # retranslateUi

