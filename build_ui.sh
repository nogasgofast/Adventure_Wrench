#!/bin/sh

python3 -m PyQt5.uic.pyuic ui_files/Template_Dialog.ui -o d_template_editor.py
python3 -m PyQt5.uic.pyuic ui_files/Configurator.ui -o d_configurator.py
python3 -m PyQt5.uic.pyuic ui_files/Player_Dialog.ui -o d_player.py
python3 -m PyQt5.uic.pyuic ui_files/Vault_Dialog.ui -o d_vault.py
python3 -m PyQt5.uic.pyuic ui_files/Main_Window.ui -o w_main.py
