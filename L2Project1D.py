#This is the chapter one codes in the FEM book of Larson.
#this is educational project to get myself familiar with FEM implementation and git.

import numpy as np

from MassMatrix import *
from loadvecx import * 
from plotpf import *

x = np.linspace(-1,1,16)  # the vector x

M = MassMat1D(x)
inverse_M = np.linalg.inv(M) #the inverse of the Matrix M 
b = LoadVec1D(x)

Pf = inverse_M@b    

print('x= \n',x)
print('b= \n', LoadVec1D(x))
print('M = \n',MassMat1D(x))
print('Pf= \n' ,Pf)

plotall(x,Pf)