from pylab import *
from matplotlib.patches import Ellipse

clf()

ax = axes()
dt = 0.01
t = arange(-(pi/2)/dt, (pi/2)/dt)*dt

plot(1.2*sin(t), 0.5*sin(t/2)*abs(sin(t)), label="$\\gamma(t)$", color='black') #Possible curvesn
plot(t, t*0, color='black')
plot(sin(t),1-cos(t), label='$\\tau^+(t)$', color='blue',ls='-.') #Bounding curves
plot(sin(t),-1+cos(t), label='$\\tau^-(t)$', color='green', ls=':')

rad = Ellipse( (0.0, 0.0), pi, pi, 0.0, fill=True, edgecolor="lightblue", facecolor="lightblue" )
ax.add_patch(rad)

#Forbidden zones
upper_fz = Ellipse( (0.0, 1.0), 2, 2, 0.0, fill=True, edgecolor="orange", facecolor="orange" )
lower_fz = Ellipse( (0.0, -1.0), 2, 2, 0.0, fill=True, edgecolor="orange", facecolor="orange" )
ax.add_patch( upper_fz )
ax.add_patch( lower_fz )

text(0,-1.2,"Forbidden zone",horizontalalignment='center')
text(0,1.2,"Forbidden zone",horizontalalignment='center')

arrow(0,-0.5,0,0.45, width=0.015) #Radii of forbidden regions
arrow(0,-0.5,0,-0.45, width=0.015)
text(0.05,-0.65, "$R=\kappa_m^{-1}$")
arrow(0,0.5,0,0.45, width=0.015)
arrow(0,0.5,0,-0.45, width=0.015)
text(0.05,0.5, "$R=\kappa_m^{-1}$")

legend()

#Plot point p_i
ax.plot([0,], [0,], "go-")
text(0.1,0.05, "$p_{i}$", horizontalalignment="center")

xticks([-1,0,1], ["$-1/\kappa_m$","$p_{i,x}$", "$1/\kappa_m$"])
yticks([-1,0,1], ["$-1/\kappa_m$","$p_{i,y}$", "$1/\kappa_m$"])


title("Forbidden regions")

L = 2.25
ax.set_xlim(-L,L)
ax.set_ylim(-L,L)


savefig("forbidden_zone.eps")
#show()

#Noisy forbidden zone
clf()

def circle_intersection(error, height):
    t = ((arange(1000)-500)/500.0)*(pi/2-error/2)
    x_offset = cos(pi-error)
    xy = array( [cos(t)+x_offset, sin(t)]).transpose()
    xy[0] = [xy[1,0], 0]
    xy[:,0] -= xy[1,0]
    h = xy[1,1]
    xy[:,1] -= h
    if height < 0:
        xy[:,1] *= -1
    rad1 = Polygon(xy, edgecolor="orange", facecolor="orange" )

    t = ((arange(1000)-500)/500.0)*(pi/2-error/2)+pi
    x_offset = cos(pi-error)
    xy = array( [cos(t)+x_offset, sin(t)]).transpose()
    xy[0] = [xy[1,0], 0]
    xy[:,0] -= xy[1,0]
    xy[:,1] -= h
    if height < 0:
        xy[:,1] *= -1
    rad2 = Polygon(xy, edgecolor="orange", facecolor="orange" )

    return rad1, rad2

ax = axes()
dt = 0.01
t = arange(-(pi/2)/dt, (pi/2)/dt)*dt

plot(1.2*sin(t), 0.5*sin(t/2)*abs(sin(t))+0.2*t, label="$\\gamma(t)$", color='black') #Possible curvesn
plot(t, t*0, color='black')

#Allowed region
rad = Ellipse( (0.0, 0.0), 1.2, 1.2, 0.0, fill=True, edgecolor="lightblue", facecolor="lightblue" )
ax.add_patch(rad)

#Forbidden zones
ax.add_patch(circle_intersection(pi/5, 1)[0]) #Upper
ax.add_patch(circle_intersection(pi/5, 1)[1])

ax.add_patch(circle_intersection(pi/5, -1)[0]) #Lower
ax.add_patch(circle_intersection(pi/5, -1)[1])

L = 2.25
ax.set_xlim(-L,L)
ax.set_ylim(-L,L)

text(0,-1.2,"Forbidden zone",horizontalalignment='center')
text(0,1.2,"Forbidden zone",horizontalalignment='center')

savefig("forbidden_zone_noisy.eps")
