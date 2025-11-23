import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

#variables
G=9.81
H=10
u=5
max_bounces=6
C=0.7#dampening
theta = np.pi/4
dt = 0.002

def verlet(u, theta, h, g, max_bounces, C):
    x=0 # x stands for xn+1 in the verlet alg, xn+1 + vn*dt + 1/2 * an * dt^2 
    y=h
    vx=u*np.cos(theta)
    vy=u*np.sin(theta)
    ax=0
    ay=-g
    aax=0#for when acceleration is variable
    aay=-g#^
    current_bounces=0
    coords = [[x,y]]
    i=0

    while current_bounces<=max_bounces:
        x=coords[i][0] + vx*dt + 0.5*ax*dt**2
        y=coords[i][1] + vy*dt + 0.5*ay*dt**2

        vx=vx+ 0.5*(aax+ax)*dt # vx is actually vxn+1 
        vy=vy+ 0.5*(aay+ay)*dt

        if y<=0: #bounce
            y=0
            vy=-vy*C
            current_bounces+=1
        
        coords.append([x,y])
        i+=1
    return coords
def graph(set_colour, set_line, name, coord_list): 
    coord_list=np.array(coord_list)
    xlist,ylist=np.split(coord_list,2,axis=1) #split em
    ax.plot(xlist, ylist, set_line, color=set_colour, label=name)

graph('#595C5B', '-', 'projectile', verlet(u, theta, H, G, max_bounces, C))


plt.xlabel("x/m")
plt.ylabel("y/m")
plt.gca().set_xlim(left=0)
plt.gca().set_ylim(bottom=0)
title = str('G= '+str(G)+', H = '+str(H)+', u = '+str(u)+', theta = '+str(np.rad2deg(theta)))
plt.title(title)
plt.legend()
plt.show()


