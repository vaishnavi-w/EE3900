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

# Computing h(t)
y = rect(x + 1)
# Computing the fourier transform
y_fourier = [10 * np.mean(y * np.exp(-1j * 2 * np.pi * f * x)) for f in x]

# plt.plot(x,y)
# plt.xlabel('$t$')
# plt.ylabel('$h(t)$')
# plt.grid()
# plt.show()

fig, ax = plt.subplots(2,1)

#Plotting amplitude of signal
ax[0].plot(x, np.absolute(y_fourier))
ax[0].set_ylabel("$A$")
ax[0].grid()

#Plotting the phase
ax[1].plot(x, np.angle(y_fourier))
plt.xlabel("$f$")
ax[1].set_ylabel("$\phi$")
ax[1].grid()
plt.show()

#Computing g(t)
y_1 = np.exp(1j * 2 * np.pi * x ) * sinc(x)
#Computing the fourier transform
y_1_fourier = [10*np.mean(y_1 * np.exp(-1j * 2 * np.pi * f * x)) for f in x]

plt.plot(x, y, label='h(t) - Theoretical', color = 'b')
plt.plot(x, np.real(y_1_fourier), label='h(-f) - Simulation', color='r')
plt.xlabel('$t$ / $f$')
plt.ylabel('$h(t)$ / $h(-f)$')
plt.grid()
plt.legend(loc = "best")
plt.show()
