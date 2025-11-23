import matplotlib.pyplot as plt
import numpy as np
import sys

xlist = []
ylist = []

fig, ax = plt.subplots()

#constants
G=9.81
H=0

u=20
y=H
X = 10
Y = 5

theta = np.pi/6

def curve(u, x, H, theta, linesetting, strlabel, *returnmax): #*returnmax = true or false
    xlist = []
    ylist = []
    
    ux = u*np.cos(theta)
    uy = u*np.sin(theta)

    t = 0
    dt = 0.0002
    y = H
    dx = dy = 0
    s = 0

    while y>=0:
        velx = ux #dx/dt
        vely = uy - (G*t) #dy/dt

        dx = velx*dt
        dy = vely*dt

        x += dx
        y += dy
        t += dt

        

        xlist.append(x)
        ylist.append(y)
    ax.plot(xlist, ylist, linesetting, label=strlabel)

    if returnmax:
        return max(xlist), max(ylist)
    
curve(u,0,H,theta,'-b', 'theta = ' + str(np.round(theta, 2)))
### max range
Rmax = u**2/G * ((np.sqrt(1 + 2*G*H/u**2 ) ))
sinthetamax = 1/(np.sqrt(2+ (2*G*H)/u**2))
thetamax = np.arcsin(sinthetamax) #theta which gives greatest range for x
maxes = curve(u, 0, H, thetamax, '--r', 'max range', True)

### setting axes
ymax = maxes[1]
ax.set_xlim([0, Rmax*1.1])
ax.set_ylim([0, ymax*1.1])

###
plt.xlabel("x/m")
plt.ylabel("y/m")
title = str('G= '+str(G)+', H = '+str(H)+', u = '+str(u))
plt.title(title)
plt.legend()
plt.show()

