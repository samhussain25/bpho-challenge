import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Button, Slider

#fig = plt.figure()
#ax = fig.add_subplot(projection='3d')

fig, ax = plt.subplots()

###############variables

G=9.81
H=0
u=20
thetax = np.pi/4 #angle clockwise to pos x-axis
#thetaz = np.pi/4 # angle of inclination from x-y plane
FPS = 10
dt = 1/FPS
init_r = [0,0] # initial position
init_a = [0,-G]
class Projectile:
    
    def __init__(self, r, u, thetax, a, coords_list): #thetaz
        self.r = r 
        self.v = [u*np.cos(thetax), u*np.sin(thetax)] #, np.sin(thetaz)
        self.a = a
        self.coords_list = coords_list

        self.startr = r
        self.startv = self.v
        self.starta = self.a
    

    def create(self):
        t = 0
        while self.r[1]>=0:#[2]
            self.coords_list.append([self.r[0], self.r[1]]) #, self.r[2]]
            for i in range(2): # range 3
                self.r[i]=self.r[i]+ self.v[i]*dt + 0.5*self.a[i]*dt**2
                self.v[i]=self.v[i]+ self.a[i]*dt

            t+=dt
    def reset(self):
        self.r=self.startr
        self.v=self.startv
        self.a=self.starta
        self.coords_list=[]

projectiles = []

p=Projectile(list(init_r), u, thetax, init_a, []) 
b=Projectile(list(init_r), u+5, thetax, init_a, [])
projectiles.append(p)
projectiles.append(b)
for projectile in projectiles:
    projectile.create()

print(p.coords_list)
print("\n\n\n")
print(b.coords_list)

#print([projectile.coords_list for projectile in projectiles])
#xcoords = [x[0] for x in p.coords_list]
#ycoords = [y[1] for y in p.coords_list]
lines = [projectile.coords_list for projectile in projectiles]
for line in lines:
    ax.plot(line, lw=2)
#print(lines)

#line, = ax.plot(xcoords, ycoords, lw=2)

# adjust position of plot
fig.subplots_adjust(left=0.25, bottom=0.25)

axtheta = fig.add_axes([0.25, 0.1, 0.65, 0.03])
theta_slider = Slider(
    ax=axtheta,
    label='angle [degrees]',
    valmin=0.1,
    valmax=90,
    valinit=45,
    
)

axspeed = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
speed_slider = Slider(
    ax=axspeed,
    label='speed [m/s]',
    valmin=0.1,
    valmax=30,
    valinit=20,
    orientation='vertical'
)

def update(val):
    for projectile in projectiles:    
        projectile.r = [0,0]
        projectile.v = [speed_slider.val*np.cos(np.deg2rad(theta_slider.val)), speed_slider.val*np.sin(np.deg2rad(theta_slider.val))]
        projectile.coords_list = [p.r]


        projectile.create()
        coords = projectile.coords_list
        #for i, j in coords:
         #   print(i, j)
        #xcoords = [x[0] for x in projectile.coords_list]
        #ycoords = [y[1] for y in projectile.coords_list]
        #line.set_xdata(xcoords)
        #line.set_ydata(ycoords)
        lines = [projectile.coords_list for projectile in projectiles]
        #for line in lines:
        #    ax.plot(line, lw=2)
        
        fig.canvas.draw_idle()
speed_slider.on_changed(update)
theta_slider.on_changed(update)

resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    speed_slider.reset()
    theta_slider.reset()
button.on_clicked(reset)


#print(p.coords_list)
#p.graph('#595C5B', '-', 'projectile')


ax.set_xlabel('metres')
ax.set_xlim(0,100)

ax.set_ylabel('metres')
ax.set_ylim(0,100)
#ax.set_zlabel('Z')

#plt.gca().set_xlim(left=0)
#plt.gca().set_ylim(bottom=0)
#title = str('G= '+str(G)+', H = '+str(H)+', u = '+str(u)) #+', theta = '+str(np.rad2deg(theta))
#plt.title(title)
#plt.legend()
plt.show()
 