#!/usr/bin/env python

"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/lipsyncpost/lspython
"""

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path
import sys
sys.path.insert(0, path.abspath('../pygrid'))

from pygrid_ui import version

__VERSION__ = version

here = path.abspath(path.dirname(__file__))
# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get Version Info

#
setup(
    name='pygrid_ui',
    version=__VERSION__,
    description='GridEngine monitor GUI',
    long_description=long_description,
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: GridEngine :: Grid Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    url='https://github.com/compso/pygrid',
    author='Ashley Retallack',
    author_email='ashleyr.retallack@gmail.com',
    license='MIT',
    keywords='gridengine python submitter',
    packages=["pygrid_ui"],
    install_requires=["pygrid", "pyside2"],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={
    #    'sample': ['package_data.dat'],
    #},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'pyqmon=pygrid_ui:main',
        ],
        #'gui_scripts': [
        #    'makeout=makeout.view.makeout_view:main',
        #]
    },
    options={
        'build_scripts': {
            'executable': '/bin/custom_python',
        },
    },
    include_package_data=True,
    zip_safe=False
)
