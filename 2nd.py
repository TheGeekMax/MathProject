import matplotlib.pyplot as plt
import numpy as np
from runge import Runge

# Cts

h=.01
n = 1000


theta0 = 1
theta0p = 1
t0 = 0
t0p = 0
g = np.pi**2
l=2.0


#CTE

hh=np.sqrt(g/l)

# Runge-Kutta for order 2 ODE

def generateItteration(th0p=theta0p,lo=l):
    def f(t, y, yp):
        return -(g/lo)*np.sin(y)
    
    runge = Runge(f, h, t0, theta0, t0p, th0p)
    y = np.zeros(n+1)
    yp = np.zeros(n+1)
    y[0] = theta0
    yp[0] = th0p
    for i in range(1, n+1):
        y[i], yp[i] = runge.runge()
    return y, yp


t = np.linspace(t0, n*h, n+1)

#example with 1 case
y,yp = generateItteration()
plt.figure("Runge-Kutta 1 example")
plt.plot(t, y, label='Runge-Kutta, y')
plt.plot(t, yp, label='Runge-Kutta, yp')
plt.xlabel('t')
plt.ylabel('y')

plt.legend()

#example 4 cases with differents theta0p
plt.figure("Runge-Kutta 4 theta0p examples")
for i in [-1,1,2,3]:
    y,yp = generateItteration(i)
    plt.plot(t, y, label='Runge-Kutta, y, theta0p = '+str(i))

plt.xlabel('t')
plt.ylabel('y')
plt.legend()

#example 4 cases with differents l
plt.figure("Runge-Kutta 4 l examples")
for i in [1,2,3,4]:
    y,yp = generateItteration(1,i)
    plt.plot(t, y, label='Runge-Kutta, y, l = '+str(i))

plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()