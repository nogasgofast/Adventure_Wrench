# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TheShop_Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
    QSpinBox, QTextEdit, QVBoxLayout, QWidget)

class Ui_TheShop(object):
    def setupUi(self, TheShop):
        if not TheShop.objectName():
            TheShop.setObjectName(u"TheShop")
        TheShop.resize(898, 586)
        TheShop.setStyleSheet(u"QWidget {\n"
"  color: black;\n"
"  background-color: rgb(89, 92, 123);\n"
"}\n"
"\n"
"QListWidget QTreeWidget{\n"
"   color: #000;\n"
"   selection-color: #FFF;\n"
"   selection-background-color: #55A;\n"
"}\n"
"\n"
"QListWidget::item:selected:!active{\n"
"   color: #000;\n"
"   selection-color: #FFF;\n"
"   selection-background-color: #55A;\n"
"}\n"
"\n"
"QTreeWidget::item:selected:!active{\n"
"   color: #000;\n"
"   selection-color: #FFF;\n"
"   selection-background-color: #55A;\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	border: 5px solid orange;\n"
"	background-color: #39537d;\n"
"    color: #FFF;\n"
"}\n"
"\n"
"QLabel {\n"
"color: rgb(222, 221, 218);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: rgb(75, 82, 143);\n"
"color: white;\n"
"}")
        TheShop.setModal(False)
        self.horizontalLayout_2 = QHBoxLayout(TheShop)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_shop = QVBoxLayout()
        self.verticalLayout_shop.setObjectName(u"verticalLayout_shop")
        self.groupBox_shop = QGroupBox(TheShop)
        self.groupBox_shop.setObjectName(u"groupBox_shop")
        self.groupBox_shop.setFlat(True)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_shop)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_name = QHBoxLayout()
        self.horizontalLayout_name.setObjectName(u"horizontalLayout_name")
        self.label_name = QLabel(self.groupBox_shop)
        self.label_name.setObjectName(u"label_name")

        self.horizontalLayout_name.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.groupBox_shop)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.horizontalLayout_name.addWidget(self.lineEdit_name)


        self.verticalLayout_2.addLayout(self.horizontalLayout_name)

        self.horizontalLayout_cr = QHBoxLayout()
        self.horizontalLayout_cr.setObjectName(u"horizontalLayout_cr")
        self.label_target_cr = QLabel(self.groupBox_shop)
        self.label_target_cr.setObjectName(u"label_target_cr")

        self.horizontalLayout_cr.addWidget(self.label_target_cr)

        self.spinBox_cr = QSpinBox(self.groupBox_shop)
        self.spinBox_cr.setObjectName(u"spinBox_cr")
        self.spinBox_cr.setMinimum(1)
        self.spinBox_cr.setMaximum(999)
        self.spinBox_cr.setValue(1)

        self.horizontalLayout_cr.addWidget(self.spinBox_cr)

        self.horizontalLayout_group_of = QHBoxLayout()
        self.horizontalLayout_group_of.setObjectName(u"horizontalLayout_group_of")
        self.label_group_of = QLabel(self.groupBox_shop)
        self.label_group_of.setObjectName(u"label_group_of")

        self.horizontalLayout_group_of.addWidget(self.label_group_of)

        self.spinBox_group_of = QSpinBox(self.groupBox_shop)
        self.spinBox_group_of.setObjectName(u"spinBox_group_of")
        self.spinBox_group_of.setMinimum(1)
        self.spinBox_group_of.setMaximum(999)
        self.spinBox_group_of.setValue(1)

        self.horizontalLayout_group_of.addWidget(self.spinBox_group_of)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_group_of.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_cr.addLayout(self.horizontalLayout_group_of)


        self.verticalLayout_2.addLayout(self.horizontalLayout_cr)

        self.pushButton_roll_stats = QPushButton(self.groupBox_shop)
        self.pushButton_roll_stats.setObjectName(u"pushButton_roll_stats")
        self.pushButton_roll_stats.setAutoDefault(False)

        self.verticalLayout_2.addWidget(self.pushButton_roll_stats)

        self.horizontalLayout_stats_shop = QHBoxLayout()
        self.horizontalLayout_stats_shop.setObjectName(u"horizontalLayout_stats_shop")
        self.verticalLayout_str = QVBoxLayout()
        self.verticalLayout_str.setObjectName(u"verticalLayout_str")
        self.label_STR = QLabel(self.groupBox_shop)
        self.label_STR.setObjectName(u"label_STR")
        self.label_STR.setEnabled(True)

        self.verticalLayout_str.addWidget(self.label_STR)

        self.spinBox_STR = QSpinBox(self.groupBox_shop)
        self.spinBox_STR.setObjectName(u"spinBox_STR")
        self.spinBox_STR.setMaximum(30)
        self.spinBox_STR.setValue(10)

        self.verticalLayout_str.addWidget(self.spinBox_STR)


        self.horizontalLayout_stats_shop.addLayout(self.verticalLayout_str)

        self.verticalLayout_dex = QVBoxLayout()
        self.verticalLayout_dex.setObjectName(u"verticalLayout_dex")
        self.label_DEX = QLabel(self.groupBox_shop)
        self.label_DEX.setObjectName(u"label_DEX")

        self.verticalLayout_dex.addWidget(self.label_DEX)

        self.spinBox_DEX = QSpinBox(self.groupBox_shop)
        self.spinBox_DEX.setObjectName(u"spinBox_DEX")
        self.spinBox_DEX.setMaximum(30)
        self.spinBox_DEX.setValue(10)

        self.verticalLayout_dex.addWidget(self.spinBox_DEX)


        self.horizontalLayout_stats_shop.addLayout(self.verticalLayout_dex)

        self.verticalLayout_con = QVBoxLayout()
        self.verticalLayout_con.setObjectName(u"verticalLayout_con")
        self.label_CON = QLabel(self.groupBox_shop)
        self.label_CON.setObjectName(u"label_CON")

        self.verticalLayout_con.addWidget(self.label_CON)

        self.spinBox_CON = QSpinBox(self.groupBox_shop)
        self.spinBox_CON.setObjectName(u"spinBox_CON")
        self.spinBox_CON.setMaximum(30)
        self.spinBox_CON.setValue(10)

        self.verticalLayout_con.addWidget(self.spinBox_CON)


        self.horizontalLayout_stats_shop.addLayout(self.verticalLayout_con)

        self.verticalLayout_int = QVBoxLayout()
        self.verticalLayout_int.setObjectName(u"verticalLayout_int")
        self.label_INT = QLabel(self.groupBox_shop)
        self.label_INT.setObjectName(u"label_INT")

        self.verticalLayout_int.addWidget(self.label_INT)

        self.spinBox_INT = QSpinBox(self.groupBox_shop)
        self.spinBox_INT.setObjectName(u"spinBox_INT")
        self.spinBox_INT.setMaximum(30)
        self.spinBox_INT.setValue(10)

        self.verticalLayout_int.addWidget(self.spinBox_INT)


        self.horizontalLayout_stats_shop.addLayout(self.verticalLayout_int)

        self.verticalLayout_wis = QVBoxLayout()
        self.verticalLayout_wis.setObjectName(u"verticalLayout_wis")
        self.label_WIS = QLabel(self.groupBox_shop)
        self.label_WIS.setObjectName(u"label_WIS")

        self.verticalLayout_wis.addWidget(self.label_WIS)

        self.spinBox_WIS = QSpinBox(self.groupBox_shop)
        self.spinBox_WIS.setObjectName(u"spinBox_WIS")
        self.spinBox_WIS.setMaximum(30)
        self.spinBox_WIS.setValue(10)

        self.verticalLayout_wis.addWidget(self.spinBox_WIS)


        self.horizontalLayout_stats_shop.addLayout(self.verticalLayout_wis)

        self.verticalLayout_cha = QVBoxLayout()
        self.verticalLayout_cha.setObjectName(u"verticalLayout_cha")
        self.label_CHA = QLabel(self.groupBox_shop)
        self.label_CHA.setObjectName(u"label_CHA")

        self.verticalLayout_cha.addWidget(self.label_CHA)

        self.spinBox_CHA = QSpinBox(self.groupBox_shop)
        self.spinBox_CHA.setObjectName(u"spinBox_CHA")
        self.spinBox_CHA.setMaximum(30)
        self.spinBox_CHA.setValue(10)

        self.verticalLayout_cha.addWidget(self.spinBox_CHA)


        self.horizontalLayout_stats_shop.addLayout(self.verticalLayout_cha)


        self.verticalLayout_2.addLayout(self.horizontalLayout_stats_shop)

        self.horizontalLayout_display = QHBoxLayout()
        self.horizontalLayout_display.setObjectName(u"horizontalLayout_display")
        self.verticalLayout_display_template = QVBoxLayout()
        self.verticalLayout_display_template.setObjectName(u"verticalLayout_display_template")
        self.label_display_templates = QLabel(self.groupBox_shop)
        self.label_display_templates.setObjectName(u"label_display_templates")

        self.verticalLayout_display_template.addWidget(self.label_display_templates)

        self.pushButton_reset_stat_block = QPushButton(self.groupBox_shop)
        self.pushButton_reset_stat_block.setObjectName(u"pushButton_reset_stat_block")
        self.pushButton_reset_stat_block.setAutoDefault(False)

        self.verticalLayout_display_template.addWidget(self.pushButton_reset_stat_block)

        self.textEdit_stat_block = QTextEdit(self.groupBox_shop)
        self.textEdit_stat_block.setObjectName(u"textEdit_stat_block")
        self.textEdit_stat_block.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_display_template.addWidget(self.textEdit_stat_block)


        self.horizontalLayout_display.addLayout(self.verticalLayout_display_template)


        self.verticalLayout_2.addLayout(self.horizontalLayout_display)


        self.verticalLayout_shop.addWidget(self.groupBox_shop)

        self.horizontalLayout_back = QHBoxLayout()
        self.horizontalLayout_back.setObjectName(u"horizontalLayout_back")
        self.pushButton_back = QPushButton(TheShop)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setAutoDefault(False)

        self.horizontalLayout_back.addWidget(self.pushButton_back)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_back.addItem(self.horizontalSpacer_2)

        self.pushButton_delete_shop = QPushButton(TheShop)
        self.pushButton_delete_shop.setObjectName(u"pushButton_delete_shop")
        self.pushButton_delete_shop.setAutoDefault(False)

        self.horizontalLayout_back.addWidget(self.pushButton_delete_shop)


        self.verticalLayout_shop.addLayout(self.horizontalLayout_back)


        self.horizontalLayout_2.addLayout(self.verticalLayout_shop)

        self.groupBox_templates = QGroupBox(TheShop)
        self.groupBox_templates.setObjectName(u"groupBox_templates")
        self.groupBox_templates.setFlat(True)
        self.verticalLayout = QVBoxLayout(self.groupBox_templates)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBox_selector_templates = QComboBox(self.groupBox_templates)
        self.comboBox_selector_templates.setObjectName(u"comboBox_selector_templates")

        self.verticalLayout.addWidget(self.comboBox_selector_templates)

        self.pushButton_add_templates = QPushButton(self.groupBox_templates)
        self.pushButton_add_templates.setObjectName(u"pushButton_add_templates")
        self.pushButton_add_templates.setAutoDefault(False)

        self.verticalLayout.addWidget(self.pushButton_add_templates)

        self.label_templates = QLabel(self.groupBox_templates)
        self.label_templates.setObjectName(u"label_templates")

        self.verticalLayout.addWidget(self.label_templates)

        self.listWidget_templates = QListWidget(self.groupBox_templates)
        self.listWidget_templates.setObjectName(u"listWidget_templates")
        self.listWidget_templates.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.listWidget_templates)

        self.pushButton_remove_templates = QPushButton(self.groupBox_templates)
        self.pushButton_remove_templates.setObjectName(u"pushButton_remove_templates")
        self.pushButton_remove_templates.setAutoDefault(False)

        self.verticalLayout.addWidget(self.pushButton_remove_templates)


        self.horizontalLayout_2.addWidget(self.groupBox_templates)


        self.retranslateUi(TheShop)

        QMetaObject.connectSlotsByName(TheShop)
    # setupUi

    def retranslateUi(self, TheShop):
        TheShop.setWindowTitle(QCoreApplication.translate("TheShop", u"The Shop", None))
        self.groupBox_shop.setTitle(QCoreApplication.translate("TheShop", u"Vault Item:", None))
        self.label_name.setText(QCoreApplication.translate("TheShop", u"What is it?", None))
        self.lineEdit_name.setInputMask("")
        self.lineEdit_name.setText(QCoreApplication.translate("TheShop", u"*new vault item*", None))
        self.lineEdit_name.setPlaceholderText(QCoreApplication.translate("TheShop", u"***", None))
        self.label_target_cr.setText(QCoreApplication.translate("TheShop", u"Challange rating:", None))
        self.label_group_of.setText(QCoreApplication.translate("TheShop", u"Group of:", None))
        self.pushButton_roll_stats.setText(QCoreApplication.translate("TheShop", u"Re-roll Stats", None))
        self.label_STR.setText(QCoreApplication.translate("TheShop", u"STR", None))
        self.label_DEX.setText(QCoreApplication.translate("TheShop", u"DEX", None))
        self.label_CON.setText(QCoreApplication.translate("TheShop", u"CON", None))
        self.label_INT.setText(QCoreApplication.translate("TheShop", u"INT", None))
        self.label_WIS.setText(QCoreApplication.translate("TheShop", u"WIS", None))
        self.label_CHA.setText(QCoreApplication.translate("TheShop", u"CHA", None))
        self.label_display_templates.setText(QCoreApplication.translate("TheShop", u"Stat block", None))
        self.pushButton_reset_stat_block.setText(QCoreApplication.translate("TheShop", u"Re-Roll templates", None))
#if QT_CONFIG(tooltip)
        self.textEdit_stat_block.setToolTip(QCoreApplication.translate("TheShop", u"<html><head/><body><p>This box gets over-written by the controlls on this page. If you make changes here, make sure it's the only thing, or the last thing you do on this page. Even after you save it.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_back.setText(QCoreApplication.translate("TheShop", u"<- Save (Esc)", None))
        self.pushButton_delete_shop.setText(QCoreApplication.translate("TheShop", u"Delete from vault", None))
        self.groupBox_templates.setTitle(QCoreApplication.translate("TheShop", u"Templates", None))
#if QT_CONFIG(tooltip)
        self.comboBox_selector_templates.setToolTip(QCoreApplication.translate("TheShop", u"Templates are created in The Acadamy. Navigate there from the Vault.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_add_templates.setText(QCoreApplication.translate("TheShop", u"Add", None))
        self.label_templates.setText(QCoreApplication.translate("TheShop", u"Applied templates", None))
        self.pushButton_remove_templates.setText(QCoreApplication.translate("TheShop", u"Remove template", None))
    # retranslateUi

