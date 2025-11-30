# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Legend_Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Legend(object):
    def setupUi(self, Legend):
        if not Legend.objectName():
            Legend.setObjectName(u"Legend")
        Legend.resize(537, 419)
        self.verticalLayout_2 = QVBoxLayout(Legend)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget_legend = QListWidget(Legend)
        self.listWidget_legend.setObjectName(u"listWidget_legend")

        self.verticalLayout_2.addWidget(self.listWidget_legend)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_legend_close = QPushButton(Legend)
        self.pushButton_legend_close.setObjectName(u"pushButton_legend_close")

        self.horizontalLayout.addWidget(self.pushButton_legend_close)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Legend)

        QMetaObject.connectSlotsByName(Legend)
    # setupUi

    def retranslateUi(self, Legend):
        Legend.setWindowTitle(QCoreApplication.translate("Legend", u"Legend", None))
        self.pushButton_legend_close.setText(QCoreApplication.translate("Legend", u"Close (Esc)", None))
    # retranslateUi

