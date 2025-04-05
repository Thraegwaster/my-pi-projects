#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 20:54:00 2025

@author: chris
"""

# For integers Python has the data type int. It apparently
# can store arbitrarily large values.

print("Here is 2 to the power of 100:")
print(2**100)

# 'Small' numbers are handled by the processor. Large numbers are handled
# by Python itself.

# The limit is 2^63-1. It can be queried by

import sys
print(sys.maxsize)

print("""The finite representation of real numbers is the fundamental problem
      in numerical mathematics, regardless of how many bits are used.""")

print(f"{0.1 :.17f}")

print("It can be seen in apparently harmless expressions: 0.1 + 0.2 = 0.3?")

print(0.1+0.2==0.3)

print("\nThe moral of the story is never test floats for equality!\n")

print("The number of representable decimal digits is ",sys.float_info.dig)

print("Let's take a closer look at what happens when we print the left hand side\n")
print("and right hand side of the above equation:")
print(f"{0.1 + 0.2 :.17f}")
print(f"{0.3 :.17f}")