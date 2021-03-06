#!/usr/bin/env python

from setuptools import setup

with open('pubs/version.py') as f:
    exec(f.read())  # defines __version__

setup(
    name='pubs',
    version=__version__,
    author='Fabien Benureau, Olivier Mangin, Jonathan Grizou',
    author_email='fabien.benureau@gmail.com',
    maintainer='Olivier Mangin',
    url='https://github.com/pubs/pubs',

    description='command-line scientific bibliography manager',
    packages=['pubs',
              'pubs.config',
              'pubs.commands',
              'pubs.templates',
              'pubs.plugs',
              'pubs.plugs.alias'],
    entry_points={
        'console_scripts': [
            'pubs=pubs.pubs_cmd:execute',
            ],
        },

    install_requires=['pyyaml', 'bibtexparser>=1.0', 'python-dateutil',
                      'requests', 'configobj', 'beautifulsoup4'],
    tests_require=['pyfakefs>=2.7', 'mock'],
    extras_require={'autocompletion': ['argcomplete'],
                    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
    ],

    # in order to avoid 'zipimport.ZipImportError: bad local file header'
    zip_safe=False,

)
