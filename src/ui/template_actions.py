# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_actions.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QTreeView, QWidget)

class Ui_template_actions(object):
    def setupUi(self, template_actions):
        if not template_actions.objectName():
            template_actions.setObjectName(u"template_actions")
        template_actions.resize(466, 590)
        self.formLayout = QFormLayout(template_actions)
        self.formLayout.setObjectName(u"formLayout")
        self.pushButton_random_table = QPushButton(template_actions)
        self.pushButton_random_table.setObjectName(u"pushButton_random_table")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.pushButton_random_table)

        self.label_name = QLabel(template_actions)
        self.label_name.setObjectName(u"label_name")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_name)

        self.lineEdit_name = QLineEdit(template_actions)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_name)

        self.label_description = QLabel(template_actions)
        self.label_description.setObjectName(u"label_description")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_description)

        self.textEdit_description = QTextEdit(template_actions)
        self.textEdit_description.setObjectName(u"textEdit_description")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.textEdit_description)

        self.pushButton_add = QPushButton(template_actions)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.pushButton_add)

        self.label_dice_roll = QLabel(template_actions)
        self.label_dice_roll.setObjectName(u"label_dice_roll")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_dice_roll)

        self.lineEdit_dice_roll = QLineEdit(template_actions)
        self.lineEdit_dice_roll.setObjectName(u"lineEdit_dice_roll")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_dice_roll)

        self.pushButton_roll_table = QPushButton(template_actions)
        self.pushButton_roll_table.setObjectName(u"pushButton_roll_table")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.pushButton_roll_table)

        self.treeView = QTreeView(template_actions)
        self.treeView.setObjectName(u"treeView")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.treeView)

        self.pushButton_delete = QPushButton(template_actions)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.pushButton_delete)


        self.retranslateUi(template_actions)

        QMetaObject.connectSlotsByName(template_actions)
    # setupUi

    def retranslateUi(self, template_actions):
        template_actions.setWindowTitle(QCoreApplication.translate("template_actions", u"Form", None))
        self.pushButton_random_table.setText(QCoreApplication.translate("template_actions", u"Add random table", None))
        self.label_name.setText(QCoreApplication.translate("template_actions", u"Name", None))
        self.label_description.setText(QCoreApplication.translate("template_actions", u"Description: %d, %e for auto damage and elemental damage", None))
        self.pushButton_add.setText(QCoreApplication.translate("template_actions", u"Add", None))
        self.label_dice_roll.setText(QCoreApplication.translate("template_actions", u"dice roll", None))
        self.pushButton_roll_table.setText(QCoreApplication.translate("template_actions", u"Add roll table", None))
        self.pushButton_delete.setText(QCoreApplication.translate("template_actions", u"Delete", None))
    # retranslateUi

