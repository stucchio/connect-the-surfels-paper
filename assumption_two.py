from pylab import *
from matplotlib.patches import Ellipse
from misc import *
from numpy import random

clf()

ax = axes()
dt = 0.01
nt = int(2*pi/dt)
t = arange(0, nt)*dt


for (n, gamma) in enumerate([ array([ cos(t) + 1.3*exp(-7*(t-2*pi/2)**2), -sin(t) + 0.5*exp(-2*(t-3*pi/2)**2)]),
                              array([ cos(t)*(1-0.85*cos(t)**2)+1.5, 1.4*sin(t)]),
                              ]):
    ax.plot(gamma[0], gamma[1], label="$\gamma_{"+str(n+1)+"}$")

arrow(1.17,0,0.13,0, width=0.01, facecolor="black")
arrow(1.17,0,-0.125,0, width=0.01, facecolor="black")
text(1.16,0,"$\delta$")
arrow(1.5,0,-0.105,0, width=0.01, facecolor="red", edgecolor="red")
arrow(1.5,0,0.10,0, width=0.01, facecolor="red", edgecolor="red")
text(1.5,0,"$\delta$")

legend()

ax.set_xlim(-1.1,2.2)
ax.set_ylim(-1.5,2.0)
ax.set_xticklabels([])
ax.set_yticklabels([])


title("Separation between curves")



savefig("assumption_two.eps")
#show()
