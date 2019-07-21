# This function is to evaluate the mass matrix in 1D for X
# The main fil is L2Projection1D

import numpy as np 
 
def MassMat1D(x):
    n= len(x) - 1 # number of elemnts 
    M = np.zeros((n+1,n+1)) #allocate n+1xn+1 zeros matrix for M
    
    for i in range(n):
        h = x[i+1] - x[i]
        M[i,i] += h/3
        M[i+1,i] += h/6      
        M[i,i+1] += h/6
        M[i+1,i+1] += h/3 
        
    return M      

