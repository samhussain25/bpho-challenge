"""Task 7: A curious fact is that the range r of a projectile from the
launch point, plotted against time t can, for launch angles
greater than about 70.5 degrees, actually pass through a local
maximum and then a minimum, before increasing with
increasing gradient. Use the derivations to recreate the
graphs of r vs t. Work out the times, x, y, and r values for
these maxima and minima and plot these via a
suitable marker."""


import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from Particle import Particle
import numpy as np


class Page7(tk.Toplevel):
    


    buttonClose : ctk.CTkButton = None
    sliderSpeed : tk.Scale = None
    labelSpeed : tk.Label = None
    sliderTheta : tk.Scale = None
    labelTheta : tk.Label = None
    sliderHeight : tk.Scale = None
    labelTheta : tk.Label = None

#######################
    g = 9.81
    speed = 10
    theta = 45 # of inclination
    h = 0
    a = [0,-g]
    maxr = 0 # maximum value of t in the whole set of data
    maxt = 0 # MAXIMUM VALUE OF T IN THE WHOLE SET OF DATA
    maxx = 0
    maxy = 0

    
        


    def __init__(self, parent):
        super().__init__(parent)
        app : tk.Tk = parent
        NORMALFONT = ("Montserrat", 15)

        self.geometry('600x600')
        self.title('page 7')

####### GRAPH #######
        fig1 = Figure(figsize=(3,4), dpi=100, constrained_layout=True)
        plot1 = fig1.add_subplot(111)
        canvas1 = FigureCanvasTkAgg(fig1, self)
        
        fig2 = Figure(figsize=(3,4), dpi=100, constrained_layout=True)
        plot2 = fig2.add_subplot(111)
        canvas2 = FigureCanvasTkAgg(fig2, self)

        if app.speed>10:   
            app.speed=5

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

                r = np.sqrt((u*t)**2-((app.g*t**3)*u*sin)+((app.g*t**2)**2/4))

                rlist.append(r)
                tlist.append(t)
            ################### SECOND SET OF AXES
                velx = ux #dx/dt
                vely = uy - (app.g*t) #dy/dt

                dx = velx*dt
                dy = vely*dt

                x += dx
                y += dy

                xlist.append(x)
                ylist.append(y)


            plot1.plot(tlist, rlist, '-', color=coloursetting, label=strlabel)

            tx = ((3*u)/(2*app.g))*(sin+np.sqrt(sin**2-(8/9))) # T WHEN THE GRAPH IS AT MAXIMUM
            tm = ((3*u)/(2*app.g))*(sin-np.sqrt(sin**2-(8/9))) # T WHEN THE GRAPH IS AT MINIMUM

            rwhentx = np.sqrt((u*tx)**2-((app.g*tx**3)*u*sin)+((app.g*tx**2)**2/4))
            rwhentm = np.sqrt((u*tm)**2-((app.g*tm**3)*u*sin)+((app.g*tm**2)**2/4))

            plot1.plot(tx, rwhentx, 'x', color='magenta') # magenta = a maxima in r vs t
            plot1.plot(tm, rwhentm, 'x', color='gray') # gray = a minimum in r vs t



            self.maxr = max(self.maxr, max(rlist)) # to scale axes properly
            self.maxt = max(self.maxt, max(tlist)) 


            self.maxx = max(self.maxx, max(xlist)) # to scale y axis properly
            self.maxy = max(self.maxy, max(ylist)) 


            xwhentx = u*cos*tx
            ywhentx = u*sin*tx - ((app.g*tx**2)/2)
            xwhentm = u*cos*tm
            ywhentm = u*sin*tm - ((app.g*tm**2)/2)

            plot2.plot(xlist, ylist, '-', color=coloursetting, label=strlabel)
            plot2.plot(xwhentx, ywhentx, 'x', color='magenta')
            plot2.plot(xwhentm, ywhentm, 'x', color='gray')

        def animate():
            plot1.clear()
            plot2.clear()
            
            curve(app.speed, np.deg2rad(30), '#06ff00', 'θ = 30')
            curve(app.speed, np.deg2rad(45), '#00daff', 'θ = 45')
            curve(app.speed, np.deg2rad(60), '#3500ff', 'θ = 60')
            curve(app.speed, np.arcsin(2*np.sqrt(2)/3), '#ff0072', 'θ = 70.5')
            curve(app.speed, np.deg2rad(78), '#ff7400', 'θ = 78')
            curve(app.speed, np.deg2rad(85), '#ffce00', 'θ = 85')
            fig1.suptitle('u='+str(app.speed))
            plot1.set_xlim([0, self.maxt])
            plot1.set_ylim([0, self.maxr])
            plot1.set_xlabel("time, t/s")
            plot1.set_ylabel("range, r/m")
            plot2.set_xlim([0, 15])
            plot2.set_ylim([-self.maxy, self.maxy])
            plot2.set_xlabel("x/m")
            plot2.set_ylabel("y/m")


        
        def update_speed(new_val):
            app.speed=float(new_val)
            animate()
        
        def close():
            self.destroy()

        def refresh():
            self.destroy()
            app.page7()



        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=2)

        

        self.buttonClose = ctk.CTkButton(self, text='Close', command=close)
        self.buttonClose.grid(column=4,row=0, padx=10, pady=10, sticky='nsew')

        self.buttonRefresh = ctk.CTkButton(self, text='Refresh', command=refresh)
        self.buttonRefresh.grid(column=4, row=1, padx=10, pady=10, sticky='nsew')

        self.sliderSpeed = tk.Scale(self, from_=0.1, to=10, orient='horizontal', resolution=0.01,
                                command=update_speed, showvalue=True)
        self.sliderSpeed.grid(column=2, row=1, sticky='ew')
        self.sliderSpeed.set(app.speed)

        self.labelSpeed = tk.Label(self, text='speed, m/s', font = NORMALFONT)
        self.labelSpeed.grid(column=2, row=0)

        animate()
        canvas1.draw()
        canvas2.draw()
        canvas1.get_tk_widget().grid(column=0, row=1, rowspan=6, padx=10, pady=10, sticky='news')
        canvas2.get_tk_widget().grid(column=1, row=1, rowspan=6, padx=10, pady=10, sticky='news')
        
