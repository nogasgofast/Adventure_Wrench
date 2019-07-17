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
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_options = QtGui.QLabel(configurator)
        self.label_options.setObjectName(_fromUtf8("label_options"))
        self.horizontalLayout.addWidget(self.label_options)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineEdit_search = QtGui.QLineEdit(configurator)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_search.sizePolicy().hasHeightForWidth())
        self.lineEdit_search.setSizePolicy(sizePolicy)
        self.lineEdit_search.setMaximumSize(QtCore.QSize(452, 16777215))
        self.lineEdit_search.setBaseSize(QtCore.QSize(0, 0))
        self.lineEdit_search.setObjectName(_fromUtf8("lineEdit_search"))
        self.horizontalLayout_2.addWidget(self.lineEdit_search)
        self.label_selection = QtGui.QLabel(configurator)
        self.label_selection.setObjectName(_fromUtf8("label_selection"))
        self.horizontalLayout_2.addWidget(self.label_selection)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.listWidget_catagory = QtGui.QListWidget(configurator)
        self.listWidget_catagory.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_catagory.setObjectName(_fromUtf8("listWidget_catagory"))
        self.verticalLayout_4.addWidget(self.listWidget_catagory)
        self.pushButton_add = QtGui.QPushButton(configurator)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.verticalLayout_4.addWidget(self.pushButton_add)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.listWidget_options = QtGui.QListWidget(configurator)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_options.sizePolicy().hasHeightForWidth())
        self.listWidget_options.setSizePolicy(sizePolicy)
        self.listWidget_options.setStyleSheet(_fromUtf8("QpushButton { margin-left: 25px; }"))
        self.listWidget_options.setObjectName(_fromUtf8("listWidget_options"))
        self.verticalLayout_3.addWidget(self.listWidget_options)
        self.pushButton_reset = QtGui.QPushButton(configurator)
        self.pushButton_reset.setObjectName(_fromUtf8("pushButton_reset"))
        self.verticalLayout_3.addWidget(self.pushButton_reset)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton_back = QtGui.QPushButton(configurator)
        self.pushButton_back.setObjectName(_fromUtf8("pushButton_back"))
        self.verticalLayout.addWidget(self.pushButton_back)

        self.retranslateUi(configurator)
        QtCore.QMetaObject.connectSlotsByName(configurator)

    def retranslateUi(self, configurator):
        configurator.setWindowTitle(_translate("configurator", "Characteristics", None))
        self.label_options.setText(_translate("configurator", "Search and select Items here.", None))
        self.lineEdit_search.setPlaceholderText(_translate("configurator", "Search", None))
        self.label_selection.setText(_translate("configurator", "Collected selections here:", None))
        self.pushButton_add.setToolTip(_translate("configurator", "Add an item to the list", None))
        self.pushButton_add.setText(_translate("configurator", "Add", None))
        self.pushButton_reset.setText(_translate("configurator", "Reset", None))
        self.pushButton_back.setText(_translate("configurator", "Back (Esc)", None))

