# -*- coding: utf-8 -*-
import numpy as npy
from matplotlib import pyplot as p
print(">>METODO RAZON DORADA<<")
xu=4.0
x1=0.0
i=0.01
def metodo_razon(xu,x1,i,fu):
  re=(5**.5-1.)/2.
  x2=x1=0
  k=0
  while xu-x1>i:
    d=re*(xu-x1)
    x1=x1+d
    x2=xu-d
    k+=1
    if fu(x1)<fu(x2):
      x1=x2
    print('k=', k,', x1=',x1,', fu(x1)=',fu(x1),', x2=',x2,', fu(x2)=',fu(x2))
    if fu(x1)<fu(x2):
      return x1
    else:
      return x2
  
fu=lambda x: (x**2)-npy.sin(x)
x=metodo_razon(xu, x1, i, fu)

print(x)
y=fu(x)
x=npy.linspace(0,1,30)
y=fu(x)
p.plot(x,y)

