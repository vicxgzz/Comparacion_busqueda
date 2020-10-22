# -*- coding: utf-8 -*-
import numpy as npy
from matplotlib import pyplot as p
print(">>METODO NEWTON<<")
x0=0.5
e=0.1
def metodo_newton(x0,e,func,func1,func2):
  xk=x0
  k=0
  print(func1(xk))
  while abs(func1(xk))>=e:
    xk=xk-func1(xk)/func2(xk)
    k+=1
    print('k=', k,', xk=',xk,', func(xk)=',func(xk),', func1(xk)=',func1(xk),', func2(xk)',func2(xk))
    if k==10:
      break
  return xk
func=lambda x: (x**2)-npy.sin(x)
func1=lambda x:  (2*x)-npy.cos(x)
func2=lambda x:   2+npy.sin(x)
x=metodo_newton(x0,e,func,func1,func2)
print(x)
y=func(x)
x=npy.linspace(0,1,30)
y=func(x)
p.plot(x,y)

