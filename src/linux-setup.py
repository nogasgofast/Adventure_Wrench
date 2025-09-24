from cx_Freeze import setup, Executable
from version import ver

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 
                 'excludes': [], 
                 'includes':['pony.orm.dbproviders.sqlite'],
                 'include_files': [("net.nogasgofast.rpg.adventure_wrench.desktop",
                                   "share/applications/net.nogasgofast.rpg.adventure_wrench.desktop"),
                                  ("net.nogasgofast.rpg.adventure_wrench.metainfo.xml",
                                   "share/metainfo/net.nogasgofast.rpg.adventure_wrench.metainfo.xml"),
                                  ("net.nogasgofast.rpg.adventure_wrench.png",
                                   "share/icons/hicolor/256x256/apps/net.nogasgofast.rpg.adventure_wrench.png")]
                 }

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, target_name = 'adventure_wrench')
]

setup(name='adventure_wrench',
      version = ver,
      description = 'offline encounter tracker and builder for laptops.',
      options = {'build_exe': build_options},
      executables = executables,
      includes = ['pony.orm.dbproviders'])


