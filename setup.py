#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2010 Łukasz Langa
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys
from setuptools import setup, find_packages

reload(sys)
sys.setdefaultencoding('utf8')

ld_file = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
try:
    long_description = ld_file.read()
finally:
    ld_file.close()
# We let it die a horrible tracebacking death if reading the file fails.
# We couldn't sensibly recover anyway: we need the long description.

setup (
    name = 'dj.choices',
    version = '0.8.4',
    author = 'Łukasz Langa',
    author_email = 'lukasz@langa.pl',
    description = "An enum implementation for Django forms and models.",
    long_description = long_description,
    url = 'https://github.com/ambv/dj.choices/',
    keywords = 'django dj extra contrib choices enum enumeration',
    platforms = ['any'],
    license = 'MIT',
    package_dir = {'': 'src'},
    packages = find_packages('src'),
    include_package_data = True,
    zip_safe = False, # if only because of the readme file
    namespace_packages = ['dj'],
    install_requires = [
        'django',
    ],

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )
