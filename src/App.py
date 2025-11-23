import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from Page1 import Page1
from Page2 import Page2
from Page3 import Page3
from Page4 import Page4
from Page5 import Page5
from Page6 import Page6
from Page7 import Page7
from Page8 import Page8
from Page9 import Page9
import numpy as np


class App(tk.Tk):

    # componenets #
    buttonPage1 : ctk.CTkButton = None
    buttonPage2 : ctk.CTkButton = None
    buttonPage3 : ctk.CTkButton = None
    buttonPage4 : ctk.CTkButton = None
    buttonPage5 : ctk.CTkButton = None
    buttonPage6 : ctk.CTkButton = None
    buttonPage7 : ctk.CTkButton = None
    buttonPage8 : ctk.CTkButton = None
    buttonPage9 : ctk.CTkButton = None

    buttonClose: ctk.CTkButton = None
    ################
    # APP SETTINGS #
    ################

    name = "Projectiles"                                         
    width = 720                                                      
    height = 240                                                                                                             

    # STATE VARIABLES #
    g = 9.81
    speed = 10
    theta = 30 # of inclination
    h = 0
    a = [0,-g]
    g=9.81
    MAXSPEED = 100
    MAXHEIGHT = 100
    RANGEMAX = MAXSPEED**2/g * ((np.sqrt(1 + 2*g*MAXHEIGHT/MAXSPEED**2 ) ))
    HEIGHTMAX = MAXHEIGHT + MAXSPEED**2/(2*g)
    bounces=6
    C=0.7
    Cd=0.1
    rho=1
    m=0.1
    A=0.007854

    def page1(self):
        window=Page1(self)
        window.grab_set()
    def page2(self):
        window=Page2(self)
        window.grab_set()
    def page3(self):
        window=Page3(self)
        window.grab_set()
    def page4(self):
        window=Page4(self)
        window.grab_set()
    def page5(self):
        window=Page5(self)
        window.grab_set()
    def page6(self):
        window=Page6(self)
        window.grab_set()
    def page7(self):
        window=Page7(self)
        window.grab_set()
    def page8(self):
        window=Page8(self)
        window.grab_set()
    def page9(self):
        window=Page9(self)
        window.grab_set()


    # INITIALIZE THE APP #
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self) 
        container.grid(row=0, column=0)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.geometry(f"{self.width}x{self.height}")
        self.title(self.name)
        self.resizable(False, False)

        # Theme settings for the app
        # https://github.com/TomSchimansky/CustomTkinter/wiki/Themes
        ctk.set_appearance_mode("dark")    # Modes: system (default), light, dark
        ctk.set_default_color_theme("dark-blue")    # Themes: blue (default), dark-blue, green

        self.buttonPage1 = ctk.CTkButton(master=self, text="Page 1", command= lambda : self.page1())
        self.buttonPage1.grid(row=0, column=0,padx=10,pady=10)
        
        self.buttonPage2 = ctk.CTkButton(master=self, text="Page 2", command= lambda : self.page2())
        self.buttonPage2.grid(row=0, column=1,padx=10,pady=10)

        self.buttonPage3 = ctk.CTkButton(master=self, text="Page 3", command= lambda : self.page3())
        self.buttonPage3.grid(row=0, column=2,padx=10,pady=10)

        self.buttonPage4 = ctk.CTkButton(master=self, text="Page 4", command= lambda : self.page4())
        self.buttonPage4.grid(row=0, column=3,padx=10,pady=10)

        self.buttonPage5 = ctk.CTkButton(master=self, text="Page 5", command= lambda : self.page5())
        self.buttonPage5.grid(row=1, column=0,padx=10,pady=10)

        self.buttonPage6 = ctk.CTkButton(master=self, text="Page 6", command= lambda : self.page6())
        self.buttonPage6.grid(row=1, column=1,padx=10,pady=10)

        self.buttonPage7 = ctk.CTkButton(master=self, text="Page 7", command= lambda : self.page7())
        self.buttonPage7.grid(row=1, column=2,padx=10,pady=10)

        self.buttonPage8 = ctk.CTkButton(master=self, text="Page 8", command= lambda : self.page8())
        self.buttonPage8.grid(row=1, column=3,padx=10,pady=10)

        self.buttonPage9 = ctk.CTkButton(master=self, text="Page 9", command= lambda : self.page9())
        self.buttonPage9.grid(row=2, column=1, columnspan=2,padx=10,pady=10)

        self.buttonClose = ctk.CTkButton(self, text='Close', command=self.destroy)
        self.buttonClose.grid(row=3, column=1, columnspan=2, padx=10, pady=10)