# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Acadamy_Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFormLayout, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStackedWidget, QTextEdit, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)
import images_rc

class Ui_acadamy_dialog(object):
    def setupUi(self, acadamy_dialog):
        if not acadamy_dialog.objectName():
            acadamy_dialog.setObjectName(u"acadamy_dialog")
        acadamy_dialog.resize(1056, 587)
        self.horizontalLayout = QHBoxLayout(acadamy_dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_new_template = QPushButton(acadamy_dialog)
        self.pushButton_new_template.setObjectName(u"pushButton_new_template")
        self.pushButton_new_template.setAutoDefault(False)

        self.verticalLayout.addWidget(self.pushButton_new_template)

        self.label_template_details = QLabel(acadamy_dialog)
        self.label_template_details.setObjectName(u"label_template_details")

        self.verticalLayout.addWidget(self.label_template_details)

        self.treeWidget_all_templates = QTreeWidget(acadamy_dialog)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget_all_templates.setHeaderItem(__qtreewidgetitem)
        self.treeWidget_all_templates.setObjectName(u"treeWidget_all_templates")
        self.treeWidget_all_templates.setStyleSheet(u"")
        self.treeWidget_all_templates.setHeaderHidden(True)

        self.verticalLayout.addWidget(self.treeWidget_all_templates)

        self.pushButton_back = QPushButton(acadamy_dialog)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setAutoDefault(False)

        self.verticalLayout.addWidget(self.pushButton_back)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.line = QFrame(acadamy_dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.verticalStackedWidget_forms = QStackedWidget(acadamy_dialog)
        self.verticalStackedWidget_forms.setObjectName(u"verticalStackedWidget_forms")
        self.page_splash = QWidget()
        self.page_splash.setObjectName(u"page_splash")
        self.formLayout = QFormLayout(self.page_splash)
        self.formLayout.setObjectName(u"formLayout")
        self.label_splash = QLabel(self.page_splash)
        self.label_splash.setObjectName(u"label_splash")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_splash.sizePolicy().hasHeightForWidth())
        self.label_splash.setSizePolicy(sizePolicy)
        self.label_splash.setMaximumSize(QSize(500, 500))
        self.label_splash.setPixmap(QPixmap(u":/images/mascot.png"))
        self.label_splash.setScaledContents(True)
        self.label_splash.setMargin(50)
        self.label_splash.setIndent(0)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_splash)

        self.verticalStackedWidget_forms.addWidget(self.page_splash)
        self.page_new_template = QWidget()
        self.page_new_template.setObjectName(u"page_new_template")
        self.verticalLayout_9 = QVBoxLayout(self.page_new_template)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.page_new_template)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_9.addWidget(self.label_2)

        self.lineEdit_template_name = QLineEdit(self.page_new_template)
        self.lineEdit_template_name.setObjectName(u"lineEdit_template_name")

        self.verticalLayout_9.addWidget(self.lineEdit_template_name)

        self.line_3 = QFrame(self.page_new_template)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_3)

        self.label_3 = QLabel(self.page_new_template)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_9.addWidget(self.label_3)

        self.comboBox_type_templates_page = QComboBox(self.page_new_template)
        self.comboBox_type_templates_page.addItem("")
        self.comboBox_type_templates_page.addItem("")
        self.comboBox_type_templates_page.addItem("")
        self.comboBox_type_templates_page.addItem("")
        self.comboBox_type_templates_page.addItem("")
        self.comboBox_type_templates_page.addItem("")
        self.comboBox_type_templates_page.setObjectName(u"comboBox_type_templates_page")

        self.verticalLayout_9.addWidget(self.comboBox_type_templates_page)

        self.pushButton_add_detail = QPushButton(self.page_new_template)
        self.pushButton_add_detail.setObjectName(u"pushButton_add_detail")
        self.pushButton_add_detail.setAutoDefault(False)

        self.verticalLayout_9.addWidget(self.pushButton_add_detail)

        self.line_2 = QFrame(self.page_new_template)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)

        self.label_4 = QLabel(self.page_new_template)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_9.addWidget(self.label_4)

        self.comboBox_stack_template = QComboBox(self.page_new_template)
        self.comboBox_stack_template.setObjectName(u"comboBox_stack_template")

        self.verticalLayout_9.addWidget(self.comboBox_stack_template)

        self.pushButton_stack_template = QPushButton(self.page_new_template)
        self.pushButton_stack_template.setObjectName(u"pushButton_stack_template")
        self.pushButton_stack_template.setAutoDefault(False)

        self.verticalLayout_9.addWidget(self.pushButton_stack_template)

        self.line_4 = QFrame(self.page_new_template)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_4)

        self.label_13 = QLabel(self.page_new_template)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setTextFormat(Qt.MarkdownText)

        self.verticalLayout_9.addWidget(self.label_13)

        self.pushButton_randomize_template = QPushButton(self.page_new_template)
        self.pushButton_randomize_template.setObjectName(u"pushButton_randomize_template")
        self.pushButton_randomize_template.setAutoDefault(False)

        self.verticalLayout_9.addWidget(self.pushButton_randomize_template)

        self.checkBox_is_folder_template = QCheckBox(self.page_new_template)
        self.checkBox_is_folder_template.setObjectName(u"checkBox_is_folder_template")

        self.verticalLayout_9.addWidget(self.checkBox_is_folder_template)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_add_another_template = QPushButton(self.page_new_template)
        self.pushButton_add_another_template.setObjectName(u"pushButton_add_another_template")
        self.pushButton_add_another_template.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.pushButton_add_another_template)

        self.pushButton_delete_template = QPushButton(self.page_new_template)
        self.pushButton_delete_template.setObjectName(u"pushButton_delete_template")
        self.pushButton_delete_template.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.pushButton_delete_template)

        self.pushButton_next_template = QPushButton(self.page_new_template)
        self.pushButton_next_template.setObjectName(u"pushButton_next_template")
        self.pushButton_next_template.setEnabled(False)
        self.pushButton_next_template.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.pushButton_next_template)


        self.verticalLayout_9.addLayout(self.horizontalLayout_4)

        self.verticalStackedWidget_forms.addWidget(self.page_new_template)
        self.page_lore = QWidget()
        self.page_lore.setObjectName(u"page_lore")
        self.verticalLayout_2 = QVBoxLayout(self.page_lore)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_name_lore = QLabel(self.page_lore)
        self.label_name_lore.setObjectName(u"label_name_lore")

        self.verticalLayout_2.addWidget(self.label_name_lore)

        self.lineEdit_name_lore = QLineEdit(self.page_lore)
        self.lineEdit_name_lore.setObjectName(u"lineEdit_name_lore")

        self.verticalLayout_2.addWidget(self.lineEdit_name_lore)

        self.label_description_lore = QLabel(self.page_lore)
        self.label_description_lore.setObjectName(u"label_description_lore")

        self.verticalLayout_2.addWidget(self.label_description_lore)

        self.textEdit_content_lore = QTextEdit(self.page_lore)
        self.textEdit_content_lore.setObjectName(u"textEdit_content_lore")
        self.textEdit_content_lore.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_2.addWidget(self.textEdit_content_lore)

        self.horizontalLayout_buttons_lore = QHBoxLayout()
        self.horizontalLayout_buttons_lore.setObjectName(u"horizontalLayout_buttons_lore")
        self.pushButton_add_another_lore = QPushButton(self.page_lore)
        self.pushButton_add_another_lore.setObjectName(u"pushButton_add_another_lore")
        self.pushButton_add_another_lore.setAutoDefault(False)

        self.horizontalLayout_buttons_lore.addWidget(self.pushButton_add_another_lore)

        self.pushButton_delete_lore = QPushButton(self.page_lore)
        self.pushButton_delete_lore.setObjectName(u"pushButton_delete_lore")
        self.pushButton_delete_lore.setAutoDefault(False)

        self.horizontalLayout_buttons_lore.addWidget(self.pushButton_delete_lore)

        self.pushButton_next_lore = QPushButton(self.page_lore)
        self.pushButton_next_lore.setObjectName(u"pushButton_next_lore")
        self.pushButton_next_lore.setAutoDefault(False)

        self.horizontalLayout_buttons_lore.addWidget(self.pushButton_next_lore)


        self.verticalLayout_2.addLayout(self.horizontalLayout_buttons_lore)

        self.verticalStackedWidget_forms.addWidget(self.page_lore)
        self.page_stats = QWidget()
        self.page_stats.setObjectName(u"page_stats")
        self.verticalLayout_5 = QVBoxLayout(self.page_stats)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_name_stats = QLabel(self.page_stats)
        self.label_name_stats.setObjectName(u"label_name_stats")

        self.verticalLayout_5.addWidget(self.label_name_stats)

        self.comboBox_name_stats = QComboBox(self.page_stats)
        self.comboBox_name_stats.addItem("")
        self.comboBox_name_stats.addItem("")
        self.comboBox_name_stats.addItem("")
        self.comboBox_name_stats.addItem("")
        self.comboBox_name_stats.addItem("")
        self.comboBox_name_stats.addItem("")
        self.comboBox_name_stats.addItem("")
        self.comboBox_name_stats.addItem("")
        self.comboBox_name_stats.setObjectName(u"comboBox_name_stats")

        self.verticalLayout_5.addWidget(self.comboBox_name_stats)

        self.label_des1_stats = QLabel(self.page_stats)
        self.label_des1_stats.setObjectName(u"label_des1_stats")

        self.verticalLayout_5.addWidget(self.label_des1_stats)

        self.label_des3_stats = QLabel(self.page_stats)
        self.label_des3_stats.setObjectName(u"label_des3_stats")

        self.verticalLayout_5.addWidget(self.label_des3_stats)

        self.lineEdit_content_stats = QLineEdit(self.page_stats)
        self.lineEdit_content_stats.setObjectName(u"lineEdit_content_stats")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_content_stats.sizePolicy().hasHeightForWidth())
        self.lineEdit_content_stats.setSizePolicy(sizePolicy1)
        self.lineEdit_content_stats.setMaxLength(10)

        self.verticalLayout_5.addWidget(self.lineEdit_content_stats)

        self.verticalSpacer_stats = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_stats)

        self.horizontalLayout_buttons_stats = QHBoxLayout()
        self.horizontalLayout_buttons_stats.setObjectName(u"horizontalLayout_buttons_stats")
        self.pushButton_add_another_stats = QPushButton(self.page_stats)
        self.pushButton_add_another_stats.setObjectName(u"pushButton_add_another_stats")
        self.pushButton_add_another_stats.setAutoDefault(False)

        self.horizontalLayout_buttons_stats.addWidget(self.pushButton_add_another_stats)

        self.pushButton_delete_stats = QPushButton(self.page_stats)
        self.pushButton_delete_stats.setObjectName(u"pushButton_delete_stats")
        self.pushButton_delete_stats.setAutoDefault(False)

        self.horizontalLayout_buttons_stats.addWidget(self.pushButton_delete_stats)

        self.pushButton_next_stats = QPushButton(self.page_stats)
        self.pushButton_next_stats.setObjectName(u"pushButton_next_stats")
        self.pushButton_next_stats.setAutoDefault(False)

        self.horizontalLayout_buttons_stats.addWidget(self.pushButton_next_stats)


        self.verticalLayout_5.addLayout(self.horizontalLayout_buttons_stats)

        self.verticalStackedWidget_forms.addWidget(self.page_stats)
        self.page_attribute = QWidget()
        self.page_attribute.setObjectName(u"page_attribute")
        self.verticalLayout_4 = QVBoxLayout(self.page_attribute)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_name_attribute = QLabel(self.page_attribute)
        self.label_name_attribute.setObjectName(u"label_name_attribute")

        self.verticalLayout_4.addWidget(self.label_name_attribute)

        self.lineEdit_name_attribute = QLineEdit(self.page_attribute)
        self.lineEdit_name_attribute.setObjectName(u"lineEdit_name_attribute")

        self.verticalLayout_4.addWidget(self.lineEdit_name_attribute)

        self.label_attribute_description = QLabel(self.page_attribute)
        self.label_attribute_description.setObjectName(u"label_attribute_description")

        self.verticalLayout_4.addWidget(self.label_attribute_description)

        self.lineEdit_content_attribute = QLineEdit(self.page_attribute)
        self.lineEdit_content_attribute.setObjectName(u"lineEdit_content_attribute")

        self.verticalLayout_4.addWidget(self.lineEdit_content_attribute)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_buttons_attribute = QHBoxLayout()
        self.horizontalLayout_buttons_attribute.setObjectName(u"horizontalLayout_buttons_attribute")
        self.pushButton_add_another_attribute = QPushButton(self.page_attribute)
        self.pushButton_add_another_attribute.setObjectName(u"pushButton_add_another_attribute")
        self.pushButton_add_another_attribute.setAutoDefault(False)

        self.horizontalLayout_buttons_attribute.addWidget(self.pushButton_add_another_attribute)

        self.pushButton_delete_attribute = QPushButton(self.page_attribute)
        self.pushButton_delete_attribute.setObjectName(u"pushButton_delete_attribute")
        self.pushButton_delete_attribute.setAutoDefault(False)

        self.horizontalLayout_buttons_attribute.addWidget(self.pushButton_delete_attribute)

        self.pushButton_next_attribute = QPushButton(self.page_attribute)
        self.pushButton_next_attribute.setObjectName(u"pushButton_next_attribute")
        self.pushButton_next_attribute.setAutoDefault(False)

        self.horizontalLayout_buttons_attribute.addWidget(self.pushButton_next_attribute)


        self.verticalLayout_4.addLayout(self.horizontalLayout_buttons_attribute)

        self.verticalStackedWidget_forms.addWidget(self.page_attribute)
        self.page_item = QWidget()
        self.page_item.setObjectName(u"page_item")
        self.verticalLayout_6 = QVBoxLayout(self.page_item)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_name_item = QLabel(self.page_item)
        self.label_name_item.setObjectName(u"label_name_item")

        self.verticalLayout_6.addWidget(self.label_name_item)

        self.lineEdit_name_item = QLineEdit(self.page_item)
        self.lineEdit_name_item.setObjectName(u"lineEdit_name_item")

        self.verticalLayout_6.addWidget(self.lineEdit_name_item)

        self.label_weight_item = QLabel(self.page_item)
        self.label_weight_item.setObjectName(u"label_weight_item")

        self.verticalLayout_6.addWidget(self.label_weight_item)

        self.lineEdit_weight_item = QLineEdit(self.page_item)
        self.lineEdit_weight_item.setObjectName(u"lineEdit_weight_item")

        self.verticalLayout_6.addWidget(self.lineEdit_weight_item)

        self.label_quantity_item = QLabel(self.page_item)
        self.label_quantity_item.setObjectName(u"label_quantity_item")

        self.verticalLayout_6.addWidget(self.label_quantity_item)

        self.spinBox_quantity_item = QSpinBox(self.page_item)
        self.spinBox_quantity_item.setObjectName(u"spinBox_quantity_item")

        self.verticalLayout_6.addWidget(self.spinBox_quantity_item)

        self.label_description_item = QLabel(self.page_item)
        self.label_description_item.setObjectName(u"label_description_item")

        self.verticalLayout_6.addWidget(self.label_description_item)

        self.textEdit_description_item = QTextEdit(self.page_item)
        self.textEdit_description_item.setObjectName(u"textEdit_description_item")
        self.textEdit_description_item.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_6.addWidget(self.textEdit_description_item)

        self.horizontalLayout_buttons_item = QHBoxLayout()
        self.horizontalLayout_buttons_item.setObjectName(u"horizontalLayout_buttons_item")
        self.pushButton_add_another_item = QPushButton(self.page_item)
        self.pushButton_add_another_item.setObjectName(u"pushButton_add_another_item")
        self.pushButton_add_another_item.setAutoDefault(False)

        self.horizontalLayout_buttons_item.addWidget(self.pushButton_add_another_item)

        self.pushButton_delete_item = QPushButton(self.page_item)
        self.pushButton_delete_item.setObjectName(u"pushButton_delete_item")
        self.pushButton_delete_item.setAutoDefault(False)

        self.horizontalLayout_buttons_item.addWidget(self.pushButton_delete_item)

        self.pushButton_next_item = QPushButton(self.page_item)
        self.pushButton_next_item.setObjectName(u"pushButton_next_item")
        self.pushButton_next_item.setAutoDefault(False)

        self.horizontalLayout_buttons_item.addWidget(self.pushButton_next_item)


        self.verticalLayout_6.addLayout(self.horizontalLayout_buttons_item)

        self.verticalStackedWidget_forms.addWidget(self.page_item)
        self.page_action = QWidget()
        self.page_action.setObjectName(u"page_action")
        self.verticalLayout_7 = QVBoxLayout(self.page_action)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_name_action = QLabel(self.page_action)
        self.label_name_action.setObjectName(u"label_name_action")

        self.verticalLayout_7.addWidget(self.label_name_action)

        self.lineEdit_name_action = QLineEdit(self.page_action)
        self.lineEdit_name_action.setObjectName(u"lineEdit_name_action")

        self.verticalLayout_7.addWidget(self.lineEdit_name_action)

        self.label_cost_action = QLabel(self.page_action)
        self.label_cost_action.setObjectName(u"label_cost_action")

        self.verticalLayout_7.addWidget(self.label_cost_action)

        self.lineEdit_cost_action = QLineEdit(self.page_action)
        self.lineEdit_cost_action.setObjectName(u"lineEdit_cost_action")

        self.verticalLayout_7.addWidget(self.lineEdit_cost_action)

        self.label_limitations_action = QLabel(self.page_action)
        self.label_limitations_action.setObjectName(u"label_limitations_action")

        self.verticalLayout_7.addWidget(self.label_limitations_action)

        self.lineEdit_limitations_action = QLineEdit(self.page_action)
        self.lineEdit_limitations_action.setObjectName(u"lineEdit_limitations_action")

        self.verticalLayout_7.addWidget(self.lineEdit_limitations_action)

        self.label_description_action = QLabel(self.page_action)
        self.label_description_action.setObjectName(u"label_description_action")

        self.verticalLayout_7.addWidget(self.label_description_action)

        self.textEdit_result_action = QTextEdit(self.page_action)
        self.textEdit_result_action.setObjectName(u"textEdit_result_action")
        self.textEdit_result_action.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_7.addWidget(self.textEdit_result_action)

        self.horizontalLayout_buttons_action = QHBoxLayout()
        self.horizontalLayout_buttons_action.setObjectName(u"horizontalLayout_buttons_action")
        self.pushButton_add_another_action = QPushButton(self.page_action)
        self.pushButton_add_another_action.setObjectName(u"pushButton_add_another_action")
        self.pushButton_add_another_action.setAutoDefault(False)

        self.horizontalLayout_buttons_action.addWidget(self.pushButton_add_another_action)

        self.pushButton_delete_action = QPushButton(self.page_action)
        self.pushButton_delete_action.setObjectName(u"pushButton_delete_action")
        self.pushButton_delete_action.setAutoDefault(False)

        self.horizontalLayout_buttons_action.addWidget(self.pushButton_delete_action)

        self.pushButton_next_action = QPushButton(self.page_action)
        self.pushButton_next_action.setObjectName(u"pushButton_next_action")
        self.pushButton_next_action.setAutoDefault(False)

        self.horizontalLayout_buttons_action.addWidget(self.pushButton_next_action)


        self.verticalLayout_7.addLayout(self.horizontalLayout_buttons_action)

        self.verticalStackedWidget_forms.addWidget(self.page_action)
        self.page_roll_table = QWidget()
        self.page_roll_table.setObjectName(u"page_roll_table")
        self.verticalLayout_3 = QVBoxLayout(self.page_roll_table)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_name_roll_table = QLabel(self.page_roll_table)
        self.label_name_roll_table.setObjectName(u"label_name_roll_table")

        self.verticalLayout_3.addWidget(self.label_name_roll_table)

        self.lineEdit_name_roll_table = QLineEdit(self.page_roll_table)
        self.lineEdit_name_roll_table.setObjectName(u"lineEdit_name_roll_table")

        self.verticalLayout_3.addWidget(self.lineEdit_name_roll_table)

        self.label_8 = QLabel(self.page_roll_table)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)

        self.label_11 = QLabel(self.page_roll_table)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_3.addWidget(self.label_11)

        self.label = QLabel(self.page_roll_table)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.label_10 = QLabel(self.page_roll_table)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)

        self.label_5 = QLabel(self.page_roll_table)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.label_6 = QLabel(self.page_roll_table)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_3.addWidget(self.label_6)

        self.label_7 = QLabel(self.page_roll_table)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_3.addWidget(self.label_7)

        self.label_dice_roll_table = QLabel(self.page_roll_table)
        self.label_dice_roll_table.setObjectName(u"label_dice_roll_table")

        self.verticalLayout_3.addWidget(self.label_dice_roll_table)

        self.lineEdit_dice_roll_table = QLineEdit(self.page_roll_table)
        self.lineEdit_dice_roll_table.setObjectName(u"lineEdit_dice_roll_table")
        self.lineEdit_dice_roll_table.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_dice_roll_table.sizePolicy().hasHeightForWidth())
        self.lineEdit_dice_roll_table.setSizePolicy(sizePolicy2)
        self.lineEdit_dice_roll_table.setMinimumSize(QSize(100, 0))
        self.lineEdit_dice_roll_table.setReadOnly(False)

        self.verticalLayout_3.addWidget(self.lineEdit_dice_roll_table)

        self.label_table_roll_table = QLabel(self.page_roll_table)
        self.label_table_roll_table.setObjectName(u"label_table_roll_table")

        self.verticalLayout_3.addWidget(self.label_table_roll_table)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_item_match_roll_table = QLineEdit(self.page_roll_table)
        self.lineEdit_item_match_roll_table.setObjectName(u"lineEdit_item_match_roll_table")
        sizePolicy2.setHeightForWidth(self.lineEdit_item_match_roll_table.sizePolicy().hasHeightForWidth())
        self.lineEdit_item_match_roll_table.setSizePolicy(sizePolicy2)
        self.lineEdit_item_match_roll_table.setMinimumSize(QSize(10, 0))
        self.lineEdit_item_match_roll_table.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.lineEdit_item_match_roll_table)

        self.comboBox_options_roll_table = QComboBox(self.page_roll_table)
        self.comboBox_options_roll_table.setObjectName(u"comboBox_options_roll_table")
        sizePolicy1.setHeightForWidth(self.comboBox_options_roll_table.sizePolicy().hasHeightForWidth())
        self.comboBox_options_roll_table.setSizePolicy(sizePolicy1)
        self.comboBox_options_roll_table.setEditable(True)

        self.horizontalLayout_3.addWidget(self.comboBox_options_roll_table)

        self.pushButton_add_item_roll_table = QPushButton(self.page_roll_table)
        self.pushButton_add_item_roll_table.setObjectName(u"pushButton_add_item_roll_table")
        sizePolicy2.setHeightForWidth(self.pushButton_add_item_roll_table.sizePolicy().hasHeightForWidth())
        self.pushButton_add_item_roll_table.setSizePolicy(sizePolicy2)
        self.pushButton_add_item_roll_table.setMinimumSize(QSize(1, 0))
        self.pushButton_add_item_roll_table.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_add_item_roll_table)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.listWidget_table_roll_table = QListWidget(self.page_roll_table)
        self.listWidget_table_roll_table.setObjectName(u"listWidget_table_roll_table")
        self.listWidget_table_roll_table.setSortingEnabled(True)

        self.verticalLayout_3.addWidget(self.listWidget_table_roll_table)

        self.pushButton_delete_item_roll_table = QPushButton(self.page_roll_table)
        self.pushButton_delete_item_roll_table.setObjectName(u"pushButton_delete_item_roll_table")

        self.verticalLayout_3.addWidget(self.pushButton_delete_item_roll_table)

        self.checkBox_israndom_roll_table = QCheckBox(self.page_roll_table)
        self.checkBox_israndom_roll_table.setObjectName(u"checkBox_israndom_roll_table")

        self.verticalLayout_3.addWidget(self.checkBox_israndom_roll_table)

        self.checkBox_interpret_roll_table = QCheckBox(self.page_roll_table)
        self.checkBox_interpret_roll_table.setObjectName(u"checkBox_interpret_roll_table")

        self.verticalLayout_3.addWidget(self.checkBox_interpret_roll_table)

        self.horizontalLayout_button_roll_table = QHBoxLayout()
        self.horizontalLayout_button_roll_table.setObjectName(u"horizontalLayout_button_roll_table")
        self.pushButton_add_another_roll_table = QPushButton(self.page_roll_table)
        self.pushButton_add_another_roll_table.setObjectName(u"pushButton_add_another_roll_table")
        self.pushButton_add_another_roll_table.setAutoDefault(False)

        self.horizontalLayout_button_roll_table.addWidget(self.pushButton_add_another_roll_table)

        self.pushButton_delete_roll_table = QPushButton(self.page_roll_table)
        self.pushButton_delete_roll_table.setObjectName(u"pushButton_delete_roll_table")
        self.pushButton_delete_roll_table.setAutoDefault(False)

        self.horizontalLayout_button_roll_table.addWidget(self.pushButton_delete_roll_table)

        self.pushButton_next_roll_table = QPushButton(self.page_roll_table)
        self.pushButton_next_roll_table.setObjectName(u"pushButton_next_roll_table")
        self.pushButton_next_roll_table.setAutoDefault(False)

        self.horizontalLayout_button_roll_table.addWidget(self.pushButton_next_roll_table)


        self.verticalLayout_3.addLayout(self.horizontalLayout_button_roll_table)

        self.verticalStackedWidget_forms.addWidget(self.page_roll_table)

        self.horizontalLayout.addWidget(self.verticalStackedWidget_forms)


        self.retranslateUi(acadamy_dialog)

        self.verticalStackedWidget_forms.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(acadamy_dialog)
    # setupUi

    def retranslateUi(self, acadamy_dialog):
        acadamy_dialog.setWindowTitle(QCoreApplication.translate("acadamy_dialog", u"Acadamy", None))
        self.pushButton_new_template.setText(QCoreApplication.translate("acadamy_dialog", u"New template", None))
        self.label_template_details.setText(QCoreApplication.translate("acadamy_dialog", u"Templates", None))
        self.pushButton_back.setText(QCoreApplication.translate("acadamy_dialog", u"<- Save (Esc)", None))
        self.label_splash.setText("")
        self.label_2.setText(QCoreApplication.translate("acadamy_dialog", u"#### Template Name", None))
        self.label_3.setText(QCoreApplication.translate("acadamy_dialog", u"#### Add details to this template:", None))
        self.comboBox_type_templates_page.setItemText(0, QCoreApplication.translate("acadamy_dialog", u"Lore", None))
        self.comboBox_type_templates_page.setItemText(1, QCoreApplication.translate("acadamy_dialog", u"Stat Modification", None))
        self.comboBox_type_templates_page.setItemText(2, QCoreApplication.translate("acadamy_dialog", u"Attributes", None))
        self.comboBox_type_templates_page.setItemText(3, QCoreApplication.translate("acadamy_dialog", u"Items", None))
        self.comboBox_type_templates_page.setItemText(4, QCoreApplication.translate("acadamy_dialog", u"Actions", None))
        self.comboBox_type_templates_page.setItemText(5, QCoreApplication.translate("acadamy_dialog", u"Roll Table", None))

        self.pushButton_add_detail.setText(QCoreApplication.translate("acadamy_dialog", u"Add", None))
        self.label_4.setText(QCoreApplication.translate("acadamy_dialog", u"#### Combine Templates", None))
        self.pushButton_stack_template.setText(QCoreApplication.translate("acadamy_dialog", u"Stack", None))
        self.label_13.setText(QCoreApplication.translate("acadamy_dialog", u"#### Randomizer", None))
#if QT_CONFIG(tooltip)
        self.pushButton_randomize_template.setToolTip(QCoreApplication.translate("acadamy_dialog", u"converts this template to a folder and uses it's contents to build a randomized template", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.pushButton_randomize_template.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.pushButton_randomize_template.setText(QCoreApplication.translate("acadamy_dialog", u"Convert to Randomized Template", None))
        self.checkBox_is_folder_template.setText(QCoreApplication.translate("acadamy_dialog", u"Folder toggle. Removes template from template only lists.", None))
        self.pushButton_add_another_template.setText(QCoreApplication.translate("acadamy_dialog", u"Add Another", None))
        self.pushButton_delete_template.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.pushButton_next_template.setText(QCoreApplication.translate("acadamy_dialog", u"Next", None))
        self.label_name_lore.setText(QCoreApplication.translate("acadamy_dialog", u"Name", None))
        self.label_description_lore.setText(QCoreApplication.translate("acadamy_dialog", u"Lore description", None))
        self.pushButton_add_another_lore.setText(QCoreApplication.translate("acadamy_dialog", u"Add Another", None))
        self.pushButton_delete_lore.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.pushButton_next_lore.setText(QCoreApplication.translate("acadamy_dialog", u"Next", None))
        self.label_name_stats.setText(QCoreApplication.translate("acadamy_dialog", u"Stat Modification:", None))
        self.comboBox_name_stats.setItemText(0, QCoreApplication.translate("acadamy_dialog", u"Strength", None))
        self.comboBox_name_stats.setItemText(1, QCoreApplication.translate("acadamy_dialog", u"Dexterity", None))
        self.comboBox_name_stats.setItemText(2, QCoreApplication.translate("acadamy_dialog", u"Constitution", None))
        self.comboBox_name_stats.setItemText(3, QCoreApplication.translate("acadamy_dialog", u"Wisdom", None))
        self.comboBox_name_stats.setItemText(4, QCoreApplication.translate("acadamy_dialog", u"Intelligence", None))
        self.comboBox_name_stats.setItemText(5, QCoreApplication.translate("acadamy_dialog", u"Charisma", None))
        self.comboBox_name_stats.setItemText(6, QCoreApplication.translate("acadamy_dialog", u"Hit Points", None))
        self.comboBox_name_stats.setItemText(7, QCoreApplication.translate("acadamy_dialog", u"Armor Class", None))

        self.label_des1_stats.setText("")
        self.label_des3_stats.setText(QCoreApplication.translate("acadamy_dialog", u"If it starts with a \"+\" or \"-\" symbol it adds or subtracts instead of replacing.", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_content_stats.setToolTip(QCoreApplication.translate("acadamy_dialog", u"can have + or - to add or remove points from the base score. Or without them the value is replaced", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_content_stats.setWhatsThis(QCoreApplication.translate("acadamy_dialog", u"<html><head/><body><p>accepts one number from 0  to 30. A template with a number set as a stat will override the stat to be that number. The number may have a minus or plus symbol directly before it. If a minus or plus is used the previous value of the stat is added to this value. But will stay within the range 0 to 30. </p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton_add_another_stats.setText(QCoreApplication.translate("acadamy_dialog", u"Add Another", None))
        self.pushButton_delete_stats.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.pushButton_next_stats.setText(QCoreApplication.translate("acadamy_dialog", u"Next", None))
        self.label_name_attribute.setText(QCoreApplication.translate("acadamy_dialog", u"Attribute Name", None))
        self.label_attribute_description.setText(QCoreApplication.translate("acadamy_dialog", u"Attribute description (optional)", None))
        self.pushButton_add_another_attribute.setText(QCoreApplication.translate("acadamy_dialog", u"Add Another", None))
        self.pushButton_delete_attribute.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.pushButton_next_attribute.setText(QCoreApplication.translate("acadamy_dialog", u"Next", None))
        self.label_name_item.setText(QCoreApplication.translate("acadamy_dialog", u"Item Name", None))
        self.label_weight_item.setText(QCoreApplication.translate("acadamy_dialog", u"Weight (optional)", None))
        self.label_quantity_item.setText(QCoreApplication.translate("acadamy_dialog", u"Quantity", None))
        self.label_description_item.setText(QCoreApplication.translate("acadamy_dialog", u"<html><head/><body><p>Item description: (allows %d,%e) </p></body></html>", None))
        self.pushButton_add_another_item.setText(QCoreApplication.translate("acadamy_dialog", u"Add Another", None))
        self.pushButton_delete_item.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.pushButton_next_item.setText(QCoreApplication.translate("acadamy_dialog", u"Next", None))
        self.label_name_action.setText(QCoreApplication.translate("acadamy_dialog", u"Action Name", None))
        self.label_cost_action.setText(QCoreApplication.translate("acadamy_dialog", u"Cost, i.e. \"1 dimond worth 1000gp\" or \"1 action\" or \"1 bonus action\"", None))
        self.label_limitations_action.setText(QCoreApplication.translate("acadamy_dialog", u"Limitations, i.e. \"targets cone area\" or \"range 20/60 feet\" ", None))
#if QT_CONFIG(tooltip)
        self.label_description_action.setToolTip(QCoreApplication.translate("acadamy_dialog", u"<html><head/><body><p>%a gets replaced automaticly with level appropriate attack</p><p>%d and %e get replaced with level appropriate damage</p><p>You can divide the damage into smaller portions by adding a number to the end. i.e. %d2 is half damage %d9 is 1/9th damage. the only valid numbers are [2-9]. </p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_description_action.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.label_description_action.setText(QCoreApplication.translate("acadamy_dialog", u"Result: allows %a, %d, and %e. Hover over this for help.", None))
        self.pushButton_add_another_action.setText(QCoreApplication.translate("acadamy_dialog", u"Add Another", None))
        self.pushButton_delete_action.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.pushButton_next_action.setText(QCoreApplication.translate("acadamy_dialog", u"Next", None))
        self.label_name_roll_table.setText(QCoreApplication.translate("acadamy_dialog", u"Roll Table Name:", None))
        self.label_8.setText(QCoreApplication.translate("acadamy_dialog", u"In the shop, when a roll table is applied to something. Adventure Wrench", None))
        self.label_11.setText(QCoreApplication.translate("acadamy_dialog", u"rolls dice for you, and writes all matching entries into the stat block.", None))
        self.label.setText(QCoreApplication.translate("acadamy_dialog", u"Example:", None))
        self.label_10.setText(QCoreApplication.translate("acadamy_dialog", u"1d6  :", None))
        self.label_5.setText(QCoreApplication.translate("acadamy_dialog", u"1       : Great Axe", None))
        self.label_6.setText(QCoreApplication.translate("acadamy_dialog", u"2-4   : Chicken Breast", None))
        self.label_7.setText(QCoreApplication.translate("acadamy_dialog", u"5,6   : Bannana Bazooka", None))
        self.label_dice_roll_table.setText(QCoreApplication.translate("acadamy_dialog", u"Dice to Roll:", None))
        self.label_table_roll_table.setText(QCoreApplication.translate("acadamy_dialog", u"Match this         : What to add to the template if matched.", None))
        self.pushButton_add_item_roll_table.setText(QCoreApplication.translate("acadamy_dialog", u"+", None))
        self.pushButton_delete_item_roll_table.setText(QCoreApplication.translate("acadamy_dialog", u"Remove selected from list", None))
        self.checkBox_israndom_roll_table.setText(QCoreApplication.translate("acadamy_dialog", u"Select from the list randomly <Dice to Roll> times.", None))
        self.checkBox_interpret_roll_table.setText(QCoreApplication.translate("acadamy_dialog", u"This is Not a template, just write this stuff into the stat block.", None))
        self.pushButton_add_another_roll_table.setText(QCoreApplication.translate("acadamy_dialog", u"Add Another", None))
        self.pushButton_delete_roll_table.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.pushButton_next_roll_table.setText(QCoreApplication.translate("acadamy_dialog", u"Next", None))
    # retranslateUi

