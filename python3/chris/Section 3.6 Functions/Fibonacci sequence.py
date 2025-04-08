#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 15:34:48 2025

@author: chris
"""

# Computes the Fibonnaci sequence
def fib(n): return 1 if n == 1 or n == 2 else fib(n-1) + fib(n-2)

# Here we encounter a composite test condition.