# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/Player_Dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Player(object):
    def setupUi(self, Player):
        Player.setObjectName(_fromUtf8("Player"))
        Player.resize(629, 115)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Player.sizePolicy().hasHeightForWidth())
        Player.setSizePolicy(sizePolicy)
        Player.setMinimumSize(QtCore.QSize(629, 115))
        Player.setMaximumSize(QtCore.QSize(629, 115))
        self.horizontalLayoutWidget = QtGui.QWidget(Player)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 611, 101))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 15, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem3 = QtGui.QSpacerItem(31, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboBox_name = QtGui.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_name.sizePolicy().hasHeightForWidth())
        self.comboBox_name.setSizePolicy(sizePolicy)
        self.comboBox_name.setEditable(True)
        self.comboBox_name.setObjectName(_fromUtf8("comboBox_name"))
        self.horizontalLayout.addWidget(self.comboBox_name)
        self.spinBox_initiative = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_initiative.setMinimum(1)
        self.spinBox_initiative.setMaximum(40)
        self.spinBox_initiative.setSingleStep(1)
        self.spinBox_initiative.setProperty("value", 1)
        self.spinBox_initiative.setObjectName(_fromUtf8("spinBox_initiative"))
        self.horizontalLayout.addWidget(self.spinBox_initiative)
        self.spinBox_hp = QtGui.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_hp.setMinimum(1)
        self.spinBox_hp.setMaximum(999)
        self.spinBox_hp.setSingleStep(1)
        self.spinBox_hp.setObjectName(_fromUtf8("spinBox_hp"))
        self.horizontalLayout.addWidget(self.spinBox_hp)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.pushButton_add = QtGui.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.horizontalLayout_3.addWidget(self.pushButton_add)
        self.pushButton_delete = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_delete.setMinimumSize(QtCore.QSize(0, 80))
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.horizontalLayout_3.addWidget(self.pushButton_delete)

        self.retranslateUi(Player)
        QtCore.QMetaObject.connectSlotsByName(Player)

    def retranslateUi(self, Player):
        Player.setWindowTitle(_translate("Player", "Dialog", None))
        self.label_3.setText(_translate("Player", "Name", None))
        self.label_2.setText(_translate("Player", "Initiative", None))
        self.label.setText(_translate("Player", "HP", None))
        self.pushButton_add.setText(_translate("Player", "Summon!", None))
        self.pushButton_delete.setText(_translate("Player", "Un-Summon!", None))

