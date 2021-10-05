import numpy as np
import matplotlib.pyplot as plt
from math import *

N = 1000

time = np.linspace(0,4,N)

signal1 = 3*np.sin(25*time)
signal2 = 4*np.cos(20*time+3) + 2*np.sin(10*time)
signal3 = np.exp(-time)*np.sin(25*time)

plt.plot(time,signal1)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Signal 1')
plt.grid()
plt.show()

plt.plot(time,signal2)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Signal 2')
plt.grid()
plt.show()

plt.plot(time,signal3)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Signal 3')
plt.grid()
plt.show()
