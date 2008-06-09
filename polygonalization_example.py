from pylab import *
from matplotlib.patches import Ellipse
from misc import *
from numpy import random

clf()

ax = axes()
dt = 0.01
nt = int(2*pi/dt)
t = arange(0, nt)*dt


for (n, gamma) in enumerate([ array([ cos(t), sin(t) + 1.0*exp(-4*(t-3*pi/2)**2)]),
                              array([ cos(t), 0.5*sin(t)+1.6]),
                              array([ cos(t)*(1-0.8*cos(t)**2)+1.5, 1.4*sin(t)]),
                              ]):
    step = 50
    t = arange(0,nt,step)
    t += random.randint(0,2*step/3.0, [t.shape[0], ])
    if t[-1] >= t.shape[0]-1:
        t[-1] = t.shape[0]-1
    if n == 0:
        ax.plot(gamma[0], gamma[1], "k--", label="$\gamma$")
        ax.plot(gamma[0,t], gamma[1,t], "go-", label="polygonalization")
    else:
        ax.plot(gamma[0], gamma[1], "k--", label=None)
        ax.plot(gamma[0,t], gamma[1,t], "go-", label=None)


legend()

ax.set_xlim(-1.5,2.2)
ax.set_ylim(-1.5,2.7)
ax.set_xticklabels([])
ax.set_yticklabels([])


title("Curves and polygonalizations")



savefig("polygonalization_example.eps")
show()
