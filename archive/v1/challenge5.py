import matplotlib.pyplot as plt
import numpy as np
import sys

xlist = []
ylist = []

fig, ax = plt.subplots()

#constants
G=9.81
H=100
u=20
y=H

X = 10
Y = 5



def curve(u, x, H, theta, linesetting, strlabel, *returnmax): #*returnmax = true or false
    xlist = []
    ylist = []
    
    ux = u*np.cos(theta)
    uy = u*np.sin(theta)

    t = 0
    dt = 0.0002
    y = H

    while y>=0:
        velx = ux #dx/dt
        vely = uy - (G*t) #dy/dt

        x += velx*dt
        y += vely*dt
        t += dt

        xlist.append(x)
        ylist.append(y)
    ax.plot(xlist, ylist, linesetting, label=strlabel)

    if returnmax:
        return xlist[-1], max(ylist)


### low ball + high ball
if u < np.sqrt(G)*np.sqrt(Y+np.sqrt(X**2+Y**2)):
    print("value of u is too low, invalid")
    sys.exit()

a = (G*X**2)/(2*u**2)
b = X*-1
c = Y - H + ( (G*X**2) / (2*u**2) )

roots = np.roots([a, b, c])
theta1 = max(roots)
theta2 = min(roots)

curve(u, 0, H, theta1, '-b', 'high ball')
curve(u, 0, H, theta2, '-m', 'low ball')

### max range
Rmax = u**2/G * ((np.sqrt(1 + 2*G*H/u**2 ) ))
sinthetamax = 1/(np.sqrt(2+ (2*G*H)/u**2))
thetamax = np.arcsin(sinthetamax) #theta which gives greatest range for x
curve(u, 0, H, thetamax, '--r', 'max range')

ax.plot(0, H, '.m', label='launch: ' + str((0, H)))
ax.plot(X, Y, '.g', label='target (' + str(X) + ', '+ str(Y) + ')')

### bounding parabola
x = np.linspace(0, Rmax, 100)
y = (((u**2)/(2*G)) - ((G*x**2)/(2*u**2))) + H # makes a list, iterates through x list
ymax = max(y)
xmax = Rmax
ax.plot(x, y, '--g', label='bounding parabola')

### setting axes
ax = plt.gca()
ax.set_xlim([0, Rmax*1.1])
ax.set_ylim([0, ymax*1.1])

###
plt.xlabel("x/m")
plt.ylabel("y/m")
title = str('G= '+str(G)+', H = '+str(H)+', u = '+str(u))
plt.title(title)
plt.legend()
plt.show()
