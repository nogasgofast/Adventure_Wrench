# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Acadamy_Dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)

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

        self.verticalLayout.addWidget(self.pushButton_new_template)

        self.label_all_templates = QLabel(acadamy_dialog)
        self.label_all_templates.setObjectName(u"label_all_templates")

        self.verticalLayout.addWidget(self.label_all_templates)

        self.horizontalLayout_filter = QHBoxLayout()
        self.horizontalLayout_filter.setObjectName(u"horizontalLayout_filter")
        self.label_filter = QLabel(acadamy_dialog)
        self.label_filter.setObjectName(u"label_filter")

        self.horizontalLayout_filter.addWidget(self.label_filter)

        self.lineEdit_filter = QLineEdit(acadamy_dialog)
        self.lineEdit_filter.setObjectName(u"lineEdit_filter")

        self.horizontalLayout_filter.addWidget(self.lineEdit_filter)


        self.verticalLayout.addLayout(self.horizontalLayout_filter)

        self.listWidget_all_templates = QListWidget(acadamy_dialog)
        self.listWidget_all_templates.setObjectName(u"listWidget_all_templates")

        self.verticalLayout.addWidget(self.listWidget_all_templates)

        self.label_template_details = QLabel(acadamy_dialog)
        self.label_template_details.setObjectName(u"label_template_details")

        self.verticalLayout.addWidget(self.label_template_details)

        self.listWidget_template_detail = QListWidget(acadamy_dialog)
        self.listWidget_template_detail.setObjectName(u"listWidget_template_detail")

        self.verticalLayout.addWidget(self.listWidget_template_detail)

        self.pushButton_back = QPushButton(acadamy_dialog)
        self.pushButton_back.setObjectName(u"pushButton_back")

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
        self.label = QLabel(self.page_splash)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(500, 500))
        self.label.setPixmap(QPixmap(u"../src/ui/mascot.png"))
        self.label.setScaledContents(True)
        self.label.setMargin(50)
        self.label.setIndent(0)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.verticalStackedWidget_forms.addWidget(self.page_splash)
        self.page_new_template = QWidget()
        self.page_new_template.setObjectName(u"page_new_template")
        self.verticalLayout_9 = QVBoxLayout(self.page_new_template)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.page_new_template)
        self.label_2.setObjectName(u"label_2")

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

        self.verticalLayout_9.addWidget(self.label_3)

        self.comboBox_type_templates_page = QComboBox(self.page_new_template)
        self.comboBox_type_templates_page.addItem("")
        self.comboBox_type_templates_page.addItem("")
        self.comboBox_type_templates_page.addItem("")
        self.comboBox_type_templates_page.addItem("")
        self.comboBox_type_templates_page.addItem("")
        self.comboBox_type_templates_page.setObjectName(u"comboBox_type_templates_page")

        self.verticalLayout_9.addWidget(self.comboBox_type_templates_page)

        self.pushButton_add_type_template = QPushButton(self.page_new_template)
        self.pushButton_add_type_template.setObjectName(u"pushButton_add_type_template")

        self.verticalLayout_9.addWidget(self.pushButton_add_type_template)

        self.line_2 = QFrame(self.page_new_template)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_2)

        self.label_4 = QLabel(self.page_new_template)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_9.addWidget(self.label_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_filter_templates_page = QLabel(self.page_new_template)
        self.label_filter_templates_page.setObjectName(u"label_filter_templates_page")

        self.horizontalLayout_2.addWidget(self.label_filter_templates_page)

        self.lineEdit_filter_templates_page = QLineEdit(self.page_new_template)
        self.lineEdit_filter_templates_page.setObjectName(u"lineEdit_filter_templates_page")

        self.horizontalLayout_2.addWidget(self.lineEdit_filter_templates_page)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.comboBox_templates_page = QComboBox(self.page_new_template)
        self.comboBox_templates_page.setObjectName(u"comboBox_templates_page")

        self.verticalLayout_9.addWidget(self.comboBox_templates_page)

        self.pushButton_new_sub_template = QPushButton(self.page_new_template)
        self.pushButton_new_sub_template.setObjectName(u"pushButton_new_sub_template")

        self.verticalLayout_9.addWidget(self.pushButton_new_sub_template)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.pushButton_template_delete = QPushButton(self.page_new_template)
        self.pushButton_template_delete.setObjectName(u"pushButton_template_delete")

        self.verticalLayout_9.addWidget(self.pushButton_template_delete)

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

        self.verticalLayout_2.addWidget(self.textEdit_content_lore)

        self.pushButton_delete_lore = QPushButton(self.page_lore)
        self.pushButton_delete_lore.setObjectName(u"pushButton_delete_lore")

        self.verticalLayout_2.addWidget(self.pushButton_delete_lore)

        self.verticalStackedWidget_forms.addWidget(self.page_lore)
        self.page_attribute_score = QWidget()
        self.page_attribute_score.setObjectName(u"page_attribute_score")
        self.verticalLayout_5 = QVBoxLayout(self.page_attribute_score)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_attribute_score_name = QLabel(self.page_attribute_score)
        self.label_attribute_score_name.setObjectName(u"label_attribute_score_name")

        self.verticalLayout_5.addWidget(self.label_attribute_score_name)

        self.lineEdit_attribute_score_name = QLineEdit(self.page_attribute_score)
        self.lineEdit_attribute_score_name.setObjectName(u"lineEdit_attribute_score_name")

        self.verticalLayout_5.addWidget(self.lineEdit_attribute_score_name)

        self.label_attribute_score = QLabel(self.page_attribute_score)
        self.label_attribute_score.setObjectName(u"label_attribute_score")

        self.verticalLayout_5.addWidget(self.label_attribute_score)

        self.horizontalLayout_score_button_group = QHBoxLayout()
        self.horizontalLayout_score_button_group.setObjectName(u"horizontalLayout_score_button_group")
        self.comboBox_attribute_score = QComboBox(self.page_attribute_score)
        self.comboBox_attribute_score.addItem("")
        self.comboBox_attribute_score.addItem("")
        self.comboBox_attribute_score.addItem("")
        self.comboBox_attribute_score.addItem("")
        self.comboBox_attribute_score.addItem("")
        self.comboBox_attribute_score.addItem("")
        self.comboBox_attribute_score.setObjectName(u"comboBox_attribute_score")

        self.horizontalLayout_score_button_group.addWidget(self.comboBox_attribute_score)

        self.lineEdit_attribute_score = QLineEdit(self.page_attribute_score)
        self.lineEdit_attribute_score.setObjectName(u"lineEdit_attribute_score")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_attribute_score.sizePolicy().hasHeightForWidth())
        self.lineEdit_attribute_score.setSizePolicy(sizePolicy1)
        self.lineEdit_attribute_score.setMaxLength(10)

        self.horizontalLayout_score_button_group.addWidget(self.lineEdit_attribute_score)

        self.pushButton_attribute_score_new = QPushButton(self.page_attribute_score)
        self.pushButton_attribute_score_new.setObjectName(u"pushButton_attribute_score_new")

        self.horizontalLayout_score_button_group.addWidget(self.pushButton_attribute_score_new)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_score_button_group.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_score_button_group)

        self.pushButton_attribute_score_delete = QPushButton(self.page_attribute_score)
        self.pushButton_attribute_score_delete.setObjectName(u"pushButton_attribute_score_delete")

        self.verticalLayout_5.addWidget(self.pushButton_attribute_score_delete)

        self.verticalStackedWidget_forms.addWidget(self.page_attribute_score)
        self.page_attribute = QWidget()
        self.page_attribute.setObjectName(u"page_attribute")
        self.verticalLayout_4 = QVBoxLayout(self.page_attribute)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_attribute_name = QLabel(self.page_attribute)
        self.label_attribute_name.setObjectName(u"label_attribute_name")

        self.verticalLayout_4.addWidget(self.label_attribute_name)

        self.lineEdit_attribute_name = QLineEdit(self.page_attribute)
        self.lineEdit_attribute_name.setObjectName(u"lineEdit_attribute_name")

        self.verticalLayout_4.addWidget(self.lineEdit_attribute_name)

        self.label_attribute_description = QLabel(self.page_attribute)
        self.label_attribute_description.setObjectName(u"label_attribute_description")

        self.verticalLayout_4.addWidget(self.label_attribute_description)

        self.lineEdit_attribute_description = QLineEdit(self.page_attribute)
        self.lineEdit_attribute_description.setObjectName(u"lineEdit_attribute_description")

        self.verticalLayout_4.addWidget(self.lineEdit_attribute_description)

        self.pushButton_attribute_delete = QPushButton(self.page_attribute)
        self.pushButton_attribute_delete.setObjectName(u"pushButton_attribute_delete")

        self.verticalLayout_4.addWidget(self.pushButton_attribute_delete)

        self.verticalStackedWidget_forms.addWidget(self.page_attribute)
        self.page_item = QWidget()
        self.page_item.setObjectName(u"page_item")
        self.verticalLayout_6 = QVBoxLayout(self.page_item)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_item_name = QLabel(self.page_item)
        self.label_item_name.setObjectName(u"label_item_name")

        self.verticalLayout_6.addWidget(self.label_item_name)

        self.lineEdit_item_name = QLineEdit(self.page_item)
        self.lineEdit_item_name.setObjectName(u"lineEdit_item_name")

        self.verticalLayout_6.addWidget(self.lineEdit_item_name)

        self.label_item_weight = QLabel(self.page_item)
        self.label_item_weight.setObjectName(u"label_item_weight")

        self.verticalLayout_6.addWidget(self.label_item_weight)

        self.lineEdit_item_weight = QLineEdit(self.page_item)
        self.lineEdit_item_weight.setObjectName(u"lineEdit_item_weight")

        self.verticalLayout_6.addWidget(self.lineEdit_item_weight)

        self.label__item_description = QLabel(self.page_item)
        self.label__item_description.setObjectName(u"label__item_description")

        self.verticalLayout_6.addWidget(self.label__item_description)

        self.textEdit_item_description = QTextEdit(self.page_item)
        self.textEdit_item_description.setObjectName(u"textEdit_item_description")

        self.verticalLayout_6.addWidget(self.textEdit_item_description)

        self.pushButton_item_roll_table = QPushButton(self.page_item)
        self.pushButton_item_roll_table.setObjectName(u"pushButton_item_roll_table")

        self.verticalLayout_6.addWidget(self.pushButton_item_roll_table)

        self.pushButton_item_random_table = QPushButton(self.page_item)
        self.pushButton_item_random_table.setObjectName(u"pushButton_item_random_table")

        self.verticalLayout_6.addWidget(self.pushButton_item_random_table)

        self.pushButton_item_delete = QPushButton(self.page_item)
        self.pushButton_item_delete.setObjectName(u"pushButton_item_delete")

        self.verticalLayout_6.addWidget(self.pushButton_item_delete)

        self.verticalStackedWidget_forms.addWidget(self.page_item)
        self.page_action = QWidget()
        self.page_action.setObjectName(u"page_action")
        self.verticalLayout_7 = QVBoxLayout(self.page_action)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_action_name = QLabel(self.page_action)
        self.label_action_name.setObjectName(u"label_action_name")

        self.verticalLayout_7.addWidget(self.label_action_name)

        self.lineEdit_action_name = QLineEdit(self.page_action)
        self.lineEdit_action_name.setObjectName(u"lineEdit_action_name")

        self.verticalLayout_7.addWidget(self.lineEdit_action_name)

        self.label_action_description = QLabel(self.page_action)
        self.label_action_description.setObjectName(u"label_action_description")

        self.verticalLayout_7.addWidget(self.label_action_description)

        self.textEdit_action_description = QTextEdit(self.page_action)
        self.textEdit_action_description.setObjectName(u"textEdit_action_description")

        self.verticalLayout_7.addWidget(self.textEdit_action_description)

        self.pushButton_action_delete = QPushButton(self.page_action)
        self.pushButton_action_delete.setObjectName(u"pushButton_action_delete")

        self.verticalLayout_7.addWidget(self.pushButton_action_delete)

        self.verticalStackedWidget_forms.addWidget(self.page_action)
        self.page_dice_roll = QWidget()
        self.page_dice_roll.setObjectName(u"page_dice_roll")
        self.verticalLayout_3 = QVBoxLayout(self.page_dice_roll)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_dice_roll_name = QLabel(self.page_dice_roll)
        self.label_dice_roll_name.setObjectName(u"label_dice_roll_name")

        self.verticalLayout_3.addWidget(self.label_dice_roll_name)

        self.lineEdit_dice_roll_name = QLineEdit(self.page_dice_roll)
        self.lineEdit_dice_roll_name.setObjectName(u"lineEdit_dice_roll_name")

        self.verticalLayout_3.addWidget(self.lineEdit_dice_roll_name)

        self.label_dice_roll_parent = QLabel(self.page_dice_roll)
        self.label_dice_roll_parent.setObjectName(u"label_dice_roll_parent")

        self.verticalLayout_3.addWidget(self.label_dice_roll_parent)

        self.lineEdit_parent_dice_roll = QLineEdit(self.page_dice_roll)
        self.lineEdit_parent_dice_roll.setObjectName(u"lineEdit_parent_dice_roll")
        self.lineEdit_parent_dice_roll.setEnabled(True)
        self.lineEdit_parent_dice_roll.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.lineEdit_parent_dice_roll)

        self.label_dice_roll_range = QLabel(self.page_dice_roll)
        self.label_dice_roll_range.setObjectName(u"label_dice_roll_range")

        self.verticalLayout_3.addWidget(self.label_dice_roll_range)

        self.lineEdit_dice_roll_range = QLineEdit(self.page_dice_roll)
        self.lineEdit_dice_roll_range.setObjectName(u"lineEdit_dice_roll_range")

        self.verticalLayout_3.addWidget(self.lineEdit_dice_roll_range)

        self.pushButton_dice_roll_delete = QPushButton(self.page_dice_roll)
        self.pushButton_dice_roll_delete.setObjectName(u"pushButton_dice_roll_delete")

        self.verticalLayout_3.addWidget(self.pushButton_dice_roll_delete)

        self.verticalStackedWidget_forms.addWidget(self.page_dice_roll)
        self.page_random = QWidget()
        self.page_random.setObjectName(u"page_random")
        self.verticalLayout_8 = QVBoxLayout(self.page_random)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_random_name = QLabel(self.page_random)
        self.label_random_name.setObjectName(u"label_random_name")

        self.verticalLayout_8.addWidget(self.label_random_name)

        self.lineEdit_random_name = QLineEdit(self.page_random)
        self.lineEdit_random_name.setObjectName(u"lineEdit_random_name")
        self.lineEdit_random_name.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.lineEdit_random_name)

        self.pushButton_random_delete = QPushButton(self.page_random)
        self.pushButton_random_delete.setObjectName(u"pushButton_random_delete")

        self.verticalLayout_8.addWidget(self.pushButton_random_delete)

        self.verticalStackedWidget_forms.addWidget(self.page_random)

        self.horizontalLayout.addWidget(self.verticalStackedWidget_forms)


        self.retranslateUi(acadamy_dialog)

        self.verticalStackedWidget_forms.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(acadamy_dialog)
    # setupUi

    def retranslateUi(self, acadamy_dialog):
        acadamy_dialog.setWindowTitle(QCoreApplication.translate("acadamy_dialog", u"Acadamy", None))
        self.pushButton_new_template.setText(QCoreApplication.translate("acadamy_dialog", u"New template", None))
        self.label_all_templates.setText(QCoreApplication.translate("acadamy_dialog", u"Templates", None))
        self.label_filter.setText(QCoreApplication.translate("acadamy_dialog", u"Filter", None))
        self.label_template_details.setText(QCoreApplication.translate("acadamy_dialog", u"Selected Template", None))
        self.pushButton_back.setText(QCoreApplication.translate("acadamy_dialog", u"<- Back (Esc)", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("acadamy_dialog", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("acadamy_dialog", u"Stat block areas:", None))
        self.comboBox_type_templates_page.setItemText(0, QCoreApplication.translate("acadamy_dialog", u"Lore", None))
        self.comboBox_type_templates_page.setItemText(1, QCoreApplication.translate("acadamy_dialog", u"Ability Scores", None))
        self.comboBox_type_templates_page.setItemText(2, QCoreApplication.translate("acadamy_dialog", u"Attributes", None))
        self.comboBox_type_templates_page.setItemText(3, QCoreApplication.translate("acadamy_dialog", u"Items", None))
        self.comboBox_type_templates_page.setItemText(4, QCoreApplication.translate("acadamy_dialog", u"Actions", None))

        self.pushButton_add_type_template.setText(QCoreApplication.translate("acadamy_dialog", u"Add", None))
        self.label_4.setText(QCoreApplication.translate("acadamy_dialog", u"Stack a template on top of this one", None))
        self.label_filter_templates_page.setText(QCoreApplication.translate("acadamy_dialog", u"Filter", None))
        self.pushButton_new_sub_template.setText(QCoreApplication.translate("acadamy_dialog", u"Stack", None))
        self.pushButton_template_delete.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.label_name_lore.setText(QCoreApplication.translate("acadamy_dialog", u"Lore Name", None))
        self.label_description_lore.setText(QCoreApplication.translate("acadamy_dialog", u"Lore description", None))
        self.pushButton_delete_lore.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.label_attribute_score_name.setText(QCoreApplication.translate("acadamy_dialog", u"Attribute_score template name", None))
        self.label_attribute_score.setText(QCoreApplication.translate("acadamy_dialog", u"score template", None))
        self.comboBox_attribute_score.setItemText(0, QCoreApplication.translate("acadamy_dialog", u"Strength", None))
        self.comboBox_attribute_score.setItemText(1, QCoreApplication.translate("acadamy_dialog", u"Dexterity", None))
        self.comboBox_attribute_score.setItemText(2, QCoreApplication.translate("acadamy_dialog", u"Constitution", None))
        self.comboBox_attribute_score.setItemText(3, QCoreApplication.translate("acadamy_dialog", u"Wisdom", None))
        self.comboBox_attribute_score.setItemText(4, QCoreApplication.translate("acadamy_dialog", u"Intelligence", None))
        self.comboBox_attribute_score.setItemText(5, QCoreApplication.translate("acadamy_dialog", u"Charisma", None))

#if QT_CONFIG(tooltip)
        self.lineEdit_attribute_score.setToolTip(QCoreApplication.translate("acadamy_dialog", u"can have + or - to add or remove points from the base score. Or without them the value is replaced", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_attribute_score_new.setText(QCoreApplication.translate("acadamy_dialog", u"Add", None))
        self.pushButton_attribute_score_delete.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.label_attribute_name.setText(QCoreApplication.translate("acadamy_dialog", u"Name", None))
        self.label_attribute_description.setText(QCoreApplication.translate("acadamy_dialog", u"description (optional)", None))
        self.pushButton_attribute_delete.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.label_item_name.setText(QCoreApplication.translate("acadamy_dialog", u"Item Name", None))
        self.label_item_weight.setText(QCoreApplication.translate("acadamy_dialog", u"Item Weight", None))
        self.label__item_description.setText(QCoreApplication.translate("acadamy_dialog", u"<html><head/><body>Description: (Allows %d,%e) </body></html>", None))
        self.pushButton_item_roll_table.setText(QCoreApplication.translate("acadamy_dialog", u"Add roll table", None))
        self.pushButton_item_random_table.setText(QCoreApplication.translate("acadamy_dialog", u"Add random table", None))
        self.pushButton_item_delete.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.label_action_name.setText(QCoreApplication.translate("acadamy_dialog", u"Action name", None))
        self.label_action_description.setText(QCoreApplication.translate("acadamy_dialog", u"Description: %d, %e for auto damage and elemental damage", None))
        self.pushButton_action_delete.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.label_dice_roll_name.setText(QCoreApplication.translate("acadamy_dialog", u"Roll table name", None))
        self.label_dice_roll_parent.setText(QCoreApplication.translate("acadamy_dialog", u"dice roll", None))
        self.label_dice_roll_range.setText(QCoreApplication.translate("acadamy_dialog", u"Range: written 5-10 or 20 subtituting your own numbers of coarse.", None))
        self.pushButton_dice_roll_delete.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
        self.label_random_name.setText(QCoreApplication.translate("acadamy_dialog", u"Random table name", None))
        self.pushButton_random_delete.setText(QCoreApplication.translate("acadamy_dialog", u"Delete", None))
    # retranslateUi

