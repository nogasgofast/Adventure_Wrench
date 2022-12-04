# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Template_finder.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_template_finder(object):
    def setupUi(self, template_finder):
        if not template_finder.objectName():
            template_finder.setObjectName(u"template_finder")
        template_finder.setWindowModality(Qt.WindowModal)
        template_finder.resize(620, 441)
        self.verticalLayout = QVBoxLayout(template_finder)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(template_finder)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_search = QLineEdit(template_finder)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_search.sizePolicy().hasHeightForWidth())
        self.lineEdit_search.setSizePolicy(sizePolicy)
        self.lineEdit_search.setMaximumSize(QSize(452, 16777215))
        self.lineEdit_search.setBaseSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.lineEdit_search)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.pushButton = QPushButton(template_finder)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_4.addWidget(self.pushButton)

        self.listWidget_catagory = QListWidget(template_finder)
        self.listWidget_catagory.setObjectName(u"listWidget_catagory")
        self.listWidget_catagory.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_4.addWidget(self.listWidget_catagory)

        self.pushButton_create_example = QPushButton(template_finder)
        self.pushButton_create_example.setObjectName(u"pushButton_create_example")

        self.verticalLayout_4.addWidget(self.pushButton_create_example)


        self.verticalLayout.addLayout(self.verticalLayout_4)


        self.retranslateUi(template_finder)

        QMetaObject.connectSlotsByName(template_finder)
    # setupUi

    def retranslateUi(self, template_finder):
        template_finder.setWindowTitle(QCoreApplication.translate("template_finder", u"Form", None))
        self.label.setText(QCoreApplication.translate("template_finder", u"Templates:", None))
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("template_finder", u"Search", None))
        self.pushButton.setText(QCoreApplication.translate("template_finder", u"Create New Template", None))
        self.pushButton_create_example.setText(QCoreApplication.translate("template_finder", u"Apply Template", None))
    # retranslateUi

