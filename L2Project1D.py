#Maged Shaban
#This is the chapter one cod in the the FEM book of Larson.
#this is educational project to get familiar with FEM implementaion and git.

import numpy as np
import matplotlib.pyplot as plt

# This function is to evaluate the mass matrix in 1D for X 
def MassMat1D(x):
    n= len(x) - 1 # numper of elemnts 
    M = np.zeros((n+1,n+1)) #allocate n+1xn+1 zeros matrix for M
    
    for i in range(n):
        h = x[i+1] - x[i]
        M[i,i] += h/3
        M[i+1,i] += h/6      
        M[i,i+1] += h/6
        M[i+1,i+1] += h/3 
        
    return M      

x = np.linspace(0,1,6)
print('x= \n',x)

print('M = \n',MassMat1D(x))

# This function in the right handside of the equation.
def foo(y):
     
    z= y*np.sin(y)
    return z
# print ('foo(x)= ',foo(x))

# This function is to evaluate the Load vector b in 1D for X 
def LoadVec1D(x):
    n = len(x) - 1
    b = np.zeros((n+1,1))
    
    for i in range(n):
        h = x[i+1] - x[i]
        b[i] += foo([x[i]])*h/2
        b[i+1] += foo([x[i+1]])*h/2
    
    return b


print('b= \n', LoadVec1D(x))

M = MassMat1D(x)
M_inverse = np.linalg.inv(M)
b = LoadVec1D(x)

Pf = M_inverse@b 
print('pf= \n' ,Pf)

plt.plot(x,Pf)
plt.show()