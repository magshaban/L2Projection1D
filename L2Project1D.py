# This is the main file.
# this code can be used to find the L2 projection of a given function in 1D.

import numpy as np

from MassMatrix import *
from loadvecx import * 
from plotpf import *

x = np.linspace(-1,1,32)  # the vector x

M = MassMat1D(x)
inverse_M = np.linalg.inv(M) #the inverse of the Matrix M 
b = LoadVec1D(x)

Pf = inverse_M@b    

print('x= \n',x)
print('b= \n', LoadVec1D(x))
print('M = \n',MassMat1D(x))
print('Pf= \n' ,Pf)

plotall(x,Pf,M)