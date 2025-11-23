import matplotlib.pyplot as plt
import numpy as np


xlist = []
ylist = []

t=0
dt = 0.01

#variables
g=9.81
u=10
theta = np.pi/4
h=10

sin = np.sin(theta)
cos = np.cos(theta)

x=0
y=h

xlist.append(x)
ylist.append(y)

ux = u*cos #initial x/y vel
uy = u*sin

R = u**2/g * (sin*cos + cos*(np.sqrt(sin**2 + 2*g*h/u**2 ) )) #range 
apogeex = u**2/g * sin*cos
apogeey = h + u**2/(2*g) * sin**2


while y>=0:
    velx = ux #dx/dt
    vely = uy - (g*t) #dy/dt

    x += velx*dt
    y += vely*dt
    t += dt

    xlist.append(x)
    ylist.append(y)

#xlist = np.array(xlist)
#ylist = np.array(ylist)
    
print(R)


for i in range(len(xlist)):
    print("x =",xlist[i], "y =",ylist[i])

print("Range(m) =", R)
print("apogee =", (apogeex, apogeey))
print("theta(radians) =", theta)
print("theta(degrees) =", np.degrees(theta))

fig, ax = plt.subplots()
ax.plot(xlist, ylist, 'r-', label='trajectory')
ax.plot(apogeex, apogeey, 'b.', label='apogee')

plt.xlabel("x/m")
plt.ylabel("y/m")
plt.legend()
plt.show()
