#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 15:56:02 2025

@author: chris
"""

# This implementation is surprisingly concise.
def qsort(lst):
    if lst == []: return []
    p = lst[0]  # pivot element
    sml = qsort([x for x in lst[1:] if x < p])
    grt = qsort([x for x in lst[1:] if x >= p])
    return sml + [p] + grt