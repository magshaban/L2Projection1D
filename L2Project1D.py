#This is the chapter one codes in the FEM book of Larson.
#this is educational project to get myself familiar with FEM implementation and git.

import numpy as np
import matplotlib.pyplot as plt



# This function is to evaluate the mass matrix in 1D for X 
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


# This function f(x) which used int the numerical integration.
def foo(y):
     return y*np.sin(y)


# print ('foo(x)= ',foo(x))

# This function is to evaluate the Load vector b in 1D for X 
def LoadVec1D(x):
    n = len(x) - 1          # number of elemnts 
    b = np.zeros((n+1,1))   # allocate b matrix
    
    for i in range(n):
        h = x[i+1] - x[i]
        b[i] += foo([x[i]])*h/2
        b[i+1] += foo([x[i+1]])*h/2
    
    return b


x = np.linspace(0,1,6)

M = MassMat1D(x)
inverse_M = np.linalg.inv(M)
b = LoadVec1D(x)

Pf = inverse_M@b 

print('x= \n',x)
print('b= \n', LoadVec1D(x))
print('M = \n',MassMat1D(x))
print('Pf= \n' ,Pf)

plt.plot(x,foo(x))
plt.plot(x,Pf)
plt.show()
