from vpython import *
#GlowScript 2.7 VPython
alphamass=4*1.7e-27
alphacharge=2*1.6e-19
alpharadius=1e-15
goldmass=197*1.7e-27
goldcharge=79*1.6e-19
goldradius=6e-15
goldmomentum=vector(0,0,0)
b=1e-14
gold=sphere(pos=vec(0,0,0),radius=goldradius,color=color.yellow, make_trail=True)
alpha=sphere(pos=vec(-3e-13,b,0),radius=alpharadius,color=color.green,make_trail=True)
alphamomentum=vec(1e-19,0,0)
scene.range=2*mag(alpha.pos)
deltat=4.082e-20/1000

##########################

electricforcehat=norm(alpha.pos-gold.pos)
electricforce=goldcharge*alphacharge*9e9/mag(alpha.pos-gold.pos)**2
alpha.pos=alpha.pos+alphamomentum/alphamass*deltat
electricforcevector=electricforce*electricforcehat
print(electricforce)
##########################
arrow=arrow(pos=vec(-3e-13,b,0), axis=(electricforcevector/0.404)*1e-13, color=color.red)

dinitial=mag(alpha.pos)


t=0

#Graph
X_momentum = gdisplay(xtitle = 'Time', ytitle= 'Px',height=200)
Alphapx = gcurve(color = color.cyan)
Aupx = gcurve(color=color.yellow)
totalpx = gcurve(color = color.green)
Y_momentum = gdisplay(xtitle = 'Time', ytitle = 'Py',height=200)
Alphapy = gcurve(color = color.cyan)
Aupy = gcurve(color=color.yellow)
totalpy = gcurve(color= color.green)
b=dinitial
#print(deltat,dinitial,mag(alpha.pos))

while mag(alpha.pos-gold.pos)<1.1*dinitial:
    rate(1000)
    electricforcehat=norm(alpha.pos-gold.pos)
    electricforce=goldcharge*alphacharge*9e9/mag(alpha.pos-gold.pos)**2
    alpha.pos=alpha.pos+alphamomentum/alphamass*deltat
    electricforcevector=electricforce*electricforcehat
    alphamomentum=alphamomentum+electricforcevector*deltat
    goldmomentum=goldmomentum-electricforcevector*deltat
    gold.pos=gold.pos+(goldmomentum/goldmass)*deltat
    t=t+deltat
    arrow.pos=alpha.pos
    arrow.axis=electricforcevector/0.4e-13
    
    if  b<mag(gold.pos-alpha.pos):
        b=mag(gold.pos-alpha.pos)
    
    Alphapx.plot(pos=(t,alphamomentum.x))
    Alphapy.plot(pos=(t,alphamomentum.y))
    Aupx.plot(pos=(t,goldmomentum.x))
    Aupy.plot(pos=(t,goldmomentum.y))
    totalpx.plot(pos=(t,goldmomentum.x+alphamomentum.x))
    totalpy.plot(pos=(t,goldmomentum.y+alphamomentum.y))
print(b)
print(atan((alphamomentum.y/alphamomentum.x))*(180/3.14)+180)