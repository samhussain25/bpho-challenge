import matplotlib.pyplot as plt
import numpy as np


xlist = []
ylist = []

fig, axes = plt.subplots()

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



bounces=0
dt = 0.002

vx = u*np.cos(theta)
vy = u*np.sin(theta)
vxlist = [vx]
vylist = [vy]


totaltime = 0


n = 0

def verlet(n): 
    global bounces, totaltime
    
    ax, ay = 0, -g
    
    x = xlist[n] + vxlist[n]*dt + (0.5*ax*dt**2) #current x,y coords
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

while bounces<=N:
    verlet(n)
    n+=1


xmax = max(xlist)
ymax = max(ylist)

axes.plot(xlist, ylist, '-r')

axes.set_xlim([0, xmax*1.1])
axes.set_ylim([0, ymax*1.1])

plt.xlabel("x/m")
plt.ylabel("y/m")
title = str('g='+str(g)+', h='+str(h)+'m, u='+str(u)+'m/s, N='+str(N)+', C='+str(C)+', θ='+str(round(np.rad2deg(theta), 2))+ ', tmax='+str(round(totaltime, 2))+'s')
plt.title(title)
plt.legend()
plt.show()
print(totaltime)