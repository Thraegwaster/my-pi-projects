#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 20:48:49 2025

@author: chris
"""

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(factorial(20))