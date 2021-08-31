import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
N = 500

# data
x = np.linspace(-3,3, N)

y = np.zeros(N)
for i in range(N):
  if x[i] >= -2 and x[i] <= 2:
    y[i] = 0.25
  
fourier = [np.mean(y * np.exp( 1j * 2 * np.pi * f * x)) for f in x]

# figure
plt.plot(x,y)
plt.xlabel('f')
plt.ylabel('X(f)')
plt.title('Frequency domain')
plt.show()
plt.plot(x,np.real(fourier))
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('Time domain')
plt.show()
