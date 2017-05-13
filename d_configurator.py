# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/Config_Dialog.ui'
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

class Ui_configurator(object):
    def setupUi(self, configurator):
        configurator.setObjectName(_fromUtf8("configurator"))
        configurator.resize(599, 416)
        self.horizontalLayoutWidget = QtGui.QWidget(configurator)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 581, 341))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.listView_configs = QtGui.QListView(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView_configs.sizePolicy().hasHeightForWidth())
        self.listView_configs.setSizePolicy(sizePolicy)
        self.listView_configs.setObjectName(_fromUtf8("listView_configs"))
        self.horizontalLayout_3.addWidget(self.listView_configs)
        self.listView_properties_2 = QtGui.QListView(self.horizontalLayoutWidget)
        self.listView_properties_2.setObjectName(_fromUtf8("listView_properties_2"))
        self.horizontalLayout_3.addWidget(self.listView_properties_2)
        self.layoutWidget_2 = QtGui.QWidget(configurator)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 581, 30))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_attributes = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_attributes.setObjectName(_fromUtf8("pushButton_attributes"))
        self.horizontalLayout_2.addWidget(self.pushButton_attributes)
        self.pushButton_weapons = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_weapons.setObjectName(_fromUtf8("pushButton_weapons"))
        self.horizontalLayout_2.addWidget(self.pushButton_weapons)
        self.pushButton_misc = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton_misc.setObjectName(_fromUtf8("pushButton_misc"))
        self.horizontalLayout_2.addWidget(self.pushButton_misc)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtGui.QPushButton(self.layoutWidget_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(configurator)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 380, 90, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(configurator)
        QtCore.QMetaObject.connectSlotsByName(configurator)

    def retranslateUi(self, configurator):
        configurator.setWindowTitle(_translate("configurator", "Dialog", None))
        self.pushButton_attributes.setText(_translate("configurator", "Abilities", None))
        self.pushButton_weapons.setText(_translate("configurator", "Weapons", None))
        self.pushButton_misc.setText(_translate("configurator", "Misc_Actions", None))
        self.pushButton.setText(_translate("configurator", "Reset", None))
        self.pushButton_2.setText(_translate("configurator", "Back (esc)", None))

