import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from BParticle import BParticle
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt


class Page8(tk.Toplevel):
    


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
        self.title('page8')

####### GRAPH #######
        fig = Figure(figsize=(3,4), dpi=100, constrained_layout=True)
        p = BParticle(app.h, app.speed, app.theta, app.a, bounces=app.bounces, C=app.C)
        p.sim()
        ax = fig.add_subplot()


        def labels():
            ax.legend()
            ax.set_xlim(0, None)
            ax.set_ylim(0, None)
            ax.set_xlabel('x/m')
            ax.set_ylabel('y/m')
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()

        def max_dist():
            thetamax = np.rad2deg(np.arcsin(1/(np.sqrt(2+ (2*app.g*app.h)/app.speed**2))))
            d = BParticle(h=app.h, speed=app.speed, theta=thetamax, a=app.a, bounces=app.bounces, C=app.C)
            d.sim()
            ax.plot([x[0] for x in d.coords], [y[1] for y in d.coords], '-r', label='max range')
            return (d.distance, d.t)


        def new_line():
            ax.clear()
            
            p = BParticle(h=app.h, speed=app.speed, theta=app.theta, a=app.a, bounces=app.bounces, C=app.C)
            p.sim()
            ax.plot([x[0] for x in p.coords], [y[1] for y in p.coords], '-b', label='projectile')
            smax=max_dist()
            ax.set_title(str('g='+str(app.g)+'m/s^-2, h='+str(app.h)+'m, u='+str(app.speed)+
                             'm/s, θ='+str(app.theta)+'°, s='+str(round(p.distance, 2))+
                             'm, $s_{max}$'+str(round(smax[0], 2))+'m, t='+str(round(p.t, 2))+
                              's, $t_{max}$'+str(round(smax[1], 2))+'s, bounces=')
                             +str(app.bounces)+', C='+str(app.C)+', t='+str(round(p.t, 2))+'s', loc='center', wrap=True)

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

        def update_bounces(new_val):

            app.bounces=int(new_val)
            new_line()

        def update_C(new_val):
            app.C=float(new_val)
            new_line()
        
        def close():
            self.destroy()
        
        def animate():
            self.destroy()
            fig, ax = plt.subplots()

            line, = ax.plot([], [], '-k')
            FPS=60
            p = BParticle(h=app.h, speed=app.speed, theta=app.theta, a=app.a, bounces=app.bounces, C=app.C)
            p.sim()
            x=[x[0] for x in p.coords]
            y=[y[1] for y in p.coords]
            xmax = max(x)
            ymax = max(y)
            ax.set(xlim=(0, xmax*1.05), ylim=(0, ymax*1.05))
            
            def cycle(i):
                line.set_data(x[:i], y[:i])
                return line,
            anim = FuncAnimation(fig, cycle, frames=len(x)+1, interval=1000/FPS, blit=True)

            anim.save('animation.mp4')



        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)


        self.buttonClose = ctk.CTkButton(self, text='Close', command=close)
        self.buttonClose.grid(column=3,row=0, padx=10, pady=10, sticky='nsew')

        self.buttonAnimate = ctk.CTkButton(self, text='Animate', command=animate)
        self.buttonAnimate.grid(column=3,row=1, padx=10, pady=10, sticky='nsew')


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

        
        self.sliderC = tk.Scale(self, from_=0.1, to=0.9, orient='horizontal', resolution=0.01,
                                command=update_C, showvalue=True)
        self.sliderC.grid(column=1, row=7, sticky='ew', columnspan=2)
        self.sliderC.set(app.C)

        self.labelC = tk.Label(self, text='C', font = NORMALFONT)
        self.labelC.grid(column=1, row=6, columnspan=2)

        
        self.sliderBounces = tk.Scale(self, from_=1, to=10, orient='horizontal', resolution=1,
                                command=update_bounces, showvalue=True)
        self.sliderBounces.grid(column=1, row=9, sticky='ew', columnspan=2)
        self.sliderBounces.set(app.bounces)

        self.labelBounces= tk.Label(self, text='bounces', font = NORMALFONT)
        self.labelBounces.grid(column=1, row=8, columnspan=2)



        canvas.get_tk_widget().grid(column=0, row=1, rowspan=6, padx=10, pady=10, sticky='news')
       