import numpy as np

class DParticle:
    def __init__(self, h, speed, theta, g, Cd, rho, m, A):
        self.r = [0, h]
        theta = np.deg2rad(theta)
        speed = float(speed)
        self.v = [speed*np.cos(theta), speed*np.sin(theta)]
        self.theta = theta
        self.a = [0, -g]
        self.g=g
        self.k = (Cd*rho*A)/(2*m)


        self.startr = [0, h]
        self.startv = self.v
        self.starta = self.a
        
    
    def sim(self):
        done=False
        t=0
        dt = 0.002
        self.r=self.startr
        self.coords = []
        while self.r[1]>=0:
            self.coords.append([self.r[0], self.r[1]])
            
            vel = np.sqrt(self.v[0]**2+self.v[1]**2)
            self.a[0] = (-self.v[0]*self.k*vel**2)/vel
            self.a[1] = -self.g -(self.v[1]*self.k*vel**2)/vel #formula for acceleration
            for i in range(2):
                self.r[i]=self.r[i]+ self.v[i]*dt + 0.5*self.a[i]*dt**2
                self.v[i]=self.v[i]+ self.a[i]*dt
            t+=dt
            if self.v[1]<=0 and done==False:
                self.apogee=self.r
                done=True
        dx = np.diff([i[0] for i in self.coords])
        dy = np.diff([i[1] for i in self.coords])
        self.distance = sum(np.sqrt(dx**2+dy**2))


    #def reset(self, new_speed):
    #    self.r=self.startr
    #    print(new_speed)
    #    self.v=[new_speed*float(np.cos(self.theta)), new_speed*float(np.sin(self.theta))]
    #    self.a=self.starta
    
