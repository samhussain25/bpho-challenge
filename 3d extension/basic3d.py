#works

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
#variables
G=9.81
H=10
u=5
thetax = np.pi/4 #angle clockwise to pos x-axis
thetaz = np.pi/4 # angle of inclination from x-y plane
dt = 0.2


class Projectile:
    
    def __init__(self, r, u, thetax, thetaz, a): #r is position vector ##### ? thetaz,
        self.r = r # [X, Y, Z] Z IS GOING UP AND DOWN 
        self.v = [u*np.cos(thetax), u*np.sin(thetax), u*np.sin(thetaz)] #, np.sin(thetaz)
        self.a = a
        self.coords_list = []
        self.t=0
    

    def update(self):
        self.coords_list.append([self.r[0], self.r[1], self.r[2]])
        for i in range(3):
            self.r[i]=self.r[i]+ self.v[i]*dt + 0.5*self.a[i]*dt**2
            self.v[i]=self.v[i]+ self.a[i]*dt

        self.t+=dt

    def graph(self, set_colour, set_line, name):
        self.coords_list=np.array(self.coords_list)
        ax.plot([x[0] for x in p.coords_list], [y[1] for y in p.coords_list], [z[2] for z in p.coords_list], set_line, color=set_colour, label=name)

p = Projectile([0,0,0], 5, thetax, thetaz, [0, 0, -2])
print(p.r[2])
while p.r[2]>=0:
    p.update()
print(p.coords_list)
p.graph('#595C5B', '-', 'projectile')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.gca().set_xlim(left=0)
plt.gca().set_ylim(bottom=0)
title = str('G= '+str(G)+', H = '+str(H)+', u = '+str(u)) #+', theta = '+str(np.rad2deg(theta))
plt.title(title)
plt.legend()
plt.show()
 