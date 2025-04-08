#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 15:37:02 2025

@author: chris
"""

# The Ackermann function plays a fundamental role in the mathematical theory
# of computability.

def ack(x,y):
    if x == 0: return y + 1
    if y == 0: return ack(x-1,1)
    return ack(x-1, ack(x, y-1))