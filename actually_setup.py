#!/usr/bin/env python
#####################################################################################
#Copyright (C) <2012>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in the
#Software without restriction, including without limitation the rights to use, copy,
#modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
#and to permit persons to whom the Software is furnished to do so, subject to
#the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies
#or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#####################################################################################
import setuptools
import os
import glob

here = os.path.realpath(os.path.dirname(__file__))
scripts = os.path.join(here, 'breadcrumbs', 'scripts', '*.py')
scripts = glob.glob(scripts)

setuptools.setup(
    name='breadcrumbs',
    author="Timothy Tickle",
    author_email="ttickle@sph.harvard.edu",
    license="MIT",
    version='0.8.0',
    description='Assorted metagenomics tools',
    packages=setuptools.find_packages(exclude=['ez_setup', 'tests', 'tests.*']),
    zip_safe=False,
    scripts=scripts,
    classifiers=[
        "Development Status :: 4 - Beta"
    ],
)
