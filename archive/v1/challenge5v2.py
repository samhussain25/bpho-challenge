import matplotlib.pyplot as plt
import numpy as np
import sys

fig, ax = plt.subplots()

#constants
G=9.81
H=0 # maybe try changing code to allow variable H
u=20
target = [15, 15]
X = target[0]
Y = target[1]
#can tweak
dt = 0.01


def create_coords(u, theta, h):
    ux = u*np.cos(theta)
    uy = u*np.sin(theta)
    
    x=0
    y=h

    t=0
    
    coords = []
    while y>=0:
        velx = ux #dx/dt
        vely = uy - (G*t) #dy/dt

        x += velx*dt
        y += vely*dt
        t += dt
        coords.append([x, y])
    return coords

def graph(set_colour, set_line, name, coord_list): 
    coord_list=np.array(coord_list)
    xlist,ylist=np.split(coord_list,2,axis=1) #split em
    ax.plot(xlist, ylist, set_line, color=set_colour, label=name)

xrange = (u**2/G) * ((np.sqrt(1 + ((2*G*H)/(u**2)) )))

#bounding parabola
boundingx = np.linspace(0, xrange, 100)
boundingy = u**2/(2*G) - (G*boundingx**2)/(2*u**2) + H
coords = np.transpose([boundingx,boundingy]) #merge em
graph('#06ff00', '--' ,'bounding parabola', coords)

#min speed
u_min= np.sqrt(G)*np.sqrt(Y+np.sqrt(X**2+Y**2))
min_theta = np.arctan( (Y+np.sqrt(X**2+Y**2)) / X )
print(create_coords(u_min, min_theta, H))
graph("#7A7B7B", '-', 'min speed', create_coords(u_min, min_theta, H))

#max range
theta_max = np.arcsin(1/(np.sqrt(2+ (2*G*H)/u**2)))
graph('#DC3838', '-', 'max range', create_coords(u, theta_max, H))

#high and low ball
a = G*X**2/(2*u**2)
b = -X
c = Y - H + ( (G*X**2) / (2*u**2) )
roots = np.roots([a, b, c])
roots = np.sort(roots)
theta1 = np.arctan(roots[0])
theta2 = np.arctan(roots[1])

graph('#2DA86F', '-', 'low ball', create_coords(u, theta1, H))
graph('#A749D5', '-', 'high ball', create_coords(u, theta2, H))
###
ax.plot(X, Y, 'xy', label='target: '+str(target))
plt.xlabel("x/m")
plt.ylabel("y/m")
plt.gca().set_xlim(left=0)
plt.gca().set_ylim(bottom=0)
title = str('G= '+str(G)+', H = '+str(H)+', u = '+str(u))
plt.title(title)
plt.legend()
plt.show()
