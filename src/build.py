#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os

if __name__ == '__main__': 
  from PyInstaller import __main__ 
  params = [
    '-F',
    '-w',
    '--noupx',
    '--clean',
    '--name=demo',
    'gui/db_gui.py',
    # '--add-binary={0};lib'.format(os.path.realpath('lib/ffmpeg.exe')),
    '-y'
  ]
  __main__.run(params)
