import matplotlib.pyplot as plt
import numpy as np
from runge import Runge

# Cts
y0 = 1
t0 = 0
h = 0.001
n = 1000

# functions 

def result(t,k=2):
    return np.exp(-k*t)*y0


# Runge-Kutta
t = np.linspace(t0, n*h, n+1)


def generateItteration(kk,Y0=y0):
    def f(t, y):
        return -kk*y
    
    runge = Runge(f, h, t0, Y0)
    y = np.zeros(n+1)
    y[0] = y0
    for i in range(1, n+1):
        y[i] = runge.runge()
    return y


# Plot

# main plot with 1 example
ktemp = 2;
sol_y = result(t, ktemp)
runge = generateItteration(ktemp)

plt.figure("Runge-Kutta 1 example")
plt.plot(t, runge, 'o', label='Runge-Kutta')
plt.plot(t, sol_y, label='Exact solution')


plt.xlabel('t')
plt.ylabel('y')
plt.legend()

# show error
plt.figure("Error")
plt.plot(t, runge - sol_y)
plt.xlabel('t')
plt.ylabel('Error')


# plot with lerp colors
def lerp (a, b, t):
    return a + (b - a) * t

def colorLerp(t,a,b):
    return (lerp(a[0], b[0], t), lerp(a[1], b[1], t), lerp(a[2], b[2], t))

plt.figure("Runge-Kutta multiple examples")

for i in np.linspace(-2, 2, 1000):
    y = generateItteration(i)
    plt.plot(t, y, color=colorLerp(((i+2)/4), (41.0/255, 61.0/255, 115.0/255), (179.0/255, 25.0/255, 112.0/255)))

plt.xlabel('t')
plt.ylabel('y')

# plot with 4 values of y0

y0s = [-2, -1, 2, 3]
plt.figure("Runge-Kutta 4 examples")
for i in y0s:
    y = generateItteration(2,i)
    plt.plot(t, y, label='y0 = ' + str(i))

plt.xlabel('t')
plt.ylabel('y')
plt.legend()

plt.show()