#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 20:52:09 2025

@author: chris
"""

# Consider the function
def double(x):
    return 2*x

# This could have equivalently have been written
lambda x: 2*x

print((lambda x: 2*x)(4))

# Functions as arguments