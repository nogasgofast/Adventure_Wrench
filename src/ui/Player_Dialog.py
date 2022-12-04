# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Player_Dialog.ui'
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
    QLabel, QPushButton, QSizePolicy, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Player(object):
    def setupUi(self, Player):
        if not Player.objectName():
            Player.setObjectName(u"Player")
        Player.setWindowModality(Qt.NonModal)
        Player.resize(629, 344)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Player.sizePolicy().hasHeightForWidth())
        Player.setSizePolicy(sizePolicy)
        Player.setMinimumSize(QSize(629, 0))
        Player.setMaximumSize(QSize(629, 16777215))
        Player.setContextMenuPolicy(Qt.DefaultContextMenu)
        Player.setModal(False)
        self.verticalLayout = QVBoxLayout(Player)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_head = QHBoxLayout()
        self.horizontalLayout_head.setObjectName(u"horizontalLayout_head")
        self.verticalLayout_name = QVBoxLayout()
        self.verticalLayout_name.setObjectName(u"verticalLayout_name")
        self.label_name = QLabel(Player)
        self.label_name.setObjectName(u"label_name")

        self.verticalLayout_name.addWidget(self.label_name)

        self.comboBox_name = QComboBox(Player)
        self.comboBox_name.setObjectName(u"comboBox_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox_name.sizePolicy().hasHeightForWidth())
        self.comboBox_name.setSizePolicy(sizePolicy1)
        self.comboBox_name.setEditable(True)
        self.comboBox_name.setInsertPolicy(QComboBox.NoInsert)

        self.verticalLayout_name.addWidget(self.comboBox_name)


        self.horizontalLayout_head.addLayout(self.verticalLayout_name)

        self.verticalLayout_inititive = QVBoxLayout()
        self.verticalLayout_inititive.setObjectName(u"verticalLayout_inititive")
        self.label_inititive = QLabel(Player)
        self.label_inititive.setObjectName(u"label_inititive")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_inititive.sizePolicy().hasHeightForWidth())
        self.label_inititive.setSizePolicy(sizePolicy2)

        self.verticalLayout_inititive.addWidget(self.label_inititive)

        self.spinBox_initiative = QSpinBox(Player)
        self.spinBox_initiative.setObjectName(u"spinBox_initiative")
        self.spinBox_initiative.setMinimum(1)
        self.spinBox_initiative.setMaximum(999)
        self.spinBox_initiative.setSingleStep(1)
        self.spinBox_initiative.setValue(1)

        self.verticalLayout_inititive.addWidget(self.spinBox_initiative)


        self.horizontalLayout_head.addLayout(self.verticalLayout_inititive)

        self.verticalLayout_hp = QVBoxLayout()
        self.verticalLayout_hp.setObjectName(u"verticalLayout_hp")
        self.label_hp = QLabel(Player)
        self.label_hp.setObjectName(u"label_hp")
        sizePolicy2.setHeightForWidth(self.label_hp.sizePolicy().hasHeightForWidth())
        self.label_hp.setSizePolicy(sizePolicy2)

        self.verticalLayout_hp.addWidget(self.label_hp)

        self.spinBox_hp = QSpinBox(Player)
        self.spinBox_hp.setObjectName(u"spinBox_hp")
        self.spinBox_hp.setMinimum(1)
        self.spinBox_hp.setMaximum(999)
        self.spinBox_hp.setSingleStep(1)

        self.verticalLayout_hp.addWidget(self.spinBox_hp)


        self.horizontalLayout_head.addLayout(self.verticalLayout_hp)


        self.verticalLayout.addLayout(self.horizontalLayout_head)

        self.label = QLabel(Player)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.textEdit = QTextEdit(Player)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 150))

        self.verticalLayout.addWidget(self.textEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_add = QPushButton(Player)
        self.pushButton_add.setObjectName(u"pushButton_add")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy3)
        self.pushButton_add.setMinimumSize(QSize(0, 0))
        self.pushButton_add.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.pushButton_add)

        self.pushButton_delete = QPushButton(Player)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        sizePolicy3.setHeightForWidth(self.pushButton_delete.sizePolicy().hasHeightForWidth())
        self.pushButton_delete.setSizePolicy(sizePolicy3)
        self.pushButton_delete.setMinimumSize(QSize(0, 0))
        self.pushButton_delete.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.pushButton_delete)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Player)

        QMetaObject.connectSlotsByName(Player)
    # setupUi

    def retranslateUi(self, Player):
        Player.setWindowTitle(QCoreApplication.translate("Player", u"Add/Remove Players or Simple NPCs", None))
        self.label_name.setText(QCoreApplication.translate("Player", u"Name", None))
        self.label_inititive.setText(QCoreApplication.translate("Player", u"Initiative", None))
        self.label_hp.setText(QCoreApplication.translate("Player", u"HP", None))
        self.label.setText(QCoreApplication.translate("Player", u"Description", None))
        self.pushButton_add.setText(QCoreApplication.translate("Player", u"Add", None))
        self.pushButton_delete.setText(QCoreApplication.translate("Player", u"Remove", None))
    # retranslateUi

