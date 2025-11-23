import matplotlib.pyplot as plt
import numpy as np
import sys

fig, ax = plt.subplots(1, 2)

#constants
g=10
h=0

u=10
y=h
X = 10
Y = 5

theta = np.pi/6

maxr = 0 # maximum value of t in the whole set of data
maxt = 0 # MAXIMUM VALUE OF T IN THE WHOLE SET OF DATA
maxx = 0
maxy = 0


def curve(u, theta, coloursetting, strlabel): #*returnmax = true or false
    rlist = []
    tlist = []
    xlist = []
    ylist = []

    sin = np.sin(theta)
    cos = np.cos(theta)

    ux = u*cos
    uy = u*sin

    x=y=dx=dy=0
    t = 0
    dt = 0.001
    
    while t<2.5:
    ################### FIRST SET OF AXES
        t += dt

        r = np.sqrt((u*t)**2-((g*t**3)*u*sin)+((g*t**2)**2/4))

        rlist.append(r)
        tlist.append(t)
    ################### SECOND SET OF AXES
        velx = ux #dx/dt
        vely = uy - (g*t) #dy/dt

        dx = velx*dt
        dy = vely*dt

        x += dx
        y += dy

        xlist.append(x)
        ylist.append(y)


    ax[0].plot(tlist, rlist, '-', color=coloursetting, label=strlabel)

    tx = ((3*u)/(2*g))*(sin+np.sqrt(sin**2-(8/9))) # T WHEN THE GRAPH IS AT MAXIMUM
    tm = ((3*u)/(2*g))*(sin-np.sqrt(sin**2-(8/9))) # T WHEN THE GRAPH IS AT MINIMUM

    rwhentx = np.sqrt((u*tx)**2-((g*tx**3)*u*sin)+((g*tx**2)**2/4))
    rwhentm = np.sqrt((u*tm)**2-((g*tm**3)*u*sin)+((g*tm**2)**2/4))

    ax[0].plot(tx, rwhentx, 'x', color='magenta') # magenta = a maxima in r vs t
    ax[0].plot(tm, rwhentm, 'x', color='gray') # gray = a minimum in r vs t

    global maxr
    global maxt

    maxr = max(maxr, max(rlist)) # to scale axes properly
    maxt = max(maxt, max(tlist)) 

    #global maxx
    #global maxy

    global maxx
    global maxy

    maxx = max(maxx, max(xlist)) # to scale y axis properly
    maxy = max(maxy, max(ylist)) 


    xwhentx = u*cos*tx
    ywhentx = u*sin*tx - ((g*tx**2)/2)
    xwhentm = u*cos*tm
    ywhentm = u*sin*tm - ((g*tm**2)/2)

    ax[1].plot(xlist, ylist, '-', color=coloursetting, label=strlabel)
    ax[1].plot(xwhentx, ywhentx, 'x', color='magenta')
    ax[1].plot(xwhentm, ywhentm, 'x', color='gray')

curve(u, np.deg2rad(30), '#06ff00', 'θ = 30')
curve(u, np.deg2rad(45), '#00daff', 'θ = 45')
curve(u, np.deg2rad(60), '#3500ff', 'θ = 60')
curve(u, np.arcsin(2*np.sqrt(2)/3), '#ff0072', 'θ = 70.5')
curve(u, np.deg2rad(78), '#ff7400', 'θ = 78')
curve(u, np.deg2rad(85), '#ffce00', 'θ = 85')

### setting axis 1

ax[0].set_xlim([0, maxt])
ax[0].set_ylim([0, maxr])
ax[0].set_xlabel("t/s")
ax[0].set_ylabel("r/m")

### axis 2

ax[1].set_xlim([0, 15])
ax[1].set_ylim([-maxy, maxy])
ax[1].set_xlabel("x/m")
ax[1].set_ylabel("y/m")


title = str('g= '+str(g)+', h = '+str(h)+', u = '+str(u))
fig.suptitle(title)
plt.legend()
plt.show()
