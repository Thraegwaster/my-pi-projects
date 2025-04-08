#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 20:58:47 2025

@author: chris
"""

def factorial_rec(n):
    if n == 1: return 1
    return n*factorial_rec(n-1)