"""
Test driver for Program 18
Fall 2021
"""

import pandas as pd
import numpy as np
import p18

'''
Quick test of dropNeg():
'''
x = list(range(-5,5))
y = np.ones(10)
#Expected output:
#For inputs: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4] and [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
print(f'For inputs: {x} and {y}')
xp, yp = p18.dropNeg(x,y)
#Expected output:
#dropNeg() is (1, 2, 3, 4) and (1.0, 1.0, 1.0, 1.0)
print(f'dropNeg() is {xp} and {yp}')


'''
Quick test of logScale():
'''
xl, yl = p18.logScale(xp,yp)
#Expected output:
#Log scale of (1, 2, 3, 4) is [0.         0.69314718 1.09861229 1.38629436]
#Log scale of (1.0, 1.0, 1.0, 1.0) is [0. 0. 0. 0.]
print(f'Log scale of {xp} is {xl}')
print(f'Log scale of {yp} is {yl}')
