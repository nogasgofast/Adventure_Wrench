#!/bin/sh

#python3 -m PyQt5.uic.pyuic ui_files/Template_Dialog.ui -o d_template_editor.py
#python3 -m PyQt5.uic.pyuic ui_files/Configurator.ui -o d_configurator.py
#python3 -m PyQt5.uic.pyuic ui_files/Player_Dialog.ui -o d_player.py
#python3 -m PyQt5.uic.pyuic ui_files/Vault_Dialog.ui -o d_vault.py
#python3 -m PyQt5.uic.pyuic ui_files/Main_Window.ui -o w_main.py

pyside6-uic Main_Window.ui > ../src/ui/Main_Window.py
pyside6-uic Player_Dialog.ui > ../src/ui/Player_Dialog.py
pyside6-uic Template_Dialog.ui > ../src/ui/Template_Dialog.py
pyside6-uic Vault_Dialog.ui > ../src/ui/Vault_Dialog.py
pyside6-uic TheShop_Dialog.ui > ../src/ui/TheShop_Dialog.py
pyside6-uic Acadamy_Dialog.ui > ../src/ui/Acadamy_Dialog.py
