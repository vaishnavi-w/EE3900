import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(-1,20,15)

y_n = []
def y(n):
  if n>0 and n<1:
    return (3*(-1/2)**n - 2)
  if n>1:
    return (3*(-1/2)**n - 2)+ (4*(-1/2)**(n-1) + 14)*(1/3)
  else:
    return (0)
 
for i in n:
  y_n.append(y(i)) 


plt.stem(n,y_n,use_line_collection=True)
plt.grid()
plt.xlabel("n")
plt.ylabel("y[n]")
plt.show()

!pip install lcapy
import lcapy as lc
from lcapy.discretetime import z

X1=6*z/(2*z+1)
x1=X1.IZT()

X2=8/(6*z+3)
x2=X2.IZT()

X3=-2*z/(z - 1)
x3=X3.IZT()

X4=14/(3*z - 3)
x4=X4.IZT()

print(x1)
print(x2)
print(x3)
print(x4)