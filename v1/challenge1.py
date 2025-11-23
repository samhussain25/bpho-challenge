import matplotlib.pyplot as plt
import numpy as np



xlist = []
ylist = []

t=0
dt = 0.001

g=9.81
u=10
theta = np.pi/4
h=10


x=0
y=h

xlist.append(x)
ylist.append(y)

ux = u*np.cos(theta) #initial x/y vel
uy = u*np.sin(theta)

while y>=0:
    velx = ux #dx/dt
    vely = uy - (g*t) #dy/dt

    x += velx*dt
    y += vely*dt
    t += dt

    xlist.append(x)
    ylist.append(y)

#xlist = np.array(xlist)
#ylist = np.array(ylist)


plt.plot(xlist, ylist)
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.title('')
plt.show()