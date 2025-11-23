import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from Particle import Particle
from DParticle import DParticle
import numpy as np
from PIL import ImageTk


class Page9(tk.Toplevel):
    


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
        self.title('page 9')

####### GRAPH #######
        fig = Figure(figsize=(3,4), dpi=100, constrained_layout=True)
        p = Particle(app.h, app.speed, app.theta, app.a)
        p.sim()
        d=DParticle(app.h, app.speed, app.theta, app.g, app.Cd, app.rho, app.m, app.A)
        d.sim()
        ax = fig.add_subplot()
        
        

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
            d=DParticle(app.h, app.speed, app.theta, app.g, app.Cd, app.rho, app.m, app.A)
            d.sim()
            ax.plot([x[0] for x in d.coords], [y[1] for y in d.coords], ls='-', c='#000000', label='drag projectile')
            ax.set_title(str('g='+str(app.g)+'m/s^-2, h='+str(app.h)+'m, u='+str(app.speed)+
                             'm/s, θ='+str(app.theta)+'°, Cd='+str(app.Cd)+
                             ', air density='+str(app.rho)+'kgm^-3, mass='+str(app.m)+
                             'kg, cross sectional area='+str(app.A)+'m^2'), loc='center', wrap=True)
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

        def update_Cd(new_val):
            app.Cd=float(new_val)
            new_line()

        def update_rho(new_val):
            app.rho=float(new_val)
            new_line()
        
        def update_m(new_val):
            app.m=float(new_val)
            new_line()
        
        def update_A(new_val):
            app.A=float(new_val)
            new_line()
        
        
        
        def close():
            self.destroy()
        


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

        self.sliderCd = tk.Scale(self, from_=0, to=1, orient='horizontal', resolution=0.01,
                                command=update_Cd, showvalue=True)
        self.sliderCd.grid(column=2, row=6, sticky='we')
        self.labelCd = tk.Label(self, text='drag coefficient, Cd', font = NORMALFONT)
        self.labelCd.grid(column=1, row=6, columnspan=2, sticky='w')
        self.sliderCd.set(app.Cd)

        self.sliderRho = tk.Scale(self, from_=0, to=1, orient='horizontal', resolution=0.01,
                                command=update_rho, showvalue=True)
        self.sliderRho.grid(column=2, row=7, sticky='we')
        self.labelRho = tk.Label(self, text='air density, rho/kgm^-3', font = NORMALFONT)
        self.labelRho.grid(column=1, row=7, columnspan=2, sticky='w')
        self.sliderRho.set(app.rho)
        

        self.sliderM = tk.Scale(self, from_=0.05, to=0.5, orient='horizontal', resolution=0.001,
                                command=update_m, showvalue=True)
        self.sliderM.grid(column=2, row=8, sticky='we')
        self.labelM = tk.Label(self, text='mass, m/kg', font = NORMALFONT)
        self.labelM.grid(column=1, row=8, columnspan=2, sticky='w')
        self.sliderM.set(app.m)


        self.sliderA = tk.Scale(self, from_=0.005, to=0.05, orient='horizontal', resolution=0.001,
                                command=update_A, showvalue=True)
        self.sliderA.grid(column=2, row=9, sticky='we')
        self.labelA = tk.Label(self, text='cross sectional area, m^2', font = NORMALFONT)
        self.labelA.grid(column=1, row=9, columnspan=2, sticky='w')
        self.sliderA.set(app.A)



        canvas.get_tk_widget().grid(column=0, row=1, rowspan=10, padx=10, pady=10, sticky='news')