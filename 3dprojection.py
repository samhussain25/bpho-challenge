from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(projection='3d')


FPS=24
N=100#idk

#variables
G=0.81
u=5
theta = np.pi/4
dt = 1/FPS #so that its real time
t = 0

class Projectile:
    def __init__(self, r, v, a, coords_list): #r is position vector
        self.r = r
        self.v = v
        self.a = a
        self.coords_list = coords_list
    
    def update_r(self):
        self.coords_list.append(self.r)
        self.r[0]=self.r[0]+ self.v[0]*dt + 0.5*self.a[0]*dt**2
        self.r[1]=self.r[1]+ self.v[1]*dt + 0.5*self.a[1]*dt**2
        self.r[2]=self.r[2]+ self.v[2]*dt + 0.5*self.a[2]*dt**2
        print(self.r)

    def update_v(self):
        self.v[0]=self.v[0]+ self.a[0]*dt
        self.v[1]=self.v[1]+ self.a[1]*dt
        self.v[2]=self.v[2]+ self.a[2]*dt
        print(self.v)

    def update_a(self):
        print(self.a)
        pass

    def update_all(self):
        self.update_r()
        self.update_v()
        self.update_a()

p = Projectile(r=[0,1,0], v=[2,2,2], a=[0,-G,0], coords_list=[])


while p.r[1]>=0:
    p.update_r()
    p.update_v()
    p.update_a()
    t+=dt



x=[]
y=[]
z=[]
for i in range(len(p.coords_list)):
    x.append(p.coords_list[i][0])
    y.append(p.coords_list[i][1])
    z.append(p.coords_list[i][2])    
xmax = max(x)
ymax = max(y)
ax.set(xlim=(0, xmax*1.05), ylim=(0, ymax*1.05))

def update(num, data, line):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])

print(p.coords_list)

data = np.array(list(p.coords_list)).T
line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

ax.set_xlim3d([-1.0, 1.0])
ax.set_xlabel('X')

ax.set_ylim3d([-1.0, 1.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 10.0])
ax.set_zlabel('Z')


ani = FuncAnimation(fig, update, N, fargs=(data, line), interval=10000/N, blit=False)
ani.save('matplot003.mp4')
plt.show()
        
