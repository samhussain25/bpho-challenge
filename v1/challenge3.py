import matplotlib.pyplot as plt
import numpy as np
import sys




#variables
g=9.81
u=20
h=0

X = 10
Y = 5

if u < np.sqrt(g)*np.sqrt(Y+np.sqrt(X**2+Y**2)):
    print("value of u is too low, invalid")
    sys.exit()

a = g*X**2/(2*u**2)
b = X*-1
c = Y - h + ( (g*X**2) / (2*u**2) )

roots = np.roots([a, b, c])

theta1 = np.arctan(roots[0])
theta2 = np.arctan(roots[1])


fig, ax = plt.subplots()

def calc(theta):
    xlist = []
    ylist = []
    x=0
    y=0
    t=0
    dt = 0.01

    xlist.append(x)
    ylist.append(y)

    sin = np.sin(theta)
    cos = np.cos(theta)

    ux = u*cos #initial x/y vel
    uy = u*sin

    while x<=X:
        velx = ux #dx/dt
        vely = uy - (g*t) #dy/dt

        x += velx*dt
        y += vely*dt
        t += dt

        xlist.append(x)
        ylist.append(y)

    return xlist, ylist

def plot(tuplexy, high_ball): #flag for high ball or not
    xlist = tuplexy[0]
    ylist = tuplexy[1]

    for i in range(len(xlist)):
        print("x =",xlist[i], "y =",ylist[i])


    if high_ball == True:
        print("theta(radians) =", theta1)
        print("theta(degrees) =", np.degrees(theta1))
        ax.plot(xlist, ylist, '--r', label='high ball')
        print("high")

    if high_ball == False:
        print("theta(radians) =", theta2)
        print("theta(degrees) =", np.degrees(theta2))
        ax.plot(xlist, ylist, '--b', label='low ball')
        print("low")

first = calc(theta1)
second = calc(theta2)

plot(first, high_ball=True)
plot(second, high_ball=False)

plt.xlabel("x/m")
plt.ylabel("y/m")
plt.legend()
plt.show()
