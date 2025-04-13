#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 21:33:07 2025

@author: chris
"""

n = int(input("Enter a number: "))
while n > 1:
    if n % 2 == 0:
        n //=2
    else:
        n = 3 * n + 1
        print(n)
print("reached 1")