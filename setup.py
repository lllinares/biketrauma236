#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:11:08 2021

@author: llinares
"""

from setuptools import setup
from biketrauma import __version__ as current_version

setup(
  name='biketrauma',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='https://github.com/lllinares/biketrauma236.git',
  author='Laurent Llinares',
  author_email='laurentllinares@laposte.net',
  license='MIT',
  packages=['biketrauma','biketrauma.io', 'biketrauma.preprocess', 'biketrauma.vis'],
  zip_safe=False
)