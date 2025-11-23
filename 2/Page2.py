import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Particle import Particle
import numpy as np


class Page2(tk.Toplevel):
    


    buttonClose : ctk.CTkButton = None
    sliderSpeed : tk.Scale = None
    labelSpeed : tk.Label = None
    sliderTheta : tk.Scale = None
    labelTheta : tk.Label = None
    sliderHeight : tk.Scale = None
    labelTheta : tk.Label = None


#######################
   
    def __init__(self, parent):
        super().__init__(parent)
        app : tk.Tk = parent
        NORMALFONT = ("Montserrat", 15)

        self.geometry('600x600')
        self.title('page 2')

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



        def new_line():
            ax.clear()
            
            p = Particle(h=app.h, speed=app.speed, theta=app.theta, a=app.a)
            p.sim()
            ax.plot([x[0] for x in p.coords], [y[1] for y in p.coords], '-b', label='projectile')
            top =apogee()
            for i in range(2):
                top[i]=round(top[i], 2)

            top = tuple(top)
            R = app.speed**2/app.g * (np.sin(np.deg2rad(app.theta))*np.cos(np.deg2rad(app.theta)) + np.cos(np.deg2rad(app.theta))*(np.sqrt(np.sin(np.deg2rad(app.theta))**2 + 2*app.g*app.h/app.speed**2 ) ))
            ax.set_title(str('g='+str(app.g)+'m/s^-2, h='+str(app.h)+'m, u='+str(app.speed)+
                             'm/s, θ='+str(app.theta)+'°, apogee='+str(top))+
                             ', R='+str(round(R, 2))+'m', loc='center', wrap=True)
            
            labels()

            canvas.draw()
#################################################        
        def update_speed(new_val):
            new_val = float(new_val)
            app.speed=new_val
            new_line()

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

       
        self.sliderHeight = tk.Scale(self, from_=0, to=app.MAXHEIGHT, orient='horizontal', resolution=0.01,
                                command=update_height, showvalue=True)
        self.sliderHeight.grid(column=1, row=5, sticky='ew', columnspan=2)
        self.sliderHeight.set(app.h)

        self.labelHeight = tk.Label(self, text='height, m', font = NORMALFONT)
        self.labelHeight.grid(column=1, row=4, columnspan=2)


        canvas.get_tk_widget().grid(column=0, row=1, rowspan=6, padx=10, pady=10, sticky='news')
       