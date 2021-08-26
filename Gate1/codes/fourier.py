import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
N = 1000

# data
x = np.linspace(-5*np.pi,5*np.pi, N)

y = np.zeros(N)
for i in range(N):
  if x[i] >= -4*np.pi and x[i] <= 4*np.pi:
    y[i] = 0.25
  
fourier = [np.mean(y * np.exp( 1j * f * x)) for f in x]

# figure
plt.plot(x,y)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.title('Signal in time domain')
plt.show()
plt.plot(x,np.real(fourier))
plt.xlabel('\u03C9')
plt.ylabel('Re(F(\u03C9))')
plt.title('Signal in frequency domain')
plt.show()