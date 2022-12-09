# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_items.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QTreeView,
    QVBoxLayout, QWidget)

class Ui_template_Items(object):
    def setupUi(self, template_Items):
        if not template_Items.objectName():
            template_Items.setObjectName(u"template_Items")
        template_Items.resize(408, 498)
        self.verticalLayout = QVBoxLayout(template_Items)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(template_Items)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(template_Items)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(template_Items)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(template_Items)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(template_Items)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.textEdit = QTextEdit(template_Items)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.pushButton = QPushButton(template_Items)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.label_4 = QLabel(template_Items)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(template_Items)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.pushButton_2 = QPushButton(template_Items)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(template_Items)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.treeView = QTreeView(template_Items)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout.addWidget(self.treeView)


        self.retranslateUi(template_Items)

        QMetaObject.connectSlotsByName(template_Items)
    # setupUi

    def retranslateUi(self, template_Items):
        template_Items.setWindowTitle(QCoreApplication.translate("template_Items", u"Form", None))
        self.label.setText(QCoreApplication.translate("template_Items", u"Item Name", None))
        self.label_2.setText(QCoreApplication.translate("template_Items", u"Item Weight", None))
        self.label_3.setText(QCoreApplication.translate("template_Items", u"Description: %d for damage %e for elemental damage", None))
        self.pushButton.setText(QCoreApplication.translate("template_Items", u"Add roll table", None))
        self.label_4.setText(QCoreApplication.translate("template_Items", u"Roll table dice roll", None))
        self.pushButton_2.setText(QCoreApplication.translate("template_Items", u"Add roll table", None))
        self.pushButton_3.setText(QCoreApplication.translate("template_Items", u"Add random table", None))
    # retranslateUi

