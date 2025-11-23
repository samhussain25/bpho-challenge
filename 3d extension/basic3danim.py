#works

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
#variables
G=9.81
H=10
u=5
thetax = np.pi/4 #angle clockwise to pos x-axis
thetaz = np.pi/3 # angle of inclination from x-y plane
FPS = 24
t=0
frames = 0
dt = 1/FPS


class Projectile:
    
    def __init__(self, r, u, thetax, thetaz, a): #r is position vector ##### ? thetaz,
        self.r = r # [X, Y, Z] Z IS GOING UP AND DOWN 
        self.v = [u*np.cos(thetax), u*np.sin(thetax), u*np.sin(thetaz)] #, np.sin(thetaz)
        self.a = a
        self.coords_list = []
    

    def update(self):
        while self.r[2]>=0:    
            self.coords_list.append([self.r[0], self.r[1], self.r[2]])
            for i in range(3):
                self.r[i]=self.r[i]+ self.v[i]*dt + 0.5*self.a[i]*dt**2
                self.v[i]=self.v[i]+ self.a[i]*dt



            global t, frames
            t+=dt
            frames+=1

    #def graph(self, set_colour, set_line, name):
    #    self.coords_list=np.array(self.coords_list)
    #    ax.plot([x[0] for x in p.coords_list], [y[1] for y in p.coords_list], [z[2] for z in p.coords_list], set_line, color=set_colour, label=name)

def animate(num, data, line):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])

p = Projectile([0,0,0], 5, thetax, thetaz, [0, 0, -2])
#print(p.r[2])
p.update()


data = np.array(list(p.coords_list)).T

xmax = max(data[0])
xmin = min(data[0])
ymax = max(data[1])
ymin = min(data[1])
zmax = max(data[2])
zmin = min(data[2])


line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])
#print(data[0, 0:1], data[1, 0:1], data[2, 0:1])

ax.set_xlim3d([xmin*1.1, xmax*1.1])
ax.set_xlabel('X')

ax.set_ylim3d([ymin*1.1, ymax*1.1])
ax.set_ylabel('Y')

ax.set_zlim3d([zmin*1.1, zmax*1.1])
ax.set_zlabel('Z')
ani = FuncAnimation(fig, animate, frames+1, fargs=(data, line), interval=1000/FPS, blit=False)
#ani.save('basic3danim.mp4')

plt.show()
 