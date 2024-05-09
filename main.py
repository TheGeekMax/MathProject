import matplotlib.pyplot as plt
import numpy as np
from runge import Runge

# Cts

y0 = 1
k = 2

def f(t, y):
    return k*y

def result(t):
    return np.exp(k*t)*y0


# Runge-Kutta

t0 = 0
h = 0.1
n = 10
runge = Runge(f, t0, y0, h)

t = np.linspace(t0, n*h, n+1)
y = np.zeros(n+1)
y[0] = y0
for i in range(1, n+1):
    y[i] = runge.runge()

# Plot
sol_t = np.linspace(t0, n*h, 1000)
sol_y = result(sol_t)

plt.plot(t, y, 'o', label='Runge-Kutta')
plt.plot(sol_t, sol_y, label='Exact solution')

plt.xlabel('t')
plt.ylabel('y')
plt.legend()

plt.show()