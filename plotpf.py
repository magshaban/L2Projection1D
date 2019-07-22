# The main file is L2Projection1D.py

import matplotlib.pyplot as plt
from funcx import *

def plotall(x,Pf):
    

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
    
       plt.figure()
 
    plt.grid() 
    plt.plot(x,foo(x),'--r')
    plt.plot(x,Pf,'b')
    plt.xlabel('x')
    plt.legend(('$f(x)$','$Pf(x)$'), loc='upper right')
    plt.title('$f(x)$ and $Pf(x)$')
    plt.show()
    plt.savefig('result.png')