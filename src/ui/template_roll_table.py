# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_roll_table.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(554, 594)
        self.formLayout = QFormLayout(Form)
        self.formLayout.setObjectName(u"formLayout")
        self.label_range = QLabel(Form)
        self.label_range.setObjectName(u"label_range")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_range)

        self.label_parent_dice_roll = QLabel(Form)
        self.label_parent_dice_roll.setObjectName(u"label_parent_dice_roll")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_parent_dice_roll)

        self.lineEdit_parent_dice_roll = QLineEdit(Form)
        self.lineEdit_parent_dice_roll.setObjectName(u"lineEdit_parent_dice_roll")
        self.lineEdit_parent_dice_roll.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_parent_dice_roll)

        self.lineEdit_range = QLineEdit(Form)
        self.lineEdit_range.setObjectName(u"lineEdit_range")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_range)

        self.pushButton_add = QPushButton(Form)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.pushButton_add)

        self.treeView = QTreeView(Form)
        self.treeView.setObjectName(u"treeView")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.treeView)

        self.pushButton_delete = QPushButton(Form)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.pushButton_delete)

        self.label_description = QLabel(Form)
        self.label_description.setObjectName(u"label_description")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_description)

        self.textEdit_description = QTextEdit(Form)
        self.textEdit_description.setObjectName(u"textEdit_description")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.textEdit_description)

        self.label_dice_roll = QLabel(Form)
        self.label_dice_roll.setObjectName(u"label_dice_roll")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_dice_roll)

        self.lineEdit_dice_roll = QLineEdit(Form)
        self.lineEdit_dice_roll.setObjectName(u"lineEdit_dice_roll")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.lineEdit_dice_roll)

        self.pushButton_dice_roll = QPushButton(Form)
        self.pushButton_dice_roll.setObjectName(u"pushButton_dice_roll")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.pushButton_dice_roll)

        self.pushButton_random_table = QPushButton(Form)
        self.pushButton_random_table.setObjectName(u"pushButton_random_table")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.pushButton_random_table)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_range.setText(QCoreApplication.translate("Form", u"Range: written 5-10 or 20 subtituting your own numbers of coarse.", None))
        self.label_parent_dice_roll.setText(QCoreApplication.translate("Form", u"Parent dice roll", None))
        self.pushButton_add.setText(QCoreApplication.translate("Form", u"Add", None))
        self.pushButton_delete.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.label_description.setText(QCoreApplication.translate("Form", u"Description", None))
        self.label_dice_roll.setText(QCoreApplication.translate("Form", u"dice roll", None))
        self.pushButton_dice_roll.setText(QCoreApplication.translate("Form", u"Add roll table", None))
        self.pushButton_random_table.setText(QCoreApplication.translate("Form", u"Add random table", None))
    # retranslateUi

