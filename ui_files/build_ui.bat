#!/bin/sh

py -m pyside6-uic Main_Window.ui -o ../src/ui/Main_Window.py
py -m pyside6-uic Player_Dialog.ui -o ../src/ui/Player_Dialog.py
py -m pyside6-uic TheShop_Dialog.ui -o ../src/ui/TheShop_Dialog.py
py -m pyside6-uic Vault_Dialog.ui -o ../src/ui/Vault_Dialog.py
py -m pyside6-uic Acadamy_Dialog.ui -o ../src/ui/Acadamy_Dialog.py
py -m pyside6-rcc images.qrc -o ../src/images_rc.py
