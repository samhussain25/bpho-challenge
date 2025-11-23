from matplotlib.animation import PillowWriter
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
l, = plt.plot([], [], '-k')

plt.xlim(0, 30)
plt.ylim(0, 12)


FPS = 30
#PillowWriter (animator) info
metadata = dict(title='motion', artist='samuel hussain')
writer = PillowWriter(fps = FPS, metadata=metadata)

#variables
g=9.81
h=10
u=5
y=h
N=6 #number of bounces
C=0.7
theta = np.pi/4


xlist = [0]
ylist = [h]
n = 0
bounces=0
dt = 1/FPS

vx = u*np.cos(theta)
vy = u*np.sin(theta)
vxlist = [vx]
vylist = [vy]

totaltime = 0


def verlet(n): 
    global bounces, totaltime
    
    ax, ay = 0, -g
    
    x = xlist[n] + vxlist[n]*dt + (0.5*ax*dt**2)
    y = ylist[n] + vylist[n]*dt + (0.5*ay*dt**2)

    aax, aay = 0, -g

    vx = vxlist[n] + 0.5*(ax+aax)*dt    
    vy = vylist[n] + 0.5*(ay+aay)*dt
    
    if y<0:
        y=0
        vy=-vylist[n]*C
        bounces+=1    
    

    xlist.append(x)
    ylist.append(y)
    vxlist.append(vx)
    vylist.append(vy)
    totaltime+=dt


with writer.saving(fig, 'projectile.gif', 100):
    while bounces<=N:
        verlet(n)
        l.set_data(xlist, ylist)
        writer.grab_frame()
        n+=1
        
xmax = max(xlist)
ymax = max(ylist)

