# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_stats.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QTreeView,
    QWidget)

class Ui_template_stats(object):
    def setupUi(self, template_stats):
        if not template_stats.objectName():
            template_stats.setObjectName(u"template_stats")
        template_stats.resize(421, 536)
        self.formLayout = QFormLayout(template_stats)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(template_stats)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)

        self.lineEdit_2 = QLineEdit(template_stats)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.pushButton = QPushButton(template_stats)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pushButton)

        self.label_2 = QLabel(template_stats)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_2)

        self.lineEdit = QLineEdit(template_stats)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineEdit)

        self.pushButton_2 = QPushButton(template_stats)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.pushButton_2)

        self.pushButton_3 = QPushButton(template_stats)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.pushButton_3)

        self.treeView_2 = QTreeView(template_stats)
        self.treeView_2.setObjectName(u"treeView_2")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.treeView_2)


        self.retranslateUi(template_stats)

        QMetaObject.connectSlotsByName(template_stats)
    # setupUi

    def retranslateUi(self, template_stats):
        template_stats.setWindowTitle(QCoreApplication.translate("template_stats", u"Form", None))
        self.label.setText(QCoreApplication.translate("template_stats", u"Stat", None))
        self.pushButton.setText(QCoreApplication.translate("template_stats", u"Add", None))
        self.label_2.setText(QCoreApplication.translate("template_stats", u"Roll Table Dice Roll:", None))
        self.pushButton_2.setText(QCoreApplication.translate("template_stats", u"Add roll table", None))
        self.pushButton_3.setText(QCoreApplication.translate("template_stats", u"Add random table", None))
    # retranslateUi

