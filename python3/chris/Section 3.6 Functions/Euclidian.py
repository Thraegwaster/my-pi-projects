#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 15:31:59 2025

@author: chris
"""

# Finds the HCF of a pair of numbers
def gcd(a,b): return a if b == 0 else gcd(b, a%b)