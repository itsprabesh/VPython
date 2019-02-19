from vpython import *
#GlowScript 2.7 VPython
#set constants and parameters  (all units in SI)
mblock = 1       #enter the mass of the block
ks =  15.797        #enter the measured spring constant
L0 =       0.3    #enter the unstretched spring length
Lstarty =  -0.99 #enter the starting location

g = 9.8
deltat = .01
t = 0

#create block and spring (origin at top of spring)
ceiling = box(pos=vec(0,0,0), length = 0.2, height = 0.01, width = 0.2)
block = box(pos = vector(0,Lstarty,0),size = vec(0.1,0.1,0.1), color = color.red)
spring = helix(pos= vec(0,0,0), axis = block.pos, radius = .03, thickness = 0.008, coils = 30, color = color.yellow)

#initial values
pblock = mblock*vector(0,0,0)
Fgrav =  mblock*vector(0,-g,0)   #enter the gravitational force  Why don't we have to recalculate this every time?

#set up graph
block_y = gcurve(color=block.color)
block_y.plot(pos=(t,block.pos.y))

#calculations
while t < 10:
    rate(20)
    L = block.pos
    Lhat = norm(L)
    s=mag(L)-L0
    Fspring=-ks*s*Lhat #or Lhat = L/mag(L)
                #enter the spring stretch
                #enter the spring force
    Fnet = Fspring + Fgrav          #net force
    if t == 0:
        print(Fnet)
    pblock = pblock + Fnet*deltat  #updata momentum
    block.pos = block.pos + (pblock/mblock)*deltat  #update position
    spring.axis=block.pos
    t = t + deltat
    
    block_y.plot([t,block.pos.y])  #plot the position of the block