import matplotlib.pyplot as plt
import numpy as np

xlist = []
ylist = []

fig, ax = plt.subplots()

g=9.81
h=2
u=10


theta = np.pi/3

t=0
dt = 0.0002
x=0
y=h

sin = np.sin(theta)
cos = np.cos(theta)

R = u**2/g * (sin*cos + cos*(np.sqrt(sin**2 + 2*g*h/u**2 ) )) #range 
Rmax = u**2/g * ((np.sqrt(1 + 2*g*h/u**2 ) ))



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

ax.plot(xlist, ylist, '-b', label='θ = '+str(round(np.degrees(theta), 2)))


xlist = []
ylist = []
x=0
y=h
t=0

sinthetamax = 1/(np.sqrt(2+ (2*g*h)/u**2))
thetamax = np.arcsin(sinthetamax)

#sin = np.sin(thetamax)
#cos = np.cos(thetamax)

ux = u*np.cos(thetamax) #initial x/y vel
uy = u*np.sin(thetamax)


#for thetamax
while y>=0:
    velx = ux #dx/dt
    vely = uy - (g*t) #dy/dt

    x += velx*dt
    y += vely*dt
    t += dt

    xlist.append(x)
    ylist.append(y)
ax.plot(xlist, ylist, '-r', label='θmax = '+str(round(np.degrees(thetamax), 2)))

#xlist = np.array(xlist)
#ylist = np.array(ylist)


plt.xlabel("x/m")
plt.ylabel("y/m")
title = str('g= '+str(g)+', h = '+str(h)+', u = '+str(u)+', θmax = ' +str(round(np.degrees(thetamax), 2))+', \nθ = '+ str(round(np.degrees(theta), 2))+', Rmax= '+str(round(Rmax, 2))+', R='+str(round(R, 2)))

plt.title(title)
plt.legend()
plt.show()

