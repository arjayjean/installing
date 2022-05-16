#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess

subprocess.run('clear')

install = input('What are you installing: ')

installation = ['python3', '-m', 'pip', 'install', install]

subprocess.run(installation)