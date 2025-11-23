
import matplotlib.pyplot as plt
import numpy as np
import sys

xlist = []
ylist = []

fig, ax = plt.subplots()

#constants
G=9.81
H=2

u=10
y=H
X = 10
Y = 5

theta = np.pi/3




ux = u*np.cos(theta)
uy = u*np.sin(theta)


####################
#for inputted theta
sin = np.sin(theta)
cos = np.cos(theta)

t = 0
dt = 0.0002
dx = dy = 0
xlist = []
ylist = []
x = 0
y = H
#s = (u**2/G)*((np.log((1+sin)/cos))*cos**2 + sin)
s=0



while y>=0:
    velx = ux #dx/dt
    vely = uy - (G*t) #dy/dt

    dx = velx*dt
    dy = vely*dt

    x += dx
    y += dy
    t += dt

    s += np.sqrt(dx**2 + dy**2)

    xlist.append(x)
    ylist.append(y)
ax.plot(xlist, ylist, '-b', label='θ = '+str(round(np.degrees(theta), 3))+ ', T = '+ str(round(t, 3))+'secs, s = '+ str(round(s, 2))+ 'm')
maxy = max(ylist)

##################
#for max range

Rmax = u**2/G * ((np.sqrt(1 + 2*G*H/u**2 ) ))
thetamax = np.arcsin(1/(np.sqrt(2+ (2*G*H)/u**2)))
#smax = (u**2/G)*(np.log((1+np.sin(thetamax))/np.cos(thetamax))*(np.cos(thetamax))**2 + np.sin(thetamax))
smax = 0
ux = u*np.cos(thetamax)
uy = u*np.sin(thetamax)

t = 0
dt = 0.0002
dx = dy = 0
xlist = []
ylist = []
x = 0
y = H
while y>=0:
    velx = ux #dx/dt
    vely = uy - (G*t) #dy/dt

    dx = velx*dt
    dy = vely*dt

    x += dx
    y += dy
    t += dt

    smax += np.sqrt(dx**2 + dy**2)

    xlist.append(x)
    ylist.append(y)
ax.plot(xlist, ylist, '-r', label='max range, θ = '+str(np.round(np.degrees(thetamax), 2))+ ', T = '+ str(round(t, 3))+'secs, s = '+str(round(smax, 2))+'m')

maxheight = max(maxy, max(ylist))
ax.set_xlim([0, Rmax*1.1])
ax.set_ylim([0, maxheight*1.1])

plt.xlabel("x/m")
plt.ylabel("y/m")
title = str('G= '+str(G)+', H = '+str(H)+', u = '+str(u))
plt.title(title)
plt.legend()
plt.show()
