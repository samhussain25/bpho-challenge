import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots()

#basic variables
g=9.81 #ms^-2
h=2 #m
y=h 
u=20  #ms^-1
theta = np.pi / 6 #rad

#other variables
Cd = 0.1 #drag coefficient, no units
rho = 1 #air density, kgm^-3
m = 0.1 #object mass, kg

#cross seectional area of a ball radius r 
A = 0.007854

# direct cross-sectional area
# A = 

k = (Cd*rho*A)/(2*m) #drag force
print(k)

xlist = [0]
ylist = [h]

totaltime = 0
dt = 0.01

vx = u*np.cos(theta)
vy = u*np.sin(theta)
vxlist = [vx]
vylist = [vy]

n = 0

xn, yn, vxn, vyn = 0, h, vx, vy
aax, aay = 0, -g

def update_acc(n):
    
    vn = np.sqrt(vxn**2+vyn**2)
    aax = (-vxn*k*vn**2)/vn
    aay = -g -(vyn*k*vn**2)/vn
    return aax, aay

def verlet_resistance(n): 
    global totaltime, aax, aay
    
    xn = xlist[n]
    yn = ylist[n]
    vxn = vxlist[n]
    vyn = vylist[n]

    ax, ay = aax, aay
    aax, aay = update_acc(n)


    xn1 = xn + vxn*dt + (0.5*aax*dt**2)
    yn1 = yn + vyn*dt + (0.5*aay*dt**2)


    vxn1 = vxlist[n] + 0.5*(ax+aax)*dt    
    vyn1 = vylist[n] + 0.5*(ay+aay)*dt
    

    xlist.append(xn1)
    ylist.append(yn1)
    vxlist.append(vxn1)
    vylist.append(vyn1)
    totaltime+=dt

def verlet_no_resistance(n): 
    global totaltime, aax, aay
    
    xn = xlist[n]
    yn = ylist[n]
    vxn = vxlist[n]
    vyn = vylist[n]

    ax, ay = aax, aay
    aax, aay = 0, -g
    xn1 = xn + vxn*dt + (0.5*aax*dt**2)
    yn1 = yn + vyn*dt + (0.5*aay*dt**2)


    vxn1 = vxlist[n] + 0.5*(ax+aax)*dt    
    vyn1 = vylist[n] + 0.5*(ay+aay)*dt
    

    xlist.append(xn1)
    ylist.append(yn1)
    vxlist.append(vxn1)
    vylist.append(vyn1)
    totaltime+=dt


while ylist[n]>0:
    verlet_resistance(n)
    n+=1


axes.plot(xlist, ylist, '-r', label='air resistance')

vxn 
xlist = [0]
ylist = [h]

totaltime = 0
dt = 0.01

vx = u*np.cos(theta)
vy = u*np.sin(theta)
vxlist = [vx]
vylist = [vy]

n = 0

while ylist[n]>0:
    verlet_no_resistance(n)
    n+=1

xmax = max(xlist)
ymax = max(ylist)

axes.plot(xlist, ylist, '-b', label='no air resistance')

axes.set_xlim([0, xmax*1.1])
axes.set_ylim([0, ymax*1.1])

plt.xlabel("x/m")
plt.ylabel("y/m")
title = str('g='+str(g)+', h='+str(h)+'m, u='+str(u)+'m/s, θ='+str(round(np.rad2deg(theta), 2))+ ', tmax='+str(round(totaltime, 2))+'s')
plt.title(title)
plt.legend()
plt.show()
print(totaltime)