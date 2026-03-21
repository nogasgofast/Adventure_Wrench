#!/usr/bin/env python

import re
import sys
import requests
import subprocess
from src.version import ver

def check_github(ver):
    'Checking for latest version'
    print(f"src/version.py target: {ver}")
    r = requests.get("https://api.github.com/repos/nogasgofast/Adventure_Wrench/tags")
    version = None
    for release in r.json():
        if release['name'] == ver:
            print(f"Tag found on Github")
            return ver, release['commit']['sha']
    exit('Error: src/version.py not latest tag in github!')

def check_file(fname, ver):
    with open(f'{fname}', 'r') as f:
        m = re.search(f'\\b{ver}\\b', f.read())
        if m:
            print(f'tag in {fname}')
        else:
            exit(f'Error: {fname} missing {ver}!')
     
# validation
ver, commit = check_github(ver)
check_file('net.nogasgofast.adventure_wrench.yml', ver)
check_file('net.nogasgofast.adventure_wrench.yml', commit)
check_file('src/net.nogasgofast.adventure_wrench.metainfo.xml', ver)

# helpful reminders
print("the main github branch will always have the correct version")
print("however it will not have the correct commit reference as that is not possible before the commit.")
print("so remember the commit must be updated after submitting changes, before testing the prod build")


if '--check' in sys.argv:
    exit()
elif '--help' in sys.argv or '-h' in sys.argv:
    exit("--check : check versions in files only")
else:
    cmd = 'flatpak run --command=flathub-build org.flatpak.Builder --force-clean --disable-rofiles-fuse --user --install net.nogasgofast.adventure_wrench.yml'
    print(cmd)
    subprocess.run(cmd.split(' '))
    
    print(cmd)
    cmd = 'flatpak run --command=flatpak-builder-lint org.flatpak.Builder manifest net.nogasgofast.adventure_wrench.yml'
    subprocess.run(cmd.split(' '))
