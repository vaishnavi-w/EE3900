import numpy as np

# Matrices A and B
A = np.array([[2/3,1,5/3],[1/3,2/3,4/3],[7/3,2,2/3]])
B = np.array([[2/5,3/5,1],[1/5,2/5,4/5],[7/5,6/5,2/5]])

# 3A - 5B
C = 3*A - 5*B

print(C)
