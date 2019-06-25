from visual import *
from vpython import *
''' Simulation how a carrying loop creates a magnetic field and it creates a magnetic flux and how
    the variation in the flux in a movile loop creates an emf in the wire
'''
#CONSTANTS
Ndl=50 #divide the source loop into 50 segments
R=1 #Radius of the source
dllen=(2*pi*R)/Ndl # length of 1 segment of wire
mu = 1e-7 #Mu naught over pi
I = 10 #Current
ascale = 1e6
cscale = 1e4
frequency = 10
delta_time = (1/frequency)*0.02
offset = 2.5


CHARGES = []
for t in arange (0,2*pi+.0001,pi/Ndl):
    dl=arrow(pos=vec(R*cos(t),-2,R*sin(t)), axis=dllen*vec(-sin(t),0,cos(t)))
    CHARGES.append(dl)
    
coil = ring(pos=vec(0,2,0), axis=vec(0,1,0), radius=0.5, thickness=0.05, current = 5, loops = 50, color = color.red)

#MAGNETIC FIELD DUE TO THE WIRE
def BWire(r_obs, r_source, I, delta_l):
    r = r_source-r_obs
    rhat = norm(r)
    rmag = mag(r)
    return (mu*I*cross(delta_l,rhat))/(rmag**2)
    
ARROWS = [] 
item1 = arrow(pos = vec(0, 2 , 0), axis = vec(0,0.1,0), color = color.green)
ARROWS.append(item1)

for theta in arange(0, 2*pi, pi/4): 
    item1 = arrow(pos = vec( 0.1*sin(theta), 2 ,  0.1*cos(theta)), axis = vec(0,0.1,0), color = color.green)
    ARROWS.append(item1)


for theta in arange(0, 2*pi, pi/6): 
    item1 = arrow(pos = vec( 0.2*sin(theta), 2 ,  0.2*cos(theta)), axis = vec(0,0.1,0), color = color.green)
    ARROWS.append(item1)

for theta in arange(0, 2*pi, pi/8): 
    item1 = arrow(pos = vec( 0.3*sin(theta), 2 ,  0.3*cos(theta)), axis = vec(0,0.1,0), color = color.green)
    ARROWS.append(item1)

for theta in arange(0, 2*pi, pi/10): 
    item1 = arrow(pos = vec( 0.4*sin(theta), 2 ,  0.4*cos(theta)), axis = vec(0,0.1,0), color = color.green)
    ARROWS.append(item1)
    

from visual.graph import *    # import graphing features 
graph1 = gdisplay(xtitle = 'Time', ytitle= 'emf                       Total Magnetic Flux')
f1 = gcurve(color=color.cyan) # a graphics curve
f2 = gcurve(color=color.green)
f1.plot(pos=(0,0))    # plot  
time = 0
#initial_flux = 0
while True:
    rate(100)
    area_coil = pi * coil.radius*coil.radius
    dA = area_coil  / 57
    coil.pos.y = (1+0.5*sin(2*pi*frequency*time))
    time += delta_time
    #total_b = 0
    total_flux = 0
    for arrow in ARROWS:
        temp = vec(0,0,0)
        arrow.pos.y = coil.pos.y
        for charge in CHARGES:
            temp += BWire(arrow.pos, charge.pos, I, charge.axis)
        arrow.axis = temp*ascale 
        total_flux = total_flux + dA*arrow.axis.y/ascale 
        final_flux = total_flux     
    f1.plot(pos=(time, total_flux))
    emf_induced = (-(final_flux-initial_flux)*coil.loops)/delta_time
    initial_flux = final_flux
    f2.plot(pos=(time,emf_induced/cscale))
    print(emf_induced)
