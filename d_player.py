# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/Player_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Player(object):
    def setupUi(self, Player):
        Player.setObjectName("Player")
        Player.setWindowModality(QtCore.Qt.NonModal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Player.sizePolicy().hasHeightForWidth())
        Player.setSizePolicy(sizePolicy)
        Player.setMinimumSize(QtCore.QSize(629, 115))
        Player.setMaximumSize(QtCore.QSize(629, 115))
        Player.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Player.setModal(False)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Player)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem3 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_name = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_name.sizePolicy().hasHeightForWidth())
        self.comboBox_name.setSizePolicy(sizePolicy)
        self.comboBox_name.setEditable(True)
        self.comboBox_name.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.comboBox_name.setObjectName("comboBox_name")
        self.horizontalLayout.addWidget(self.comboBox_name)
        self.spinBox_initiative = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_initiative.setMinimum(1)
        self.spinBox_initiative.setMaximum(40)
        self.spinBox_initiative.setSingleStep(1)
        self.spinBox_initiative.setProperty("value", 1)
        self.spinBox_initiative.setObjectName("spinBox_initiative")
        self.horizontalLayout.addWidget(self.spinBox_initiative)
        self.spinBox_hp = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_hp.setMinimum(1)
        self.spinBox_hp.setMaximum(999)
        self.spinBox_hp.setSingleStep(1)
        self.spinBox_hp.setObjectName("spinBox_hp")
        self.horizontalLayout.addWidget(self.spinBox_hp)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.pushButton_add = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButton_add.setAutoDefault(True)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_3.addWidget(self.pushButton_add)
        self.pushButton_delete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_delete.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButton_delete.setAutoDefault(False)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout_3.addWidget(self.pushButton_delete)

        self.retranslateUi(Player)
        QtCore.QMetaObject.connectSlotsByName(Player)

    def retranslateUi(self, Player):
        _translate = QtCore.QCoreApplication.translate
        Player.setWindowTitle(_translate("Player", "Add/Remove Players or Simple NPCs"))
        self.label_3.setText(_translate("Player", "Name"))
        self.label_2.setText(_translate("Player", "Initiative"))
        self.label.setText(_translate("Player", "HP"))
        self.pushButton_add.setText(_translate("Player", "Summon!"))
        self.pushButton_delete.setText(_translate("Player", "Un-Summon!"))
