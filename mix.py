import matplotlib.pyplot as plt
import numpy as np
from runge import Runge


def euler(t0,x0,v0,z,N,l):
    #initialisation
    tab_x = np.zeros(N)
    tab_v = np.zeros(N)
    tab_t = np.linspace(t0,z,N)
    pas=z/N
    c=g/l
    x=x0
    v=v0

    #méthode d'euler "asymétrique"
    for i in range (N):
        tab_x[i]=x
        tab_v[i]=v
        x=x+v*pas
        v=v-c*np.sin(x)*pas
    return (tab_t,tab_x,tab_v)


g=9.81
l=2
z=10
N=100

t0=0
x0=1
v0=1

def f(t, y, yp):
        return -(g/l)*np.sin(y)


(t,x,v)=euler(t0,x0,v0,z,N,l)
y = np.zeros(N)
yp = np.zeros(N)
y[0] = x0
yp[0] = v0
runge = Runge(f, z/N, t0, x0, t0, v0)
for i in range(1, N):
    y[i], yp[i] = runge.runge()

plt.figure("Runge-Kutta & Euler position")
plt.plot(t, x, label='Euler, x')
plt.plot(t, y, label='Runge-Kutta, y')

plt.xlabel('t')
plt.ylabel('y')

plt.legend()

plt.figure("Runge-Kutta & Euler speed")
plt.plot(t, v, label='Euler, v')
plt.plot(t, yp, label='Runge-Kutta, yp')

plt.xlabel('t')
plt.ylabel('v')

plt.legend()

plt.figure("Runge-Kutta & Euler position x speed")
plt.plot(x, v, label='Euler')
plt.plot(y, yp, label='Runge-Kutta')
plt.xlabel('x')
plt.ylabel('v')

plt.legend()


plt.figure("Runge-Kutta & Euler position error")
plt.plot(t, x - y)
plt.xlabel('t')
plt.ylabel('Error')

plt.show()
