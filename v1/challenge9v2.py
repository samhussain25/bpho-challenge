import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

#variables
G=9.81
H=2
u=20
theta = np.pi/6
dt = 0.1

#drag variables
Cd = 0.1 #drag coefficient, no units
rho = 1 #air density, z
m = 0.1 #object mass, kg
A = 0.007854 #cross sectional area of a ball radius r 
k = (Cd*rho*A)/(2*m) #drag force
print(k)


def verlet(u, theta, h, g, resistance):
    x=0 # x stands for xn+1 in the verlet alg, xn+1 + vn*dt + 1/2 * an * dt^2 
    y=h
    vx=u*np.cos(theta)
    vy=u*np.sin(theta)
    ax=0
    ay=-g
    coords = [[x,y]]
    i=0

    while y>=0:
        if resistance==True:
            v = np.sqrt(vx**2+vy**2)
            ax = (-vx*k*v**2)/v
            ay = -g -(vy*k*v**2)/v #formula for acceleration
        
        x=coords[i][0] + vx*dt + 0.5*ax*dt**2
        y=coords[i][1] + vy*dt + 0.5*ay*dt**2

        vx+= ax*dt # vxn+1 formula
        vy+= ay*dt

        coords.append([x,y])
        i+=1
    return coords
def graph(set_colour, set_line, name, coord_list): 
    coord_list=np.array(coord_list)
    xlist,ylist=np.split(coord_list,2,axis=1) #split em
    ax.plot(xlist, ylist, set_line, color=set_colour, label=name)

graph('#28DC82', '-', 'resistance', verlet(u, theta, H, G, resistance=True))
graph('#595C5B', '-', 'no resistance', verlet(u, theta, H, G, resistance=False))

plt.xlabel("x/m")
plt.ylabel("y/m")
plt.gca().set_xlim(left=0)
plt.gca().set_ylim(bottom=0)
title = str('G= '+str(G)+', H = '+str(H)+', u = '+str(u)+', theta = '+str(np.rad2deg(theta)))
plt.title(title)
plt.legend()
plt.show()
