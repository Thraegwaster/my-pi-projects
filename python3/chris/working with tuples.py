#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 18:53:52 2025

@author: chris
"""

# Unlike lists, tuples are immutable.

t1 = (1,2,3,4)

# The parentheses can be left out...
t2 = 5,6,7,8

# Let's say you're going to define a single element tuple,
# you need a comma following the element
t2 = (7,)

# If you did t2 = (7) you'd just get an int.
print(t2)