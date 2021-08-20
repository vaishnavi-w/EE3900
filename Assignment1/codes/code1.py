from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

P = np.array([-2,4,-5]).reshape((3,1))
Q = np.array([1,2,3]).reshape((3,1))
O = np.array([0,0,0]).reshape((3,1))

PQ = Q - P

print('Direction vector for line PQ is :\n',PQ)

A = PQ/np.linalg.norm(PQ)
OA = A - O

print('Unit vector for line PQ is :',OA)

L_PQ = np.empty((2,3),float)
L_PQ[0,:] = P[:,0]
L_PQ[1,:] = Q[:,0]

L_OA = np.empty((2,3),float)
L_OA[0,:] = O[:,0]
L_OA[1,:] = A[:,0]

plt.plot(L_PQ[:,0],L_PQ[:,1],L_PQ[:,2],'r',label="PQ")
plt.plot(L_OA[:,0],L_OA[:,1],L_OA[:,2],'g',label="OA")

ax.scatter(P[0],P[1],P[2],'o')
ax.scatter(Q[0],Q[1],Q[2],'o')
ax.scatter(O[0],O[1],O[2],'o')
ax.scatter(A[0],A[1],A[2],'o')
ax.text(-2,4,-5, "P", color='red')
ax.text(1,2,3, "Q", color='red')
ax.text(0,0,0, "O", color='red')
ax.text(OA[0][0],OA[1][0],OA[2][0], "A", color='red')


plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best');plt.grid()
plt.show()