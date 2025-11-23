import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

#variables
G=9.81
H=10
u=5
max_bounces=6
C=0.7#dampening
thetax = np.pi/4 #angle clockwise to pos x-axis
thetaz = np.pi/4 #angle with x-y plane
dt = 0.01


class Projectile:
    
    def __init__(self, r, u, thetax,  a): #r is position vector ##### ? thetaz,
        self.r = r
        self.v = [u*np.cos(thetax), u*np.sin(thetax)] #, np.sin(thetaz)
        self.a = a
        self.coords_list = []
        self.t=0
    

    def update(self):
        self.coords_list.append([self.r[0], self.r[1]])
        self.r[0]=self.r[0]+ self.v[0]*dt + 0.5*self.a[0]*dt**2
        self.r[1]=self.r[1]+ self.v[1]*dt + 0.5*self.a[1]*dt**2
        #self.r[2]=self.r[2]+ self.v[2]*dt + 0.5*self.a[2]*dt**2

        
        self.v[0]=self.v[0]+ self.a[0]*dt
        self.v[1]=self.v[1]+ self.a[1]*dt
        #self.v[2]=self.v[2]+ self.a[2]*dt
      
        self.t+=dt

    def graph(self, set_colour, set_line, name):
        self.coords_list=np.array(self.coords_list)
        ax.plot([x[0] for x in p.coords_list], [y[1] for y in p.coords_list], set_line, color=set_colour, label=name)

p = Projectile([0,0], 5, np.pi/4, [0, -2])
print(p.r[1])
while p.r[1]>=0:
    p.update()
print(p.coords_list)
p.graph('#595C5B', '-', 'projectile')


plt.xlabel("x/m")
plt.ylabel("y/m")
plt.gca().set_xlim(left=0)
plt.gca().set_ylim(bottom=0)
title = str('G= '+str(G)+', H = '+str(H)+', u = '+str(u)) #+', theta = '+str(np.rad2deg(theta))
plt.title(title)
plt.legend()
plt.show()
 