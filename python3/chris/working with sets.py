#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 20:34:27 2025

@author: chris
"""

# These are little-found in the wild.

st={3,1,2,2,3}

print(st)

# A Python set is an unordered collection of items.
# There's no element position, nor are there duplicates of elements.


print(len(st))

print(2 in st) # test for membership

b = {4,2,3}
print(b)

print(st|b) # Union
print(st & b) # Intersection
print(st - b) # Difference

# The "comprehension" syntax, seen in lists, applies to the type set.
# a - b above, could have been written this way...

c = {x for x in st if x not in b}
print(c)