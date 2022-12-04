# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QLabel,
    QLayout, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 585)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_head = QHBoxLayout()
        self.horizontalLayout_head.setObjectName(u"horizontalLayout_head")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setTextFormat(Qt.MarkdownText)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_head.addWidget(self.label_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_head.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_head)

        self.horizontalLayout_content_2 = QHBoxLayout()
        self.horizontalLayout_content_2.setObjectName(u"horizontalLayout_content_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listWidget_Encounter = QListWidget(self.centralwidget)
        self.listWidget_Encounter.setObjectName(u"listWidget_Encounter")
        self.listWidget_Encounter.setStyleSheet(u"font: 75 12pt \"Cantarell\";")
        self.listWidget_Encounter.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_3.addWidget(self.listWidget_Encounter)


        self.horizontalLayout_content_2.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(-1, -1, 9, 0)
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setTextFormat(Qt.MarkdownText)

        self.verticalLayout.addWidget(self.label)

        self.pushButton_Players = QPushButton(self.centralwidget)
        self.pushButton_Players.setObjectName(u"pushButton_Players")

        self.verticalLayout.addWidget(self.pushButton_Players)

        self.pushButton_Encounter = QPushButton(self.centralwidget)
        self.pushButton_Encounter.setObjectName(u"pushButton_Encounter")

        self.verticalLayout.addWidget(self.pushButton_Encounter)

        self.label_quick_change = QLabel(self.centralwidget)
        self.label_quick_change.setObjectName(u"label_quick_change")
        self.label_quick_change.setTextFormat(Qt.MarkdownText)
        self.label_quick_change.setScaledContents(False)
        self.label_quick_change.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_quick_change)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.spinBox_main_initiative = QSpinBox(self.centralwidget)
        self.spinBox_main_initiative.setObjectName(u"spinBox_main_initiative")
        self.spinBox_main_initiative.setMaximum(999)

        self.horizontalLayout_4.addWidget(self.spinBox_main_initiative)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.spinBox_main_hp = QSpinBox(self.centralwidget)
        self.spinBox_main_hp.setObjectName(u"spinBox_main_hp")
        self.spinBox_main_hp.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.spinBox_main_hp)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_damage = QLabel(self.centralwidget)
        self.label_damage.setObjectName(u"label_damage")
        self.label_damage.setStyleSheet(u"")
        self.label_damage.setTextFormat(Qt.MarkdownText)
        self.label_damage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_damage)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_dam_1 = QPushButton(self.centralwidget)
        self.pushButton_dam_1.setObjectName(u"pushButton_dam_1")
        self.pushButton_dam_1.setMaximumSize(QSize(40, 16777215))
        self.pushButton_dam_1.setIconSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.pushButton_dam_1)

        self.pushButton_dam_3 = QPushButton(self.centralwidget)
        self.pushButton_dam_3.setObjectName(u"pushButton_dam_3")
        self.pushButton_dam_3.setMaximumSize(QSize(40, 16777215))
        self.pushButton_dam_3.setIconSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.pushButton_dam_3)

        self.pushButton_dam_5 = QPushButton(self.centralwidget)
        self.pushButton_dam_5.setObjectName(u"pushButton_dam_5")
        self.pushButton_dam_5.setMaximumSize(QSize(40, 16777215))
        self.pushButton_dam_5.setIconSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.pushButton_dam_5)

        self.pushButton_dam_10 = QPushButton(self.centralwidget)
        self.pushButton_dam_10.setObjectName(u"pushButton_dam_10")
        self.pushButton_dam_10.setMaximumSize(QSize(40, 16777215))
        self.pushButton_dam_10.setIconSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.pushButton_dam_10)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton_kill_remove = QPushButton(self.centralwidget)
        self.pushButton_kill_remove.setObjectName(u"pushButton_kill_remove")

        self.verticalLayout.addWidget(self.pushButton_kill_remove)

        self.label_markers = QLabel(self.centralwidget)
        self.label_markers.setObjectName(u"label_markers")
        self.label_markers.setTextFormat(Qt.MarkdownText)
        self.label_markers.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_markers)

        self.pushButton_toggle_expand = QPushButton(self.centralwidget)
        self.pushButton_toggle_expand.setObjectName(u"pushButton_toggle_expand")

        self.verticalLayout.addWidget(self.pushButton_toggle_expand)

        self.pushButton_Inititave = QPushButton(self.centralwidget)
        self.pushButton_Inititave.setObjectName(u"pushButton_Inititave")

        self.verticalLayout.addWidget(self.pushButton_Inititave)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_cross = QPushButton(self.centralwidget)
        self.pushButton_cross.setObjectName(u"pushButton_cross")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_cross.sizePolicy().hasHeightForWidth())
        self.pushButton_cross.setSizePolicy(sizePolicy1)
        self.pushButton_cross.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButton_cross)

        self.pushButton_check = QPushButton(self.centralwidget)
        self.pushButton_check.setObjectName(u"pushButton_check")
        self.pushButton_check.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButton_check)

        self.pushButton_b_star = QPushButton(self.centralwidget)
        self.pushButton_b_star.setObjectName(u"pushButton_b_star")
        self.pushButton_b_star.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButton_b_star)

        self.pushButton_w_star = QPushButton(self.centralwidget)
        self.pushButton_w_star.setObjectName(u"pushButton_w_star")
        self.pushButton_w_star.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButton_w_star)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 175, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_content_2.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout_content_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Adventure Wrench", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"## Current Encounter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"### Add Stuff", None))
        self.pushButton_Players.setText(QCoreApplication.translate("MainWindow", u"Players", None))
        self.pushButton_Encounter.setText(QCoreApplication.translate("MainWindow", u"The Vault", None))
        self.label_quick_change.setText(QCoreApplication.translate("MainWindow", u"### Quick Change", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Initiative", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"HP", None))
        self.label_damage.setText(QCoreApplication.translate("MainWindow", u"### Damage", None))
        self.pushButton_dam_1.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.pushButton_dam_3.setText(QCoreApplication.translate("MainWindow", u"-3", None))
        self.pushButton_dam_5.setText(QCoreApplication.translate("MainWindow", u"-5", None))
        self.pushButton_dam_10.setText(QCoreApplication.translate("MainWindow", u"-10", None))
        self.pushButton_kill_remove.setText(QCoreApplication.translate("MainWindow", u"Kill/Remove", None))
        self.label_markers.setText(QCoreApplication.translate("MainWindow", u"### Tools", None))
        self.pushButton_toggle_expand.setText(QCoreApplication.translate("MainWindow", u"Expand/Collapse", None))
        self.pushButton_Inititave.setText(QCoreApplication.translate("MainWindow", u"Advance Inititave", None))
        self.pushButton_cross.setText(QCoreApplication.translate("MainWindow", u"\u2716", None))
        self.pushButton_check.setText(QCoreApplication.translate("MainWindow", u"\u2714", None))
        self.pushButton_b_star.setText(QCoreApplication.translate("MainWindow", u"\u2605", None))
        self.pushButton_w_star.setText(QCoreApplication.translate("MainWindow", u"\u2606", None))
    # retranslateUi

