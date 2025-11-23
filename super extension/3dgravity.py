import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Button, Slider

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

#fig, ax = plt.subplots()

###############variables
M = 10**11
m = 1
G = 6.67*(10**-11) # m3 kg-1 s-2
g=9.81
H=0
u=5
theta = np.pi/3 #angle clockwise to pos x-axis
psi = np.pi/3 # angle of inclination from x-y plane
FPS = 24 
dt = 1/FPS
init_r = [0,0,5] # initial position
init_a = [0,0,0]
t = 0

 
class Projectile:
    
    def __init__(self, r, u, theta, psi, a, coords_list, m): #psi
        self.r = r 
        self.v = [u*np.sin(psi)*np.cos(theta), u*np.sin(psi)*np.sin(theta), u*np.cos(psi)] 
        #x=ρsinφcosθ
        #y=ρsinφsinθ
       # z=ρcosφ
        self.a = a
        self.coords_list = coords_list
    

    def create(self):
        global t
        t = 0
        
        while np.linalg.norm(self.r) >= 1:
            print(np.linalg.norm(self.r))
            ag = -(G*M)/((np.linalg.norm(self.r)))#acceleration due to gravity

            self.a = self.r/ag   
            self.coords_list.append([self.r[0], self.r[1], self.r[2]])
            for i in range(3):
                self.r[i]=self.r[i]+ self.v[i]*dt + 0.5*self.a[i]*dt**2
                self.v[i]=self.v[i]+ self.a[i]*dt

            t+=dt


p = Projectile(init_r, u, theta, psi, init_a, [], m) 

p.create()
line, = ax.plot([], [], lw=2)
x = [i[0] for i in p.coords_list]
y = [i[1] for i in p.coords_list]
z = [i[2] for i in p.coords_list]
line.set_data_3d(x, y, z)

# adjust position of plot
fig.subplots_adjust(left=0.25, bottom=0.25)


ax.set_xlabel('X')
ax.set_xlim(0,200)

ax.set_ylabel('Y')
ax.set_ylim(0,200)

ax.set_zlabel('Z')
ax.set_zlim(0,200)

plt.show()
 