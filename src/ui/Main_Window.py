# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_Window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
        MainWindow.resize(800, 777)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QWidget {\n"
"  color: black;\n"
"  background-color: rgb(89, 92, 123);\n"
"}\n"
"\n"
"QListWidget QTreeWidget{\n"
"   color: #000;\n"
"   selection-color: #FFF;\n"
"   selection-background-color: #55A;\n"
"}\n"
"\n"
"QListWidget::item:selected:!active{\n"
"   color: #000;\n"
"   selection-color: #FFF;\n"
"   selection-background-color: #55A;\n"
"}\n"
"\n"
"QTreeWidget::item:selected:!active{\n"
"   color: #000;\n"
"   selection-color: #FFF;\n"
"   selection-background-color: #55A;\n"
"}\n"
"\n"
"\n"
"QToolTip {\n"
"	border: 3px solid gray;\n"
"	background-color: #39537d;\n"
"    color: #FFF;\n"
"}\n"
"\n"
"QLabel {\n"
"color: rgb(222, 221, 218);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: rgb(75, 82, 143);\n"
"color: white;\n"
"padding: 5px;\n"
"border-color: rgb(75, 82, 143);\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(55, 62, 123);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 30px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QChec"
                        "kBox::indicator:checked {\n"
"     image: url(:/images/toggle_on.png); \n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"     image: url(:/images/toggle_off.png); /* Path to your unchecked image */\n"
"}\n"
"\n"
"\n"
"")
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
        self.label_current_game = QLabel(self.centralwidget)
        self.label_current_game.setObjectName(u"label_current_game")
        self.label_current_game.setStyleSheet(u"")
        self.label_current_game.setTextFormat(Qt.MarkdownText)
        self.label_current_game.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_head.addWidget(self.label_current_game)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_head.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_head)

        self.horizontalLayout_content_2 = QHBoxLayout()
        self.horizontalLayout_content_2.setObjectName(u"horizontalLayout_content_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.listWidget_Encounter = QListWidget(self.centralwidget)
        self.listWidget_Encounter.setObjectName(u"listWidget_Encounter")
        self.listWidget_Encounter.setStyleSheet(u"")
        self.listWidget_Encounter.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.verticalLayout_3.addWidget(self.listWidget_Encounter)


        self.horizontalLayout_content_2.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(-1, -1, 9, 0)
        self.pushButton_Inititave = QPushButton(self.centralwidget)
        self.pushButton_Inititave.setObjectName(u"pushButton_Inititave")
        self.pushButton_Inititave.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(38, 60, 134);\n"
"height: 40px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(18, 40, 114);\n"
"height: 40px;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_Inititave)

        self.pushButton_players = QPushButton(self.centralwidget)
        self.pushButton_players.setObjectName(u"pushButton_players")

        self.verticalLayout.addWidget(self.pushButton_players)

        self.pushButton_vault = QPushButton(self.centralwidget)
        self.pushButton_vault.setObjectName(u"pushButton_vault")

        self.verticalLayout.addWidget(self.pushButton_vault)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_damage = QLabel(self.centralwidget)
        self.label_damage.setObjectName(u"label_damage")
        self.label_damage.setStyleSheet(u"")
        self.label_damage.setTextFormat(Qt.MarkdownText)
        self.label_damage.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_damage)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"")
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
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.spinBox_main_hp = QSpinBox(self.centralwidget)
        self.spinBox_main_hp.setObjectName(u"spinBox_main_hp")
        self.spinBox_main_hp.setMaximum(999)

        self.horizontalLayout_2.addWidget(self.spinBox_main_hp)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_heal_1 = QPushButton(self.centralwidget)
        self.pushButton_heal_1.setObjectName(u"pushButton_heal_1")
        self.pushButton_heal_1.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_heal_1)

        self.pushButton_heal_3 = QPushButton(self.centralwidget)
        self.pushButton_heal_3.setObjectName(u"pushButton_heal_3")
        self.pushButton_heal_3.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_heal_3)

        self.pushButton_heal_5 = QPushButton(self.centralwidget)
        self.pushButton_heal_5.setObjectName(u"pushButton_heal_5")
        self.pushButton_heal_5.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_heal_5)

        self.pushButton_heal_10 = QPushButton(self.centralwidget)
        self.pushButton_heal_10.setObjectName(u"pushButton_heal_10")
        self.pushButton_heal_10.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout.addWidget(self.pushButton_heal_10)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
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

        self.pushButton_kill = QPushButton(self.centralwidget)
        self.pushButton_kill.setObjectName(u"pushButton_kill")

        self.verticalLayout.addWidget(self.pushButton_kill)

        self.pushButton_toggle_expand = QPushButton(self.centralwidget)
        self.pushButton_toggle_expand.setObjectName(u"pushButton_toggle_expand")

        self.verticalLayout.addWidget(self.pushButton_toggle_expand)

        self.pushButton_remove = QPushButton(self.centralwidget)
        self.pushButton_remove.setObjectName(u"pushButton_remove")

        self.verticalLayout.addWidget(self.pushButton_remove)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")
        self.label_2.setTextFormat(Qt.MarkdownText)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_cross = QPushButton(self.centralwidget)
        self.pushButton_cross.setObjectName(u"pushButton_cross")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
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

        self.verticalSpacer_2 = QSpacerItem(20, 175, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_switch_game = QPushButton(self.centralwidget)
        self.pushButton_switch_game.setObjectName(u"pushButton_switch_game")

        self.horizontalLayout_5.addWidget(self.pushButton_switch_game)

        self.pushButton_settings = QPushButton(self.centralwidget)
        self.pushButton_settings.setObjectName(u"pushButton_settings")
        icon = QIcon()
        iconThemeName = u"accessories-text-editor"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.pushButton_settings.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.pushButton_settings)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.label_version = QLabel(self.centralwidget)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setOpenExternalLinks(True)
        self.label_version.setTextInteractionFlags(Qt.LinksAccessibleByKeyboard|Qt.LinksAccessibleByMouse)

        self.verticalLayout.addWidget(self.label_version)


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
        self.label_current_game.setText(QCoreApplication.translate("MainWindow", u"## Current Game", None))
#if QT_CONFIG(tooltip)
        self.pushButton_Inititave.setToolTip(QCoreApplication.translate("MainWindow", u"sort and advannce selected item by initiative", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_Inititave.setText(QCoreApplication.translate("MainWindow", u"Advance Initiative", None))
#if QT_CONFIG(tooltip)
        self.pushButton_players.setToolTip(QCoreApplication.translate("MainWindow", u"Add players and simple things to the current game.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_players.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(tooltip)
        self.pushButton_vault.setToolTip(QCoreApplication.translate("MainWindow", u"A list of things you've created and more tools.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_vault.setText(QCoreApplication.translate("MainWindow", u"Vault", None))
        self.label_damage.setText(QCoreApplication.translate("MainWindow", u"### Selected Item:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Initiative", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"HP", None))
        self.pushButton_heal_1.setText(QCoreApplication.translate("MainWindow", u"+1", None))
        self.pushButton_heal_3.setText(QCoreApplication.translate("MainWindow", u"+3", None))
        self.pushButton_heal_5.setText(QCoreApplication.translate("MainWindow", u"+5", None))
        self.pushButton_heal_10.setText(QCoreApplication.translate("MainWindow", u"+10", None))
        self.pushButton_dam_1.setText(QCoreApplication.translate("MainWindow", u"-1", None))
        self.pushButton_dam_3.setText(QCoreApplication.translate("MainWindow", u"-3", None))
        self.pushButton_dam_5.setText(QCoreApplication.translate("MainWindow", u"-5", None))
        self.pushButton_dam_10.setText(QCoreApplication.translate("MainWindow", u"-10", None))
#if QT_CONFIG(tooltip)
        self.pushButton_kill.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton_kill.setText(QCoreApplication.translate("MainWindow", u"Set HP to 0", None))
#if QT_CONFIG(tooltip)
        self.pushButton_toggle_expand.setToolTip(QCoreApplication.translate("MainWindow", u"Groups-up selections of creatures with the same name. (shift to select multiple). Or breaks down groups into individuals.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_toggle_expand.setText(QCoreApplication.translate("MainWindow", u"Group-up Toggle", None))
        self.pushButton_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Status labels:", None))
#if QT_CONFIG(tooltip)
        self.pushButton_cross.setToolTip(QCoreApplication.translate("MainWindow", u"cycles on 3rd press", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_cross.setText(QCoreApplication.translate("MainWindow", u"\u2716", None))
#if QT_CONFIG(tooltip)
        self.pushButton_check.setToolTip(QCoreApplication.translate("MainWindow", u"cycles on 3rd press", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_check.setText(QCoreApplication.translate("MainWindow", u"\u2714", None))
#if QT_CONFIG(tooltip)
        self.pushButton_b_star.setToolTip(QCoreApplication.translate("MainWindow", u"cycles on 6th press", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_b_star.setText(QCoreApplication.translate("MainWindow", u"\u2605", None))
#if QT_CONFIG(tooltip)
        self.pushButton_w_star.setToolTip(QCoreApplication.translate("MainWindow", u"cycles on 6th press", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_w_star.setText(QCoreApplication.translate("MainWindow", u"\u2606", None))
        self.pushButton_switch_game.setText(QCoreApplication.translate("MainWindow", u"Switch Game", None))
#if QT_CONFIG(tooltip)
        self.pushButton_settings.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_settings.setText("")
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"Checking Version...", None))
    # retranslateUi

