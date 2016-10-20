#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2010-2013 by Łukasz Langa
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'rb') as ldf:
    long_description = ldf.read().decode('utf8')

# We let it die a horrible tracebacking death if reading the file fails.
# We couldn't sensibly recover anyway: we need the long description.

setup (
    name = 'dj.choices',
    version = '0.11.0',
    author = '\xc5\x81ukasz Langa',
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
        'six',
    ],

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
