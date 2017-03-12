# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/Main_Window.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(784, 442)
        self.gridLayout = QtGui.QGridLayout(MainWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listWidget_Encounter = QtGui.QListWidget(MainWindow)
        self.listWidget_Encounter.setStyleSheet(_fromUtf8("font: 75 12pt \"Cantarell\";"))
        self.listWidget_Encounter.setObjectName(_fromUtf8("listWidget_Encounter"))
        self.horizontalLayout.addWidget(self.listWidget_Encounter)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(-1, -1, 9, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton_Players = QtGui.QPushButton(MainWindow)
        self.pushButton_Players.setObjectName(_fromUtf8("pushButton_Players"))
        self.verticalLayout.addWidget(self.pushButton_Players)
        self.pushButton_Encounter = QtGui.QPushButton(MainWindow)
        self.pushButton_Encounter.setObjectName(_fromUtf8("pushButton_Encounter"))
        self.verticalLayout.addWidget(self.pushButton_Encounter)
        self.pushButton_toggle_expand = QtGui.QPushButton(MainWindow)
        self.pushButton_toggle_expand.setObjectName(_fromUtf8("pushButton_toggle_expand"))
        self.verticalLayout.addWidget(self.pushButton_toggle_expand)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtGui.QLabel(MainWindow)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.spinBox_main_initiative = QtGui.QSpinBox(MainWindow)
        self.spinBox_main_initiative.setObjectName(_fromUtf8("spinBox_main_initiative"))
        self.horizontalLayout_4.addWidget(self.spinBox_main_initiative)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(MainWindow)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.spinBox_main_hp = QtGui.QSpinBox(MainWindow)
        self.spinBox_main_hp.setMaximum(999)
        self.spinBox_main_hp.setObjectName(_fromUtf8("spinBox_main_hp"))
        self.horizontalLayout_2.addWidget(self.spinBox_main_hp)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label = QtGui.QLabel(MainWindow)
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_dam_1 = QtGui.QPushButton(MainWindow)
        self.pushButton_dam_1.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_dam_1.setIconSize(QtCore.QSize(0, 0))
        self.pushButton_dam_1.setObjectName(_fromUtf8("pushButton_dam_1"))
        self.horizontalLayout_3.addWidget(self.pushButton_dam_1)
        self.pushButton_dam_3 = QtGui.QPushButton(MainWindow)
        self.pushButton_dam_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_dam_3.setIconSize(QtCore.QSize(0, 0))
        self.pushButton_dam_3.setObjectName(_fromUtf8("pushButton_dam_3"))
        self.horizontalLayout_3.addWidget(self.pushButton_dam_3)
        self.pushButton_dam_5 = QtGui.QPushButton(MainWindow)
        self.pushButton_dam_5.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_dam_5.setIconSize(QtCore.QSize(0, 0))
        self.pushButton_dam_5.setObjectName(_fromUtf8("pushButton_dam_5"))
        self.horizontalLayout_3.addWidget(self.pushButton_dam_5)
        self.pushButton_dam_10 = QtGui.QPushButton(MainWindow)
        self.pushButton_dam_10.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton_dam_10.setIconSize(QtCore.QSize(0, 0))
        self.pushButton_dam_10.setObjectName(_fromUtf8("pushButton_dam_10"))
        self.horizontalLayout_3.addWidget(self.pushButton_dam_10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_Inititave = QtGui.QPushButton(MainWindow)
        self.pushButton_Inititave.setObjectName(_fromUtf8("pushButton_Inititave"))
        self.verticalLayout.addWidget(self.pushButton_Inititave)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Ugin\'s 5e Encounters", None))
        self.pushButton_Players.setText(_translate("MainWindow", "Add/Remove Players", None))
        self.pushButton_Encounter.setText(_translate("MainWindow", "Add/Remove Encounter", None))
        self.pushButton_toggle_expand.setText(_translate("MainWindow", "Expand/Collapse", None))
        self.label_2.setText(_translate("MainWindow", "Quick Change", None))
        self.label_3.setText(_translate("MainWindow", "Initiative", None))
        self.label_4.setText(_translate("MainWindow", "HP", None))
        self.label.setText(_translate("MainWindow", "Damage", None))
        self.pushButton_dam_1.setText(_translate("MainWindow", "-1", None))
        self.pushButton_dam_3.setText(_translate("MainWindow", "-3", None))
        self.pushButton_dam_5.setText(_translate("MainWindow", "-5", None))
        self.pushButton_dam_10.setText(_translate("MainWindow", "-10", None))
        self.pushButton_Inititave.setText(_translate("MainWindow", "Advance Inititave", None))

