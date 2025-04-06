#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 21:54:33 2025

@author: chris
"""

n = 100                      # input upper limit
L = list(range(2,n+1))      # constructs a list from range
P = []                      # [] denotes the empty list
while L != []:
    p = L[0]                # The smallest number still in L
    P.append(p)             # is appended to the end of P
    for i in L:
        if i % p == 0:
            L.remove(i)
print(P)