from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()

line, = ax.plot([], [], '-k')
FPS=24

#variables
G=9.81
H=10
u=5
max_bounces=6
C=0.7#dampening
theta = np.pi/4
dt = 1/FPS #so that its real time

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

coords = verlet(u, theta, H, G, max_bounces, C)
x=[]
y=[]
for i in range(len(coords)):
    x.append(coords[i][0])
    y.append(coords[i][1])
        
xmax = max(x)
ymax = max(y)
ax.set(xlim=(0, xmax*1.05), ylim=(0, ymax*1.05))

def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

anim = FuncAnimation(fig, animate, frames=len(x)+1, interval=1000/FPS, blit=True)

anim.save('challenge8.mp4')

        
