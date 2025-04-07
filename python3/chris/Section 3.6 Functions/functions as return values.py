#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 20:39:26 2025

@author: chris
"""

# Functions as return values

# We define a derivative operator ddx that , for an input function f,
# computes an approximation to the derivative f' according to the standard
# formula for the gradient.

def ddx(f):
    h = 1.e-6
    def f_prime(x): return (f(x+h) - f(x))/h
    return f_prime

def g(x): return 4*x*(1-x)
print(ddx(g)(0.3))  # out should be 1.5999960000234736
dgdx = ddx(g)
print(dgdx(0.5))    # out should be -4.0000225354219765e-06