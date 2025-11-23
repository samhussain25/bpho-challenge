import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from matplotlib.widgets import Button, Slider

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

#fig, ax = plt.subplots()


###################### EARTH
image_file = 'assets/earth.jpg'
img = plt.imread(image_file)

# define a grid matching the map size, subsample along with pixels
theta = np.linspace(0, np.pi, img.shape[0])
phi = np.linspace(0, 2*np.pi, img.shape[1])

count = 180 # keep 180 points along theta and phi
theta_inds = np.linspace(0, img.shape[0] - 1, count).round().astype(int)
phi_inds = np.linspace(0, img.shape[1] - 1, count).round().astype(int)
theta = theta[theta_inds]
phi = phi[phi_inds]
img = img[np.ix_(theta_inds, phi_inds)]

theta,phi = np.meshgrid(theta, phi)
R = 1

angle_rotation = 0

# sphere
x = R * np.sin(theta) * np.cos(phi)
y = R * np.sin(theta) * np.sin(phi)
z = R * np.cos(theta)


ax.plot_surface(x.T, y.T, z.T, facecolors=img/255, cstride=1, rstride=1) # we've already pruned ourselves
ax.axis('scaled')


#init_pos = [x,y,z] 

#z_rotation = np.array([[np.cos(angle_rotation), -np.sin(angle_rotation), 0], 
#            [np.sin(angle_rotation), np.cos(angle_rotation), 0], 
#            [0,0,1]])
#print(z_rotation)
#init_pos = np.array(list(zip(x,y,z))) # to create coordinates
#print(init_pos)
#for coord in init_pos:
#    coord = z_rotation.dot(coord)

#final_pos = z_rotation.dot(init_pos)
#final_pos = list(zip(*final_pos))

#x = final_pos[0]
#y = final_pos[1]
#z = final_pos[2]

# create 3d Axes

ax.plot_surface(x.T, y.T, z.T, facecolors=img/255, cstride=1, rstride=1) # we've already pruned ourselves



# make the plot more spherical



###############variables
EARTH_RADIUS = 6371 #km, one earth radius = 1 unit on the graph
M = 10**11
m = 1
G = 6.67*(10**-11) # m3 kg-1 s-2
g=9.81
H=0
u=10
theta = np.pi/4 #angle clockwise to pos x-axis
phi = np.pi/4 # angle of inclination from x-y plane
FPS = 24 
dt = 1/FPS
init_r = [0,0,1] # initial position
init_a = [0,0,-g/(EARTH_RADIUS/1000)]
t = 0
N=1000 #max number of frames

 
class Projectile:
    
    def __init__(self, r, u, theta, phi, a, coords_list): #phi
        self.r = r 
        self.v = [u*np.sin(phi)*np.cos(theta), 
                  u*np.sin(phi)*np.sin(theta), 
                  u*np.cos(phi)] #(spherical coordinate system)
        #x=rcosβsinα
        #y=rcosβcosα
        #z=rsinβ

        self.a = a
        self.coords_list = coords_list
    

    def create(self):
        ax.scatter(init_r[0], init_r[1], init_r[2], color='green')
        global t
        t = 0
        n=0
        while(np.linalg.norm(self.r) >= 0.99999 and n<N) :#while self.r[2]>=0:
            ag = -(G*M)/((np.linalg.norm(self.r)))#acceleration due to gravity

            self.a = self.r/ag 
            self.coords_list.append([self.r[0], self.r[1], self.r[2]])
            for i in range(3):
                self.r[i]=self.r[i]+ self.v[i]*dt + 0.5*self.a[i]*dt**2
                self.v[i]=self.v[i]+ self.a[i]*dt

            t+=dt
            n+=1
        print(self.coords_list)
        ax.scatter(self.coords_list[-1][0], self.coords_list[-1][1], self.coords_list[-1][2], color='red')


p = Projectile(init_r, u, theta, phi, init_a, []) 

p.create()
line, = ax.plot([], [], lw=2)
x = [i[0] for i in p.coords_list]
y = [i[1] for i in p.coords_list]
z = [i[2] for i in p.coords_list]
line.set_data_3d(x, y, z)

# adjust position of plot
fig.subplots_adjust(left=0.25, bottom=0.35)

axtheta = fig.add_axes([0.25, 0.1, 0.65, 0.03])
theta_slider = Slider(
    ax=axtheta,
    label='anglex [degrees]',
    valmin=0,
    valmax=360,
    valinit=45,
    
)

axphi = fig.add_axes([0.25, 0.15, 0.65, 0.03])
phi_slider = Slider(
    ax=axphi,
    label='anglez [degrees]',
    valmin=0,
    valmax=180,
    valinit=45,
    
)

axlong = fig.add_axes([0.25, 0.20, 0.65, 0.03])
long_slider = Slider(
    ax=axlong,
    label='longitude [degrees]',
    valmin=-180,
    valmax=180,
    valinit=0,
    
)

axlat = fig.add_axes([0.25, 0.25, 0.65, 0.03])
lat_slider = Slider(
    ax=axlat,
    label='latitude [degrees]',
    valmin=-90,
    valmax=90,
    valinit=0,
    
)

axspeed = fig.add_axes([0.1, 0.35, 0.0225, 0.53])
speed_slider = Slider(
    ax=axspeed,
    label='speed [km/s]',
    valmin=1,
    valmax=10,
    valinit=2,
    orientation='vertical'
)

def update(val): # edit so that calculation is only done after a button is pressed
    
    startx = np.sin(np.deg2rad(lat_slider.val+90)) * np.cos(np.deg2rad(long_slider.val+180)) # lat = phi, long = theta
    starty =  np.sin(np.deg2rad(lat_slider.val+90)) * np.sin(np.deg2rad(long_slider.val+180)) 
    startz = np.cos(np.deg2rad(lat_slider.val+90))
    p.r = [startx, starty, startz]
    
    p.coords_list = [p.r]
    
    rho = speed_slider.val/(EARTH_RADIUS/1000) # normalised speed
    p.v = [rho*np.sin(np.deg2rad(phi_slider.val))*np.cos(np.deg2rad(theta_slider.val)), 
           rho*np.sin(np.deg2rad(phi_slider.val))*np.sin(np.deg2rad(theta_slider.val)), 
           rho*np.cos(np.deg2rad(phi_slider.val))] 



    p.create()
    coords = p.coords_list
    #for i, j, z in coords:
     #   print(i, j, z)

    x = [i[0] for i in p.coords_list]
    y = [i[1] for i in p.coords_list]
    z = [i[2] for i in p.coords_list]
    line.set_data_3d(x, y, z)
    fig.canvas.draw_idle()
update(0) # works for some reason

speed_slider.on_changed(update)
theta_slider.on_changed(update)
phi_slider.on_changed(update)
long_slider.on_changed(update)
lat_slider.on_changed(update)

resetax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
reset_button = Button(resetax, 'Reset', hovercolor='0.975')

#drawax = fig.add_axes([0.8, 0.0125, 0.1, 0.04])
#draw_button = Button(drawax, 'Draw', hovercolor='0.975')



def reset(event):
    speed_slider.reset()
    theta_slider.reset()
    phi_slider.reset()
    lat_slider.reset()
    long_slider.reset()

reset_button.on_clicked(reset)
#draw_button.on_clicked(update)

scale = 1.1

ax.set_xlabel('X')
ax.set_xlim(-scale,scale)

ax.set_ylabel('Y')
ax.set_ylim(-scale, scale)

ax.set_zlabel('Z')
ax.set_zlim(-scale, scale)

plt.show()
