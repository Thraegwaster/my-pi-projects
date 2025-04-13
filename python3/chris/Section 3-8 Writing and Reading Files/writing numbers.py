#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 15:02:02 2025

@author: chris
"""

# Only strings can be written to files, not numbers.
tbl= [[1,2,3],[4,5,6]]
tblstring = ''
for num in r:
    tblstring += f" {num}"
    tblstring += '\n'

filewrite = open("/home/chris/Documents/coding/my-pi-projects/python3/chris/Section 3-8 Writing and Reading Files/numbers.txt", 'w')

