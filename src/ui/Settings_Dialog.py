# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings_Dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.setWindowModality(Qt.WindowModal)
        Settings.resize(624, 443)
        Settings.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Settings)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_TemplateEdit = QLabel(Settings)
        self.label_TemplateEdit.setObjectName(u"label_TemplateEdit")

        self.verticalLayout.addWidget(self.label_TemplateEdit)

        self.plainTextEdit_template = QPlainTextEdit(Settings)
        self.plainTextEdit_template.setObjectName(u"plainTextEdit_template")
        self.plainTextEdit_template.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.plainTextEdit_template)

        self.label_systemSelect = QLabel(Settings)
        self.label_systemSelect.setObjectName(u"label_systemSelect")

        self.verticalLayout.addWidget(self.label_systemSelect)

        self.comboBox_system = QComboBox(Settings)
        self.comboBox_system.setObjectName(u"comboBox_system")

        self.verticalLayout.addWidget(self.comboBox_system)

        self.pushButton_back = QPushButton(Settings)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.pushButton_back)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.label_TemplateEdit.setText(QCoreApplication.translate("Settings", u"New Player/NPC Template", None))
        self.label_systemSelect.setText(QCoreApplication.translate("Settings", u"PnP System Select", None))
        self.pushButton_back.setText(QCoreApplication.translate("Settings", u"<- Save (Esc)", None))
    # retranslateUi

