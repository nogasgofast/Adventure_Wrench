# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_descriptions.ui'
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

class Ui_Descriptions(object):
    def setupUi(self, Descriptions):
        if not Descriptions.objectName():
            Descriptions.setObjectName(u"Descriptions")
        Descriptions.resize(373, 408)
        self.formLayout = QFormLayout(Descriptions)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Descriptions)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label)

        self.lineEdit = QLineEdit(Descriptions)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit)

        self.pushButton = QPushButton(Descriptions)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.pushButton)

        self.pushButton_2 = QPushButton(Descriptions)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.pushButton_2)

        self.lineEdit_2 = QLineEdit(Descriptions)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lineEdit_2)

        self.treeView = QTreeView(Descriptions)
        self.treeView.setObjectName(u"treeView")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.treeView)

        self.label_2 = QLabel(Descriptions)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_2)

        self.pushButton_3 = QPushButton(Descriptions)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pushButton_3)


        self.retranslateUi(Descriptions)

        QMetaObject.connectSlotsByName(Descriptions)
    # setupUi

    def retranslateUi(self, Descriptions):
        Descriptions.setWindowTitle(QCoreApplication.translate("Descriptions", u"Form", None))
        self.label.setText(QCoreApplication.translate("Descriptions", u"Description", None))
        self.pushButton.setText(QCoreApplication.translate("Descriptions", u"Add", None))
        self.pushButton_2.setText(QCoreApplication.translate("Descriptions", u"Add Roll Table", None))
        self.label_2.setText(QCoreApplication.translate("Descriptions", u"Roll Table Dice Roll:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Descriptions", u"Add Random Table", None))
    # retranslateUi

