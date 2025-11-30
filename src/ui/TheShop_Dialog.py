# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TheShop_Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
    QTextEdit, QVBoxLayout, QWidget)

class Ui_TheShop(object):
    def setupUi(self, TheShop):
        if not TheShop.objectName():
            TheShop.setObjectName(u"TheShop")
        TheShop.resize(898, 586)
        TheShop.setStyleSheet(u"")
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

