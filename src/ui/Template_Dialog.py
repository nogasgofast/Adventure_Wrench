# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Template_Dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTreeView,
    QVBoxLayout, QWidget)

class Ui_template_editor(object):
    def setupUi(self, template_editor):
        if not template_editor.objectName():
            template_editor.setObjectName(u"template_editor")
        template_editor.setWindowModality(Qt.ApplicationModal)
        template_editor.resize(448, 500)
        template_editor.setModal(True)
        self.verticalLayout = QVBoxLayout(template_editor)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(template_editor)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(template_editor)
        self.lineEdit_name.setObjectName(u"lineEdit_name")

        self.verticalLayout.addWidget(self.lineEdit_name)

        self.pushButton_descriptions = QPushButton(template_editor)
        self.pushButton_descriptions.setObjectName(u"pushButton_descriptions")

        self.verticalLayout.addWidget(self.pushButton_descriptions)

        self.pushButton_stats = QPushButton(template_editor)
        self.pushButton_stats.setObjectName(u"pushButton_stats")

        self.verticalLayout.addWidget(self.pushButton_stats)

        self.pushButton_items = QPushButton(template_editor)
        self.pushButton_items.setObjectName(u"pushButton_items")

        self.verticalLayout.addWidget(self.pushButton_items)

        self.pushButton_attributes = QPushButton(template_editor)
        self.pushButton_attributes.setObjectName(u"pushButton_attributes")

        self.verticalLayout.addWidget(self.pushButton_attributes)

        self.pushButton_actions = QPushButton(template_editor)
        self.pushButton_actions.setObjectName(u"pushButton_actions")

        self.verticalLayout.addWidget(self.pushButton_actions)

        self.treeView_template_preview = QTreeView(template_editor)
        self.treeView_template_preview.setObjectName(u"treeView_template_preview")

        self.verticalLayout.addWidget(self.treeView_template_preview)

        self.pushButton_delete = QPushButton(template_editor)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.verticalLayout.addWidget(self.pushButton_delete)

        self.pushButton_back = QPushButton(template_editor)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.verticalLayout.addWidget(self.pushButton_back)


        self.retranslateUi(template_editor)

        QMetaObject.connectSlotsByName(template_editor)
    # setupUi

    def retranslateUi(self, template_editor):
        template_editor.setWindowTitle(QCoreApplication.translate("template_editor", u"Template Editor", None))
        self.label_name.setText(QCoreApplication.translate("template_editor", u"Name", None))
        self.pushButton_descriptions.setText(QCoreApplication.translate("template_editor", u"Descriptions", None))
        self.pushButton_stats.setText(QCoreApplication.translate("template_editor", u"Stats", None))
        self.pushButton_items.setText(QCoreApplication.translate("template_editor", u"Items", None))
        self.pushButton_attributes.setText(QCoreApplication.translate("template_editor", u"Attributes", None))
        self.pushButton_actions.setText(QCoreApplication.translate("template_editor", u"Actions", None))
        self.pushButton_delete.setText(QCoreApplication.translate("template_editor", u"Delete", None))
        self.pushButton_back.setText(QCoreApplication.translate("template_editor", u"\u21e6 Done (Esc)", None))
    # retranslateUi

