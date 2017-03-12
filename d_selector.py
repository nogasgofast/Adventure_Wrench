# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/Selector_Dialog.ui'
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

class Ui_Selector(object):
    def setupUi(self, Selector):
        Selector.setObjectName(_fromUtf8("Selector"))
        Selector.resize(400, 621)
        self.gridLayout = QtGui.QGridLayout(Selector)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listWidget_Plugins = QtGui.QListWidget(Selector)
        self.listWidget_Plugins.setStyleSheet(_fromUtf8("font: 75 12pt \"Cantarell\";\n"
"font-weight: bold;"))
        self.listWidget_Plugins.setAlternatingRowColors(True)
        self.listWidget_Plugins.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_Plugins.setObjectName(_fromUtf8("listWidget_Plugins"))
        self.gridLayout.addWidget(self.listWidget_Plugins, 0, 0, 1, 1)

        self.retranslateUi(Selector)
        QtCore.QMetaObject.connectSlotsByName(Selector)

    def retranslateUi(self, Selector):
        Selector.setWindowTitle(_translate("Selector", "Dialog", None))

