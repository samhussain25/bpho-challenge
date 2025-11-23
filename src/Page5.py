import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Particle import Particle
import numpy as np


class Page5(tk.Toplevel):
    


    buttonClose : ctk.CTkButton = None
    buttonRefresh : ctk.CTkButton = None
    sliderSpeed : tk.Scale = None
    labelSpeed : tk.Label = None
    sliderTheta : tk.Scale = None
    labelTheta : tk.Label = None
    sliderHeight : tk.Scale = None
    labelTheta : tk.Label = None
    sliderX : tk.Scale = None
    labelX : tk.Label = None
    sliderY : tk.Scale = None
    labelY : tk.Label = None
    X = float(1)
    Y = float(1)

#######################
   
    def __init__(self, parent):
        super().__init__(parent)
        app : tk.Tk = parent
        NORMALFONT = ("Montserrat", 15)

        self.geometry('600x600')
        self.title('page 5')

####### GRAPH #######
        fig = Figure(figsize=(3,4), dpi=100, constrained_layout=True)
        p = Particle(app.h, app.speed, app.theta, app.a)
        p.sim()
        ax = fig.add_subplot()
        
        def apogee():
            apogeex=app.speed**2/app.g * np.sin(np.deg2rad(app.theta))*np.cos(np.deg2rad(app.theta))
            apogeey = app.h + app.speed**2/(2*app.g) * np.sin(np.deg2rad(app.theta))**2
            ax.plot(apogeex, apogeey, 'x', label='apogee')
            return [apogeex, apogeey]

        

        def labels():
            ax.legend()
            ax.set_xlim(0, None)
            ax.set_ylim(0, None)
            ax.set_xlabel('x/m')
            ax.set_ylabel('y/m')
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        def high_low():
            ax.plot(self.X, self.Y, 'gx', label='target')

            a = app.g*self.X**2/(2*app.speed**2)
            b = -self.X
            c = self.Y - app.h + ( (app.g*self.X**2) / (2*app.speed**2) )

            roots = np.roots([a, b, c])
            
            theta1 = np.arctan(roots[0])
            theta2 = np.arctan(roots[1])
            print(theta1, theta2)
            l = Particle(h=app.h, speed=app.speed, theta=np.rad2deg(theta1), a=app.a)
            l.sim()
            h = Particle(h=app.h, speed=app.speed, theta=np.rad2deg(theta2), a=app.a)
            h.sim()
            minspeed = speed=np.sqrt(app.g)*np.sqrt(self.Y+np.sqrt(self.X**2+self.Y**2))
            thetamin = np.arctan((self.Y+np.sqrt(self.X**2+self.Y**2))/self.X)
            u=Particle(h=0, speed=minspeed, theta=np.rad2deg(thetamin), a=app.a)
            u.sim()
            ax.plot([x[0] for x in l.coords], [y[1] for y in l.coords], '--r', label='high ball')
            ax.plot([x[0] for x in h.coords], [y[1] for y in h.coords], '--g', label='low ball')
            ax.plot([x[0] for x in u.coords], [y[1] for y in u.coords], ls='--', c='#000000', label='min speed')
            return minspeed
        def bounding():
            Rmax = app.speed**2/app.g * ((np.sqrt(1 + 2*app.g*app.h/app.speed**2 ) ))
            x = np.linspace(0, Rmax, 100)
            y = (((app.speed**2)/(2*app.g)) - ((app.g*x**2)/(2*app.speed**2))) + app.h # makes a list, iterates through x list
            ax.plot(x, y, color='gray', linestyle='dashed', label='bounding parabola')


        def max_dist():
            thetamax = np.rad2deg(np.arcsin(1/(np.sqrt(2+ (2*app.g*app.h)/app.speed**2))))
            d = Particle(h=app.h, speed=app.speed, theta=thetamax, a=app.a)
            d.sim()
            ax.plot([x[0] for x in d.coords], [y[1] for y in d.coords], ls='--', c='#800080', label='max range')
            return (d.distance, d.coords[-1][0])#
        
        def new_line():
            ax.clear()
            
            p = Particle(h=app.h, speed=app.speed, theta=app.theta, a=app.a)
            p.sim()
            ax.plot([x[0] for x in p.coords], [y[1] for y in p.coords], '--b', label='projectile')
            dinfo = max_dist()

            minspeed =high_low()
            bounding()
            top = apogee()    
            for i in range(2):
                top[i]=round(top[i], 2)    
            top = tuple(top)
            ax.set_title(str('g='+str(app.g)+'m/s^-2, h='+str(app.h)+'m, u='+str(app.speed)+
                             'm/s, θ='+str(app.theta)+'°, apogee='+str(top)+', s='+str(round(p.distance, 2))+
                             'm, $s_{max}$='+str(round(dinfo[0], 2))+'m, R='+
                             str(round(p.coords[-1][0], 2))+'m, $R_{max}$='+
                             str(round(dinfo[1], 2))+'m, target=('+
                             str(self.X)+','+str(self.Y)+'), $u_{min}$='+str(round(minspeed, 2))+'m/s'), loc='center', wrap=True)

            
            
            labels()

            canvas.draw()
#################################################        
        def update_speed(new_val):
            new_val = float(new_val)
            if new_val >= np.sqrt(app.g)*np.sqrt(self.Y+np.sqrt(new_val**2+self.Y**2)):
                app.speed=new_val
                new_line()
            else:
                self.sliderSpeed.set(app.speed)

        def update_theta(new_val):
            new_val = float(new_val)
            app.theta=new_val
            new_line()


        def update_height(new_val):
            app.h=float(new_val)
            new_line()
        
        def close():
            self.destroy()
        
        def refresh():
            
            new_line()

        def set_x(new_val):
            new_val = float(new_val)
            if app.speed >= np.sqrt(app.g)*np.sqrt(self.Y+np.sqrt(new_val**2+self.Y**2)):
                self.X = new_val
                refresh()
            else:
                self.sliderX.set(self.X)
            
        
        def set_y(new_val):
            new_val = float(new_val)
            if app.speed >= np.sqrt(app.g)*np.sqrt(new_val+np.sqrt(self.X**2+new_val**2)):
                self.Y = new_val
                refresh()
            else:
                self.sliderY.set(self.Y)
            

        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)


        self.buttonClose = ctk.CTkButton(self, text='Close', command=close)
        self.buttonClose.grid(column=3,row=0, padx=10, pady=10, sticky='nsew')


        self.sliderSpeed = tk.Scale(self, from_=0.1, to=app.MAXSPEED, orient='horizontal', resolution=0.01,
                                command=update_speed, showvalue=True)
        self.sliderSpeed.grid(column=1, row=1, sticky='ew', columnspan=2)
        self.sliderSpeed.set(app.speed)

        self.labelSpeed = tk.Label(self, text='speed, m/s', font = NORMALFONT)
        self.labelSpeed.grid(column=1, row=0, columnspan=2)


        self.sliderTheta = tk.Scale(self, from_=0, to=90, orient='horizontal', resolution=0.01,
                                command=update_theta, showvalue=True)
        self.sliderTheta.grid(column=1, row=3, sticky='ew', columnspan=2)
        self.sliderTheta.set(app.theta)

        self.labelSpeed = tk.Label(self, text='theta, degrees', font = NORMALFONT)
        self.labelSpeed.grid(column=1, row=2, columnspan=2)


        self.sliderX = tk.Scale(self, from_=1, to=app.RANGEMAX, orient='horizontal', resolution=0.01,
                                command=set_x, showvalue=True)
        self.sliderX.grid(column=2, row=6, sticky='we')
        self.labelX = tk.Label(self, text='X', font = NORMALFONT)
        self.labelX.grid(column=1, row=6, columnspan=2, sticky='w')


        self.sliderY = tk.Scale(self, from_=1, to=app.HEIGHTMAX, orient='horizontal', resolution=0.01,
                                command=set_y, showvalue=True)
        self.sliderY.grid(column=2, row=7, sticky='we')
        self.labelY = tk.Label(self, text='Y', font = NORMALFONT)
        self.labelY.grid(column=1, row=7, columnspan=2, sticky='w')


        canvas.get_tk_widget().grid(column=0, row=1, rowspan=6, padx=10, pady=10, sticky='news')
       