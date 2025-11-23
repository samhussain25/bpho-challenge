if resistance==True:
            v = np.sqrt(vx**2+vy**2)
            ax = (-vx*k*v**2)/v
            ay = -g -(vy*k*v**2)/v #formula for acceleration