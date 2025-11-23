import matplotlib.pyplot as plt
import numpy as np
import sys

xlist = []
ylist = []

fig, ax = plt.subplots()

#variables
g=9.81
h=10
u=5
y=h
n=6
C=0.7
theta = np.pi/4


xlist = []
ylist = []



bounces=x=t=dx=dy=0
dt = 0.002

ux = u*np.cos(theta)
vy = u*np.sin(theta)
vely=0

totaltime = 0

while bounces<=n:
    if y<0:
        y=0
        t=0
        bounces +=1
        vy = -vely * C

    velx = ux #dx/dt
    vely = vy - (g*t) #dy/dt

    dx = velx*dt
    dy = vely*dt

    x += dx
    y += dy
    t += dt
    totaltime += dt

    xlist.append(x)
    ylist.append(y)


xmax = max(xlist)
ymax = max(ylist)

ax.plot(xlist, ylist, '-r')

ax.set_xlim([0, xmax*1.1])
ax.set_ylim([0, ymax*1.1])

plt.xlabel("x/m")
plt.ylabel("y/m")
title = str('g='+str(g)+', h='+str(h)+'m, u='+str(u)+'m/s, n='+str(n)+', C='+str(C)+', θ='+str(round(np.rad2deg(np.pi/6), 2)))
plt.title(title)
plt.legend()
plt.show()
print(totaltime)