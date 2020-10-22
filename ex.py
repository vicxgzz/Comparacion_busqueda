# -*- coding: utf-8 -*-
import numpy as npy
from matplotlib import pyplot as p
def metodo_exhaustiva (x0,h,f):
  xk=0
  xk_1=0+h
  k=0
  while f(xk_1)<f(xk):
    xk=xk_1
    xk_1=xk_1+h
    k+=1
    print('k=', k,', xk=',xk,', f(xk)=',f(xk),', xk_1=',xk_1,', f(xk_1)',f(xk_1))
  return xk 
x=0
h=0.1  
funcion=lambda x: (x**2)-npy.sin(x)
x=metodo_exhaustiva (0,h,funcion)
y=funcion(x)
print(x)
x=npy.linspace(0,1,30)
y=funcion(x)
p.plot(x,y)