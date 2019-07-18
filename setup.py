#!/usr/bin/env python

from setuptools import setup

setup(name = 'skyss',
      author = 'Equinor ASA by Kristian Reed',
      version='0.1',
      packages=['skyss'],
      install_requires = ['requests'],
      description='skyss --- Find timetable for public transport in Bergen',
      entry_points = {'console_scripts': ['skyss=skyss:main']}

      )