# The main file is L2Projection1D.py

import matplotlib.pyplot as plt
from funcx import *
from LinShapeFun1D import *


def plotall(x,Pf):
    
    # To plot the basis function.
    for i in range(len(x)):
        plt.plot(x,basisf(x,i))
        
    plt.xlabel('x')
    plt.ylabel('$\phi_i (x)$')
    plt.title('Linear shape functions in 1D')
    plt.grid()
    plt.show()

    plt.grid()
    plt.plot(x,foo(x),'r')
    plt.xlabel('x')
    plt.ylabel('$f(x)$')
    plt.title('The given function f(x)')
    plt.show()
    
    plt.plot(x,Pf,'b')
    plt.xlabel('x')
    plt.ylabel('$Pf(x)$')
    plt.title('$L^2$ projection of $f(x)$')
    plt.grid()
    plt.show()
        
    plt.grid() 
    plt.plot(x,foo(x),'--r')
    plt.plot(x,Pf,'b')
    plt.xlabel('x')
    plt.legend(('$f(x)$','$Pf(x)$'), loc='upper right')
    plt.title('$f(x)$ and $Pf(x)$')
    plt.show()
