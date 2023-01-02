# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vault_Dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Vault(object):
    def setupUi(self, Vault):
        if not Vault.objectName():
            Vault.setObjectName(u"Vault")
        Vault.resize(673, 583)
        self.verticalLayout_3 = QVBoxLayout(Vault)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_content = QHBoxLayout()
        self.horizontalLayout_content.setObjectName(u"horizontalLayout_content")
        self.verticalLayout_menu = QVBoxLayout()
        self.verticalLayout_menu.setObjectName(u"verticalLayout_menu")
        self.verticalLayout_menu.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_menu.setContentsMargins(0, -1, -1, -1)
        self.label = QLabel(Vault)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_menu.addWidget(self.label)

        self.pushButton_add_to_encounter = QPushButton(Vault)
        self.pushButton_add_to_encounter.setObjectName(u"pushButton_add_to_encounter")

        self.verticalLayout_menu.addWidget(self.pushButton_add_to_encounter)

        self.pushButton_remove_from_encounter = QPushButton(Vault)
        self.pushButton_remove_from_encounter.setObjectName(u"pushButton_remove_from_encounter")

        self.verticalLayout_menu.addWidget(self.pushButton_remove_from_encounter)

        self.pushButton_delete_selected_items = QPushButton(Vault)
        self.pushButton_delete_selected_items.setObjectName(u"pushButton_delete_selected_items")

        self.verticalLayout_menu.addWidget(self.pushButton_delete_selected_items)

        self.pushButton_clear_delete = QPushButton(Vault)
        self.pushButton_clear_delete.setObjectName(u"pushButton_clear_delete")

        self.verticalLayout_menu.addWidget(self.pushButton_clear_delete)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_menu.addItem(self.verticalSpacer)

        self.label_2 = QLabel(Vault)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.MarkdownText)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_menu.addWidget(self.label_2)

        self.pushButton_the_shop = QPushButton(Vault)
        self.pushButton_the_shop.setObjectName(u"pushButton_the_shop")

        self.verticalLayout_menu.addWidget(self.pushButton_the_shop)

        self.pushButton_acadamy = QPushButton(Vault)
        self.pushButton_acadamy.setObjectName(u"pushButton_acadamy")

        self.verticalLayout_menu.addWidget(self.pushButton_acadamy)


        self.horizontalLayout_content.addLayout(self.verticalLayout_menu)

        self.verticalLayout_treeWidget = QVBoxLayout()
        self.verticalLayout_treeWidget.setObjectName(u"verticalLayout_treeWidget")
        self.listWidget_vault = QListWidget(Vault)
        self.listWidget_vault.setObjectName(u"listWidget_vault")

        self.verticalLayout_treeWidget.addWidget(self.listWidget_vault)


        self.horizontalLayout_content.addLayout(self.verticalLayout_treeWidget)


        self.verticalLayout_3.addLayout(self.horizontalLayout_content)


        self.retranslateUi(Vault)

        QMetaObject.connectSlotsByName(Vault)
    # setupUi

    def retranslateUi(self, Vault):
        Vault.setWindowTitle(QCoreApplication.translate("Vault", u"DM Vault", None))
        self.label.setText(QCoreApplication.translate("Vault", u"## Tools", None))
#if QT_CONFIG(tooltip)
        self.pushButton_add_to_encounter.setToolTip(QCoreApplication.translate("Vault", u"Add Selected Items to Current Encounter", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_add_to_encounter.setText(QCoreApplication.translate("Vault", u"Copy into Encounter", None))
#if QT_CONFIG(tooltip)
        self.pushButton_remove_from_encounter.setToolTip(QCoreApplication.translate("Vault", u"Remove Selected items from Current Encounter", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_remove_from_encounter.setText(QCoreApplication.translate("Vault", u"Remove from Encounter", None))
#if QT_CONFIG(tooltip)
        self.pushButton_delete_selected_items.setToolTip(QCoreApplication.translate("Vault", u"Remove selected from current Encounter as well as DM Vault.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_delete_selected_items.setText(QCoreApplication.translate("Vault", u"Mark/Delete", None))
        self.pushButton_clear_delete.setText(QCoreApplication.translate("Vault", u"Clear Mark", None))
        self.label_2.setText(QCoreApplication.translate("Vault", u"## Add Stuff", None))
#if QT_CONFIG(tooltip)
        self.pushButton_the_shop.setToolTip(QCoreApplication.translate("Vault", u"Add something new to the vault using templates.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_the_shop.setText(QCoreApplication.translate("Vault", u"The Shop", None))
#if QT_CONFIG(tooltip)
        self.pushButton_acadamy.setToolTip(QCoreApplication.translate("Vault", u"add/edit templates usable in the shop.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_acadamy.setText(QCoreApplication.translate("Vault", u"The Acadamy", None))
    # retranslateUi

