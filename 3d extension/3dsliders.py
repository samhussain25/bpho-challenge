import matplotlib.pyplot as plt
import numpy as np

from matplotlib.widgets import Button, Slider

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

#fig, ax = plt.subplots()

###############variables

G=9.81
H=0
u=20
alpha = np.pi/4 #angle clockwise to pos x-axis
beta = np.pi/4 # angle of inclination from x-y plane
FPS = 24 
dt = 1/FPS
init_r = [0,0,0] # initial position
init_a = [0,0,-G]
t = 0

 
class Projectile:
    
    def __init__(self, r, u, alpha, beta, a, coords_list): #beta
        self.r = r 
        self.v = [u*np.cos(beta)*np.sin(alpha), u*np.cos(beta)*np.cos(alpha), u*np.sin(beta)] 
        #x=rcosβsinα
        #y=rcosβcosα
        #z=rsinβ
        self.a = a
        self.coords_list = coords_list
    

    def create(self):
        global t
        t = 0
        while self.r[2]>=0:
            self.coords_list.append([self.r[0], self.r[1], self.r[2]])
            for i in range(3):
                self.r[i]=self.r[i]+ self.v[i]*dt + 0.5*self.a[i]*dt**2
                self.v[i]=self.v[i]+ self.a[i]*dt

            t+=dt


p = Projectile([0,0,0], u, alpha, beta, init_a, []) 

p.create()
line, = ax.plot([], [], lw=2)
x = [i[0] for i in p.coords_list]
y = [i[1] for i in p.coords_list]
z = [i[2] for i in p.coords_list]
line.set_data_3d(x, y, z)

# adjust position of plot
fig.subplots_adjust(left=0.25, bottom=0.25)

axalpha = fig.add_axes([0.25, 0.1, 0.65, 0.03])
alpha_slider = Slider(
    ax=axalpha,
    label='anglex [degrees]',
    valmin=0.1,
    valmax=90,
    valinit=45,
    
)

axbeta = fig.add_axes([0.25, 0.05, 0.65, 0.03])
beta_slider = Slider(
    ax=axbeta,
    label='anglez [degrees]',
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
    p.r = [0,0,0]
    speed = speed_slider.val
    p.v = [speed*np.cos(np.deg2rad(beta_slider.val))*np.sin(np.deg2rad(alpha_slider.val)), speed*np.cos(np.deg2rad(beta_slider.val))*np.cos(np.deg2rad(alpha_slider.val)), speed*np.sin(np.deg2rad(beta_slider.val))] 
    p.coords_list = [p.r]


    p.create()
    coords = p.coords_list
    for i, j, z in coords:
        print(i, j, z)

    x = [i[0] for i in p.coords_list]
    y = [i[1] for i in p.coords_list]
    z = [i[2] for i in p.coords_list]
    line.set_data_3d(x, y, z)
    fig.canvas.draw_idle()
update(0) # works for some reason

speed_slider.on_changed(update)
alpha_slider.on_changed(update)
beta_slider.on_changed(update)

resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', hovercolor='0.975')


def reset(event):
    speed_slider.reset()
    alpha_slider.reset()
    beta_slider.reset()
button.on_clicked(reset)


ax.set_xlabel('X')
ax.set_xlim(0,100)

ax.set_ylabel('Y')
ax.set_ylim(0,100)

ax.set_zlabel('Z')
ax.set_zlim(0,100)

plt.show()
 