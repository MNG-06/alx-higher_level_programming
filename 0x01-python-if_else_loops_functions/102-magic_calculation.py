#!/usr/bin/python3
# 102-magic_calculation.py
# MNG-06 <mphela.mminanare@gmail.com>

def magic_calculation(a, b, c):
    """Match bytecode provided by ALXSE."""
    if a < b:
        return (c)
    if c > b:
        return (a + b)
    return (a*b - c)
