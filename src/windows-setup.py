from cx_Freeze import setup, Executable
from version import ver
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
includefiles = [('supported_systems/5e.ini','supported_systems/'), 
                ('supported_systems/5e.jinja','supported_systems/'),
                ('save/default.sqlite','save')]
build_options = {'packages': [], 'excludes':: [], 'includes':['pony.orm.dbproviders.sqlite'], 'include_files':includefiles}

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('main.py', base=base, target_name='adventure_wrench')
]

setup(name='adventure_wrench',
      version=ver,
      description='5E compatible initiative tracker and template builder',
      options={'build_exe': build_options},
      executables=executables)
