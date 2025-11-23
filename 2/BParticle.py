import numpy as np
FPS=60
class BParticle:
    def __init__(self, h, speed, theta, a : list, bounces, C):
        self.r = [0, h]
        theta = np.deg2rad(theta)
        speed = float(speed)
        self.v = [speed*np.cos(theta), speed*np.sin(theta)]
        self.theta = theta
        self.a = a
        self.bounces = bounces
        self.C=C


        self.startr = [0, h]
        self.startv = self.v
        self.starta = self.a
        
    
    def sim(self):
        self.t=0
        dt = 1/FPS
        self.r=self.startr
        self.coords = []
        current_bounces=0
        while current_bounces<=self.bounces:
            self.coords.append([self.r[0], self.r[1]])
            for i in range(2):
                self.r[i]=self.r[i]+ self.v[i]*dt + 0.5*self.a[i]*dt**2
                self.v[i]=self.v[i]+ self.a[i]*dt
            if self.r[1]<=0: #bounce
                self.r[1]=0
                self.v[1]=-self.v[1]*self.C
                current_bounces+=1
            self.t+=dt

        dx = np.diff([i[0] for i in self.coords])
        dy = np.diff([i[1] for i in self.coords])
        self.distance = sum(np.sqrt(dx**2+dy**2))


