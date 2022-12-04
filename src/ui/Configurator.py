# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Configurator.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_configurator(object):
    def setupUi(self, configurator):
        if not configurator.objectName():
            configurator.setObjectName(u"configurator")
        configurator.setWindowModality(Qt.WindowModal)
        configurator.resize(794, 304)
        configurator.setStyleSheet(u"QpushButton { margin: 0,0,0,25 px; }")
        configurator.setModal(True)
        self.verticalLayout = QVBoxLayout(configurator)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontal_layout_header = QHBoxLayout()
        self.horizontal_layout_header.setObjectName(u"horizontal_layout_header")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalName = QHBoxLayout()
        self.horizontalName.setObjectName(u"horizontalName")
        self.label_Name = QLabel(configurator)
        self.label_Name.setObjectName(u"label_Name")

        self.horizontalName.addWidget(self.label_Name)

        self.lineEdit_Name = QLineEdit(configurator)
        self.lineEdit_Name.setObjectName(u"lineEdit_Name")

        self.horizontalName.addWidget(self.lineEdit_Name)


        self.verticalLayout_5.addLayout(self.horizontalName)

        self.horizontalType = QHBoxLayout()
        self.horizontalType.setObjectName(u"horizontalType")
        self.label_type = QLabel(configurator)
        self.label_type.setObjectName(u"label_type")

        self.horizontalType.addWidget(self.label_type)

        self.comboBox_type = QComboBox(configurator)
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.setObjectName(u"comboBox_type")

        self.horizontalType.addWidget(self.comboBox_type)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalType.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalType)

        self.horizontalSize = QHBoxLayout()
        self.horizontalSize.setObjectName(u"horizontalSize")
        self.label_size = QLabel(configurator)
        self.label_size.setObjectName(u"label_size")

        self.horizontalSize.addWidget(self.label_size)

        self.comboBox_size = QComboBox(configurator)
        self.comboBox_size.setObjectName(u"comboBox_size")

        self.horizontalSize.addWidget(self.comboBox_size)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalSize.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addLayout(self.horizontalSize)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_speed = QLabel(configurator)
        self.label_speed.setObjectName(u"label_speed")

        self.horizontalLayout_11.addWidget(self.label_speed)

        self.comboBox_speed = QComboBox(configurator)
        self.comboBox_speed.setObjectName(u"comboBox_speed")

        self.horizontalLayout_11.addWidget(self.comboBox_speed)

        self.spinBox_speed = QSpinBox(configurator)
        self.spinBox_speed.setObjectName(u"spinBox_speed")
        self.spinBox_speed.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_11.addWidget(self.spinBox_speed)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_14 = QLabel(configurator)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_9.addWidget(self.label_14)

        self.spinBox_group = QSpinBox(configurator)
        self.spinBox_group.setObjectName(u"spinBox_group")
        self.spinBox_group.setValue(1)

        self.horizontalLayout_9.addWidget(self.spinBox_group)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_4 = QLabel(configurator)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.spinBox_CR = QSpinBox(configurator)
        self.spinBox_CR.setObjectName(u"spinBox_CR")
        self.spinBox_CR.setMaximum(30)
        self.spinBox_CR.setValue(10)

        self.horizontalLayout_10.addWidget(self.spinBox_CR)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_back = QPushButton(configurator)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.horizontalLayout.addWidget(self.pushButton_back)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.horizontal_layout_header.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_init_stats = QPushButton(configurator)
        self.pushButton_init_stats.setObjectName(u"pushButton_init_stats")

        self.verticalLayout_6.addWidget(self.pushButton_init_stats)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_STR = QLabel(configurator)
        self.label_STR.setObjectName(u"label_STR")
        self.label_STR.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.label_STR)

        self.label_DEX = QLabel(configurator)
        self.label_DEX.setObjectName(u"label_DEX")

        self.horizontalLayout_5.addWidget(self.label_DEX)

        self.label_CON = QLabel(configurator)
        self.label_CON.setObjectName(u"label_CON")

        self.horizontalLayout_5.addWidget(self.label_CON)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.spinBox_STR = QSpinBox(configurator)
        self.spinBox_STR.setObjectName(u"spinBox_STR")
        self.spinBox_STR.setMaximum(30)
        self.spinBox_STR.setValue(10)

        self.horizontalLayout_6.addWidget(self.spinBox_STR)

        self.spinBox_DEX = QSpinBox(configurator)
        self.spinBox_DEX.setObjectName(u"spinBox_DEX")
        self.spinBox_DEX.setMaximum(30)
        self.spinBox_DEX.setValue(10)

        self.horizontalLayout_6.addWidget(self.spinBox_DEX)

        self.spinBox_CON = QSpinBox(configurator)
        self.spinBox_CON.setObjectName(u"spinBox_CON")
        self.spinBox_CON.setMaximum(30)
        self.spinBox_CON.setValue(10)

        self.horizontalLayout_6.addWidget(self.spinBox_CON)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_WIS = QLabel(configurator)
        self.label_WIS.setObjectName(u"label_WIS")

        self.horizontalLayout_7.addWidget(self.label_WIS)

        self.label_INT = QLabel(configurator)
        self.label_INT.setObjectName(u"label_INT")

        self.horizontalLayout_7.addWidget(self.label_INT)

        self.label_CHA = QLabel(configurator)
        self.label_CHA.setObjectName(u"label_CHA")

        self.horizontalLayout_7.addWidget(self.label_CHA)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.spinBox_WIS = QSpinBox(configurator)
        self.spinBox_WIS.setObjectName(u"spinBox_WIS")
        self.spinBox_WIS.setMaximum(30)
        self.spinBox_WIS.setValue(10)

        self.horizontalLayout_8.addWidget(self.spinBox_WIS)

        self.spinBox_INT = QSpinBox(configurator)
        self.spinBox_INT.setObjectName(u"spinBox_INT")
        self.spinBox_INT.setMaximum(30)
        self.spinBox_INT.setValue(10)

        self.horizontalLayout_8.addWidget(self.spinBox_INT)

        self.spinBox_CHA = QSpinBox(configurator)
        self.spinBox_CHA.setObjectName(u"spinBox_CHA")
        self.spinBox_CHA.setMaximum(30)
        self.spinBox_CHA.setValue(10)

        self.horizontalLayout_8.addWidget(self.spinBox_CHA)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.pushButton_create = QPushButton(configurator)
        self.pushButton_create.setObjectName(u"pushButton_create")

        self.verticalLayout_6.addWidget(self.pushButton_create)


        self.horizontal_layout_header.addLayout(self.verticalLayout_6)


        self.verticalLayout.addLayout(self.horizontal_layout_header)


        self.retranslateUi(configurator)

        QMetaObject.connectSlotsByName(configurator)
    # setupUi

    def retranslateUi(self, configurator):
        configurator.setWindowTitle(QCoreApplication.translate("configurator", u"Characteristics", None))
        self.label_Name.setText(QCoreApplication.translate("configurator", u"Name:", None))
        self.lineEdit_Name.setInputMask("")
        self.lineEdit_Name.setText("")
        self.lineEdit_Name.setPlaceholderText(QCoreApplication.translate("configurator", u"***", None))
        self.label_type.setText(QCoreApplication.translate("configurator", u"Type:", None))
        self.comboBox_type.setItemText(0, QCoreApplication.translate("configurator", u"encounter", None))
        self.comboBox_type.setItemText(1, QCoreApplication.translate("configurator", u"monster", None))
        self.comboBox_type.setItemText(2, QCoreApplication.translate("configurator", u"trap", None))
        self.comboBox_type.setItemText(3, QCoreApplication.translate("configurator", u"npc", None))

        self.label_size.setText(QCoreApplication.translate("configurator", u"Size:", None))
        self.label_speed.setText(QCoreApplication.translate("configurator", u"Speed:", None))
        self.label_14.setText(QCoreApplication.translate("configurator", u"Group of:", None))
        self.label_4.setText(QCoreApplication.translate("configurator", u"TARGET CR:", None))
        self.pushButton_back.setText(QCoreApplication.translate("configurator", u"Back (Esc)", None))
#if QT_CONFIG(tooltip)
        self.pushButton_init_stats.setToolTip(QCoreApplication.translate("configurator", u"stats are initially 10 unless you use this option to change them.", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_init_stats.setText(QCoreApplication.translate("configurator", u"Toggle Initial Stats", None))
        self.label_STR.setText(QCoreApplication.translate("configurator", u"STR", None))
        self.label_DEX.setText(QCoreApplication.translate("configurator", u"DEX", None))
        self.label_CON.setText(QCoreApplication.translate("configurator", u"CON", None))
        self.label_WIS.setText(QCoreApplication.translate("configurator", u"WIS", None))
        self.label_INT.setText(QCoreApplication.translate("configurator", u"INT", None))
        self.label_CHA.setText(QCoreApplication.translate("configurator", u"CHA", None))
#if QT_CONFIG(tooltip)
        self.pushButton_create.setToolTip(QCoreApplication.translate("configurator", u"Add your creation to the DM vault..", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_create.setText(QCoreApplication.translate("configurator", u"Save Selected to Vault", None))
    # retranslateUi

