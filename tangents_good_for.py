from pylab import *
from matplotlib.patches import Ellipse

clf()
ax = axes(subplot(211))
title("Proximity-based reconstruction")
#ax = axes()
dt = 0.20
t = arange(-0.5*pi/dt, 0.5*pi/dt)*dt

bottom = array([ sin(t), -0.55+0.5*cos(t) ])
top = array([ sin(t), 0.55-0.5*cos(t) ])

#Plot point p_i
for pts in [bottom, top]:
    plot(pts[0], pts[1], "go-")
    plot(pts[0], pts[1], "go")

for n in range(bottom.shape[1]):
    try:
        if sum(abs(bottom[:,n]-top[:,n])**2) < 0.05:
            plot( [bottom[0,n], top[0,n]], [bottom[1,n], top[1,n]], "go-")
        if sum(abs(bottom[:,n]-top[:,n+1])**2) < 0.1:
            plot( [bottom[0,n], top[0,n+1]], [bottom[1,n], top[1,n+1]], "go-")
        if sum(abs(bottom[:,n]-top[:,n-1])**2) < 0.1:
            plot( [bottom[0,n], top[0,n-1]], [bottom[1,n], top[1,n-1]], "go-")

    except Exception, e:
        pass

xlim(-0.75,0.75)
ylim(-0.35,0.35)
ax.set_xticklabels([])
ax.set_yticklabels([])


#Second subplot
ax = axes(subplot(212))

title("Point/Tangent-based reconstruction")

for pts in [bottom, top]:
    plot(pts[0], pts[1], "go-")
    plot(pts[0], pts[1], "go")


for n in t:
    gamma = array([sin(n), 0.55-0.5*cos(n)])
    mperp = array([ -0.5*sin(n), cos(n)])
    mperp /= sqrt(sum(mperp**2))
    k = 0.20
    upper_fz = Ellipse( gamma+k*mperp, 2*k, 2*k, 0.0, fill=True, edgecolor="pink", facecolor="pink" )
    ax.add_patch( upper_fz )
    lower_fz = Ellipse( gamma-k*mperp, 2*k, 2*k, 0.0, fill=True, edgecolor="pink", facecolor="pink" )
    ax.add_patch( lower_fz )


xlim(-0.75,0.75)
ylim(-0.35,0.35)
ax.set_xticklabels([])
ax.set_yticklabels([])


savefig("tangents_good_for.eps")
#show()
