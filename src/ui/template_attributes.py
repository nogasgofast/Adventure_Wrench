# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_attributes.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QTreeView,
    QWidget)

class Ui_template_attributes(object):
    def setupUi(self, template_attributes):
        if not template_attributes.objectName():
            template_attributes.setObjectName(u"template_attributes")
        template_attributes.resize(400, 526)
        self.formLayout = QFormLayout(template_attributes)
        self.formLayout.setObjectName(u"formLayout")
        self.label_name = QLabel(template_attributes)
        self.label_name.setObjectName(u"label_name")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_name)

        self.lineEdit_name = QLineEdit(template_attributes)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_name)

        self.label_description = QLabel(template_attributes)
        self.label_description.setObjectName(u"label_description")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_description)

        self.lineEdit_description = QLineEdit(template_attributes)
        self.lineEdit_description.setObjectName(u"lineEdit_description")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_description)

        self.pushButton_add = QPushButton(template_attributes)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.pushButton_add)

        self.lineEdit_dice_roll = QLineEdit(template_attributes)
        self.lineEdit_dice_roll.setObjectName(u"lineEdit_dice_roll")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.lineEdit_dice_roll)

        self.pushButton_roll_table = QPushButton(template_attributes)
        self.pushButton_roll_table.setObjectName(u"pushButton_roll_table")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.pushButton_roll_table)

        self.pushButton_random_table = QPushButton(template_attributes)
        self.pushButton_random_table.setObjectName(u"pushButton_random_table")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.pushButton_random_table)

        self.treeView = QTreeView(template_attributes)
        self.treeView.setObjectName(u"treeView")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.treeView)

        self.label_roll_table = QLabel(template_attributes)
        self.label_roll_table.setObjectName(u"label_roll_table")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.label_roll_table)

        self.pushButton_delete = QPushButton(template_attributes)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.pushButton_delete)


        self.retranslateUi(template_attributes)

        QMetaObject.connectSlotsByName(template_attributes)
    # setupUi

    def retranslateUi(self, template_attributes):
        template_attributes.setWindowTitle(QCoreApplication.translate("template_attributes", u"Form", None))
        self.label_name.setText(QCoreApplication.translate("template_attributes", u"Name", None))
        self.label_description.setText(QCoreApplication.translate("template_attributes", u"description (optional)", None))
        self.pushButton_add.setText(QCoreApplication.translate("template_attributes", u"Add", None))
        self.pushButton_roll_table.setText(QCoreApplication.translate("template_attributes", u"Add roll table", None))
        self.pushButton_random_table.setText(QCoreApplication.translate("template_attributes", u"Add random table", None))
        self.label_roll_table.setText(QCoreApplication.translate("template_attributes", u"Dice roll", None))
        self.pushButton_delete.setText(QCoreApplication.translate("template_attributes", u"Delete", None))
    # retranslateUi

