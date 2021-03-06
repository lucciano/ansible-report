#!/usr/bin/env python

import os
import sys
import glob

__requires__ = ['SQLAlchemy >= 0.7']
import pkg_resources

sys.path.append( os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'lib') )

from ansiblereport import __version__, __author__, __name__
from distutils.core import setup

data_files = []
plugins = []
ANSIBLE_PLUGIN_PATH = 'share/ansible_plugins/callback_plugins'
for path in glob.glob(os.path.join('plugins', 'callback_plugins', '*.py')):
    plugins.append(path)
data_files.append((ANSIBLE_PLUGIN_PATH, plugins))

plugins = []
OUTPUT_PLUGIN_PATH = 'share/ansible-report/plugins'
for path in glob.glob(os.path.join('plugins', 'output_plugins', '*.py')):
    plugins.append(path)
data_files.append((OUTPUT_PLUGIN_PATH, plugins))

print "output plugins=%s" % data_files

setup(name=__name__,
      version=__version__,
      author=__author__,
      author_email='sfromm@gmail.com',
      url='https://github.com/sfromm/ansible-report',
      description='Utility to log and report ansible activity',
      license='GPLv3',
      package_dir={ 'ansiblereport': 'lib/ansiblereport' },
      packages=['ansiblereport'],
      scripts=['bin/ansible-report'],
      data_files=data_files,
      install_requires=['SQLAlchemy>=0.6', 'alembic', 'dateutil'],
)
