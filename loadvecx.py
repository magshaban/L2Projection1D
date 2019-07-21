# The main file is L2Projection1D.py
# This function is to evaluate the Load vector b in 1D for X 

import numpy as np
from funcx import *

def LoadVec1D(x):
    n = len(x) - 1          # number of elemnts 
    b = np.zeros((n+1,1))   # allocate b matrix
    
    for i in range(n):
        h = x[i+1] - x[i]
        b[i] += foo([x[i]])*h/2
        b[i+1] += foo([x[i+1]])*h/2
    return b
