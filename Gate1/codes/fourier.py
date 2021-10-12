import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from sklearn import metrics

N = 500
x = np.linspace(-5,5, N)

def sinc(t):
    y = np.zeros(N)
    for i in range(N):
        if t[i] == 0:
            y[i] = 1
        else:
            y[i] = np.sin(np.pi*t[i])/(np.pi*t[i])
    return y

def rect(t):
    y = np.zeros(N)
    for i in range(N):
        if t[i] >= -0.5 and t[i] <= 0.5:
            y[i] = 1
    return y

#Computing the first signal
y = sinc(4*x)
#Computing the fourier transform
y_fourier = [10*np.mean(y * np.exp(1j * 2 * np.pi * f * x)) for f in x]

plt.plot(x,y)
plt.xlabel('$t$')
plt.ylabel('$x(t)$')
plt.grid()
plt.show()

plt.plot(x,np.real(y_fourier), label='Simulation',color='b')
plt.plot(x,0.25*rect(0.25*x), label='Theoretical',color='r')
plt.xlabel('$f$')
plt.ylabel('$X(f)$')
plt.grid()
plt.legend()
plt.show()

plt.plot(x,np.real(y_fourier)**2, label='Simulation',color='b')
plt.plot(x,(0.25*rect(0.25*x))**2, label='Theoretical',color='r')
plt.xlabel('$f$')
plt.ylabel('$X^{2}(f)$')
plt.grid()
plt.legend()
plt.show()

print('Energy of signal f(t) : ',metrics.auc(x,np.real(y_fourier)**2))
