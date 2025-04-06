#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 18:46:54 2025

@author: chris
"""
import math as m

lst1 = [3,5,7,9]
lst2 = [8,6,22,58]
print(lst1 + lst2)

squares1 = [x**2 for x in lst1]

logs1 = [m.log(x) for x in lst2]

print(f"Here are some squares: {squares1}")

print(f"Here are some logs: {logs1}")

# We can make it conditional

lst3 = [2,7,3,-5]

logs2 = [m.log(x) for x in lst3 if x >= 0]
print(logs2)