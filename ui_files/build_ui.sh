#!/bin/sh

#python3 -m PyQt5.uic.pyuic ui_files/Template_Dialog.ui -o d_template_editor.py
#python3 -m PyQt5.uic.pyuic ui_files/Configurator.ui -o d_configurator.py
#python3 -m PyQt5.uic.pyuic ui_files/Player_Dialog.ui -o d_player.py
#python3 -m PyQt5.uic.pyuic ui_files/Vault_Dialog.ui -o d_vault.py
#python3 -m PyQt5.uic.pyuic ui_files/Main_Window.ui -o w_main.py

pyside6-uic add_config_option.ui > ../src/add_config_option.py
pyside6-uic Configurator.ui > ../src/Configurator.py
pyside6-uic Main_Window.ui > ../src/Main_Window.py
pyside6-uic Player_Dialog.ui > ../src/Player_Dialog.py
pyside6-uic template_actions.ui > ../src/template_actions.py
pyside6-uic template_attributes.ui > ../src/template_attributes.py
pyside6-uic template_descriptions.ui > ../src/template_descriptions.py
pyside6-uic Template_Dialog.ui > ../src/Template_Dialog.py
pyside6-uic Template_finder.ui > ../src/Template_finder.py
pyside6-uic template_items.ui > ../src/template_items.py
pyside6-uic template_roll_table.ui > ../src/template_roll_table.py
pyside6-uic template_stats.ui > ../src/template_stats.py
pyside6-uic Vault_Dialog.ui > ../src/Vault_Dialog.py


