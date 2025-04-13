#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 14:16:31 2025

@author: chris
"""

# This is implemented using formatted string literals, or fstrings

n = 1
fstr = f"{n} divided by 3 is {n/3}"
print(fstr)

# Round the output to 4 d.p.
fstr2 = f"{n} divided by 3 is {n/3 :.4}"

# .3f means round to 3 dp and output
fstr3 = f"{12.34567 :.3f}"

# 7.3f means the output will be 7 characters long, right justified
fstr4 = f"{12.34567 :7.3f}"

# 3d means that 3 digits are reserved for an integer decimal number.
fstr5 = f"{12 :3d}"

print(fstr3)
print(fstr4)
print(fstr5)