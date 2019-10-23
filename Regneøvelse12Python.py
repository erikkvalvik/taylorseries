# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:48:14 2019

@author: Erik
"""
import sympy as sy

x = sy.Symbol('x')
funksjon = sy.sympify(input("f(x) = "))
ledd = int(input("ledd = "))
taylor = [0 for x in range(ledd)]
finalEquation = 0

def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n - 1)

for i in range(1, ledd):
    taylor[i] = (funksjon.diff(x,i).subs(x,0)/factorial(i))*x**i

for i in range(ledd):
    if(taylor[i] == 0):
        pass
    else:
        finalEquation = finalEquation + taylor[i]

sy.plot(finalEquation, xlim=[-4,4], ylim=[-4,4], title = funksjon)
print(finalEquation)