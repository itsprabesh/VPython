from vpython import *
from visual import *

#define constrains and their values

k = 9e9 #Coulomb's constant
q = 1.6e-19 #fundamental charge of a particle

L = 10
scene.range = L #full scale screen dimension( +/- L in each direction)
dscale = 1e-10 #Physical distance corresponding to 1 unit of the screen

rp = vec(0,1,0)*dscale #the proton placed at  <0,1e-10,0>
re = vec(0,-1,0)*dscale #the electron placed at <0,-1e-10,0>

curve(pos = [vec(0,0,0),vec(L,0,0)], thickness = .01) # x axis
curve(pos = [vec(0,0,0),vec(0,L,0)], thickness = .01) # y axis

charge = sphere(pos=vec(0,1,0), radius=0.25, color=color.red)
charge2 = sphere(pos=vec(0,-1,0), radius=0.25, color=color.green)

Earrow = arrow(pos=vec(0,0,0), axis=vec(0,0,0), color = color.red, opacity = 0.5)
Earrow1 = arrow(pos=vec(0,0,0), axis=vec(0,0,0), color = color.green, opacity = 0.5)
Earrow_net = arrow(pos=vec(0,0,0), axis=vec(0,0,0), color = color.blue, opacity =1)


Label1 = label(pos= vec(-L,L*(3/4),0), text="Electric field of a point charge",opacity=0,box=0, line=0, align = 'left')
Label2 = label(pos= vec(-L,L*(2/3),0), text="",opacity=0, box=0, line=0, align = 'left')
Label3 = label(pos= vec(L/2,L*(2/3),0), text="Test",opacity=0, box=0, line=0, align = 'left')


def EField(r_obs,Q,rQ):
    R = r_obs-rQ
    if mag(R) == 0: 
        return vec(0,0,0) # avoid calculating E at the charge's own location
    
    E = k*Q*norm(R)/(mag(R)**2)
    return E

Escale = mag(EField(vec((L/2)*dscale,0,0),q,rp))
Escale1 = mag(EField(vec((L/2)*dscale,0,0),q,re))
Escale_net = mag(EField(vec((L/2)*dscale,0,0), q, re+rp))

while True:

#This loop calculates the electric field E at the location r
#corresponding to the mouse position, displays
#the values of r and E and draws an arrow to represent E at
#the mouse position

    rate(100)
    rmouse = scene.mouse.pos # location of mouse in screen coordinates
    r = rmouse*dscale # physical location of observation point
    E = EField(r,q,rp) # electric field at observation point due to proton
    Ee = EField(r,-q,re) #electric field at observation point due to electron
    E_net = E + Ee

#update the display

    Label1.text = " r = " + str(r)
    Label2.text = "E = " + str(E)
    Label3.text = " Net E = " + str(E_net) 
    Earrow.pos = rmouse
    Earrow1.pos = rmouse
    Earrow_net.pos = rmouse
    Earrow.axis = (E/Escale) # Scale the arrow relative to E at reference point
    Earrow1.axis = (Ee/Escale1)
    Earrow_net.axis = (E_net/Escale_net)








