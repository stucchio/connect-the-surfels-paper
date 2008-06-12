import ctd
from pylab import *
from matplotlib.collections import LineCollection
from matplotlib.colors import colorConverter
from random import *

seed()
pts = []

curvature = 3
err = 0.01
view = [0,1,0,1]
sep = 0.02

dt = 0.13#2*pi/24;

def perp(v):
    sgn = choice([-1,1])
    return (-sgn*v[1]/sqrt(v[0]**2+v[1]**2), sgn*v[0]/sqrt(v[0]**2+v[1]**2))

for t in range(int(2*pi/dt)):#-1*int(1.0/dt), int(1.0/dt):
    t *= dt
    R = 0.5
    pts.append( (-0.154+R*cos(t), R*sin(t)) +  perp([-R*sin(t),R*cos(t)]) )

    ani = 0.725
    pts.append( (0.5+0.5*sin(t)*(1-ani*sin(t)**2), 0.5*cos(t)) +
                perp( (0.5*cos(t)*(1-ani*sin(t)**2) + 0.5*sin(t)*(-ani)*2*sin(t)*cos(t)
                       , -0.5*sin(t)) ))

for i in range(1000):
    pts.append((1.7*random()-0.8, random()-0.5) + perp(( random(), random())) )

shuffle(pts)

fig = figure()

ci = 0
clrs = ['r', 'b', 'g']

ax = axes(subplot(211))
for p in pts:
    plot([p[0],], [p[1],], "go")
    arrow(p[0],p[1],-0.1*p[3],0.1*p[2], facecolor="black")

ax.set_xlim(-0.9,1.0)
ax.set_ylim(-0.6,0.6)
title("Point and Tangent data")



ax = axes(subplot(212))
curves, edges = ctd.curvature_connect( pts, curvature, 0.5*dt*sqrt(2), err*0.85, 10)

for points in curves:
    segments = []
    for i in range(len(points)):
        p = points[i]
        #arrow(p[0],p[1],0.1*p[2],0.1*p[3], ec=clrs[ci])
        if i < len(points)-1:
            p2 = points[i+1]
            segments.append( [(p[0],p[1]), (p2[0], p2[1])])
    segments.append( [(points[-1][0], points[-1][1]), (points[0][0], points[0][1])])
    LC = LineCollection(segments)
    LC.color(clrs[ci])
    ax.add_collection(LC)

    ci = (ci + 1) % len(clrs)

LC = LineCollection(edges)
LC.color('black')
ax.add_collection(LC)

ax.set_xlim(-0.9,1.0)
ax.set_ylim(-0.6,0.6)
title("Reconstructed curves")
## ax.set_xlim(0.25,0.45)
## ax.set_ylim(-0.1,0.1)


#axis(view)
savefig("example1.eps")
show()

