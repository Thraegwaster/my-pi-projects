#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 20:22:47 2025

@author: chris
"""

# This is an example of using a function as an argument to another function.
# Computes the maximum value of a function f on n+1 equidistant points
# 0/n, 1/n, 2/n, ... , n/n

def vmax(f,n):
    max_y = f(0)
    h = 1.0/n
    for i in range(1, n+1):
        y = f(i*h)
        if y > max_y: max_y = y
    return max_y
    