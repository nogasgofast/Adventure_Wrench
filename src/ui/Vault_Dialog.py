# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Vault_Dialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Vault(object):
    def setupUi(self, Vault):
        if not Vault.objectName():
            Vault.setObjectName(u"Vault")
        Vault.setWindowModality(Qt.WindowModal)
        Vault.resize(925, 583)
        self.verticalLayout_3 = QVBoxLayout(Vault)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_header = QHBoxLayout()
        self.horizontalLayout_header.setObjectName(u"horizontalLayout_header")
        self.pushButton_back = QPushButton(Vault)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.horizontalLayout_header.addWidget(self.pushButton_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_header.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_header)

        self.horizontalLayout_content = QHBoxLayout()
        self.horizontalLayout_content.setObjectName(u"horizontalLayout_content")
        self.verticalLayout_menu = QVBoxLayout()
        self.verticalLayout_menu.setObjectName(u"verticalLayout_menu")
        self.verticalLayout_menu.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout_menu.setContentsMargins(0, -1, -1, -1)
        self.pushButton_adventure = QPushButton(Vault)
        self.pushButton_adventure.setObjectName(u"pushButton_adventure")

        self.verticalLayout_menu.addWidget(self.pushButton_adventure)

        self.pushButton = QPushButton(Vault)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_menu.addWidget(self.pushButton)

        self.pushButton_toggle_expand = QPushButton(Vault)
        self.pushButton_toggle_expand.setObjectName(u"pushButton_toggle_expand")

        self.verticalLayout_menu.addWidget(self.pushButton_toggle_expand)

        self.pushButton_Summon = QPushButton(Vault)
        self.pushButton_Summon.setObjectName(u"pushButton_Summon")

        self.verticalLayout_menu.addWidget(self.pushButton_Summon)

        self.pushButton_UnSummon = QPushButton(Vault)
        self.pushButton_UnSummon.setObjectName(u"pushButton_UnSummon")

        self.verticalLayout_menu.addWidget(self.pushButton_UnSummon)

        self.pushButton_delete = QPushButton(Vault)
        self.pushButton_delete.setObjectName(u"pushButton_delete")

        self.verticalLayout_menu.addWidget(self.pushButton_delete)

        self.pushButton_delete_undo = QPushButton(Vault)
        self.pushButton_delete_undo.setObjectName(u"pushButton_delete_undo")

        self.verticalLayout_menu.addWidget(self.pushButton_delete_undo)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_menu.addItem(self.verticalSpacer)


        self.horizontalLayout_content.addLayout(self.verticalLayout_menu)

        self.verticalLayout_treeWidget = QVBoxLayout()
        self.verticalLayout_treeWidget.setObjectName(u"verticalLayout_treeWidget")
        self.label = QLabel(Vault)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_treeWidget.addWidget(self.label)

        self.treeWidget_organizer = QTreeWidget(Vault)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget_organizer.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_organizer.setObjectName(u"treeWidget_organizer")

        self.verticalLayout_treeWidget.addWidget(self.treeWidget_organizer)


        self.horizontalLayout_content.addLayout(self.verticalLayout_treeWidget)

        self.verticalLayout_display = QVBoxLayout()
        self.verticalLayout_display.setObjectName(u"verticalLayout_display")
        self.label_2 = QLabel(Vault)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.MarkdownText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_display.addWidget(self.label_2)

        self.listWidget_Display = QListWidget(Vault)
        self.listWidget_Display.setObjectName(u"listWidget_Display")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_Display.sizePolicy().hasHeightForWidth())
        self.listWidget_Display.setSizePolicy(sizePolicy)
        self.listWidget_Display.setProperty("showDropIndicator", False)
        self.listWidget_Display.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.listWidget_Display.setDefaultDropAction(Qt.IgnoreAction)
        self.listWidget_Display.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget_Display.setWordWrap(True)

        self.verticalLayout_display.addWidget(self.listWidget_Display)


        self.horizontalLayout_content.addLayout(self.verticalLayout_display)


        self.verticalLayout_3.addLayout(self.horizontalLayout_content)


        self.retranslateUi(Vault)

        QMetaObject.connectSlotsByName(Vault)
    # setupUi

    def retranslateUi(self, Vault):
        Vault.setWindowTitle(QCoreApplication.translate("Vault", u"DM Vault", None))
#if QT_CONFIG(tooltip)
        self.pushButton_back.setToolTip(QCoreApplication.translate("Vault", u"Go back to your encounter", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_back.setText(QCoreApplication.translate("Vault", u"\u21e6 Back (Esc)", None))
        self.pushButton_adventure.setText(QCoreApplication.translate("Vault", u"Create New Thingy", None))
        self.pushButton.setText(QCoreApplication.translate("Vault", u"Apply Template", None))
        self.pushButton_toggle_expand.setText(QCoreApplication.translate("Vault", u"Expand/Collapse", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Summon.setToolTip(QCoreApplication.translate("Vault", u"Add Selected Items to Current Encounter", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Summon.setText(QCoreApplication.translate("Vault", u"Copy to Encounter", None))
#if QT_CONFIG(tooltip)
        self.pushButton_UnSummon.setToolTip(QCoreApplication.translate("Vault", u"Remove Selected items from Current Encounter", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_UnSummon.setText(QCoreApplication.translate("Vault", u"Remove from Encounter", None))
#if QT_CONFIG(tooltip)
        self.pushButton_delete.setToolTip(QCoreApplication.translate("Vault", u"Remove selected from current Encounter as well as DM Vault.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_delete.setText(QCoreApplication.translate("Vault", u"Delete", None))
        self.pushButton_delete_undo.setText(QCoreApplication.translate("Vault", u"Undo Delete", None))
        self.label.setText(QCoreApplication.translate("Vault", u"### Double-Click to edit", None))
        self.label_2.setText(QCoreApplication.translate("Vault", u"## Template Summery", None))
    # retranslateUi

