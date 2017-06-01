# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/Configurator.ui'
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
        configurator.resize(921, 552)
        configurator.setStyleSheet(_fromUtf8("QpushButton { margin: 0,0,0,25 px; }"))
        self.verticalLayout = QtGui.QVBoxLayout(configurator)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_attributes = QtGui.QPushButton(configurator)
        self.pushButton_attributes.setObjectName(_fromUtf8("pushButton_attributes"))
        self.horizontalLayout_2.addWidget(self.pushButton_attributes)
        self.pushButton_weapons = QtGui.QPushButton(configurator)
        self.pushButton_weapons.setObjectName(_fromUtf8("pushButton_weapons"))
        self.horizontalLayout_2.addWidget(self.pushButton_weapons)
        self.pushButton_misc = QtGui.QPushButton(configurator)
        self.pushButton_misc.setObjectName(_fromUtf8("pushButton_misc"))
        self.horizontalLayout_2.addWidget(self.pushButton_misc)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_add = QtGui.QPushButton(configurator)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.horizontalLayout_2.addWidget(self.pushButton_add)
        self.pushButton_reset = QtGui.QPushButton(configurator)
        self.pushButton_reset.setObjectName(_fromUtf8("pushButton_reset"))
        self.horizontalLayout_2.addWidget(self.pushButton_reset)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_options = QtGui.QLabel(configurator)
        self.label_options.setObjectName(_fromUtf8("label_options"))
        self.horizontalLayout.addWidget(self.label_options)
        self.line = QtGui.QFrame(configurator)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.label_selection = QtGui.QLabel(configurator)
        self.label_selection.setObjectName(_fromUtf8("label_selection"))
        self.horizontalLayout.addWidget(self.label_selection)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit_search = QtGui.QLineEdit(configurator)
        self.lineEdit_search.setObjectName(_fromUtf8("lineEdit_search"))
        self.verticalLayout_2.addWidget(self.lineEdit_search)
        self.listWidget_catagory = QtGui.QListWidget(configurator)
        self.listWidget_catagory.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_catagory.setObjectName(_fromUtf8("listWidget_catagory"))
        self.verticalLayout_2.addWidget(self.listWidget_catagory)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.listWidget_options = QtGui.QListWidget(configurator)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_options.sizePolicy().hasHeightForWidth())
        self.listWidget_options.setSizePolicy(sizePolicy)
        self.listWidget_options.setStyleSheet(_fromUtf8("QpushButton { margin-left: 25px; }"))
        self.listWidget_options.setObjectName(_fromUtf8("listWidget_options"))
        self.horizontalLayout_3.addWidget(self.listWidget_options)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_back = QtGui.QPushButton(configurator)
        self.pushButton_back.setObjectName(_fromUtf8("pushButton_back"))
        self.verticalLayout.addWidget(self.pushButton_back)

        self.retranslateUi(configurator)
        QtCore.QMetaObject.connectSlotsByName(configurator)

    def retranslateUi(self, configurator):
        configurator.setWindowTitle(_translate("configurator", "Characteristics", None))
        self.pushButton_attributes.setText(_translate("configurator", "Abilities", None))
        self.pushButton_weapons.setText(_translate("configurator", "Weapons", None))
        self.pushButton_misc.setText(_translate("configurator", "Misc.", None))
        self.pushButton_add.setText(_translate("configurator", "Add", None))
        self.pushButton_reset.setText(_translate("configurator", "Reset", None))
        self.label_options.setText(_translate("configurator", "Search and select Items here.", None))
        self.label_selection.setText(_translate("configurator", "View and dubble-click to un-select things.", None))
        self.lineEdit_search.setPlaceholderText(_translate("configurator", "Search", None))
        self.pushButton_back.setText(_translate("configurator", "Back (esc)", None))

