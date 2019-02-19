from vpython import *
#GlowScript 2.7 VPython
G=6.7e-11  #Gravitational Constant
mplanet=6e24 #Mass of the planet
rplanet=6.4e6 #Radius of the planet 
mcraft=15e3 #mass of the spacecraft
mmoon=7e22 #mass of the moon
rmoon=1.75e6 #radius of the moon
planetloc=vector(0,0,0) #location of the planet
craftloc=vector(-10*rplanet,0,0) #initial location of spacecraft
moonloc=planetloc+vec(4e8,0,0) #location of the moon
dt=10 #deltat
#prepare the display

displaymax = 10
scene.range= displaymax

physicalmax=mag(moonloc)
scalefactor=displaymax/physicalmax

planet = sphere(pos=planetloc, radius=rplanet*scalefactor, texture="https://i.imgur.com/do31Gdf.jpg")

craft = sphere(pos=craftloc*scalefactor, radius= 0.2, color=color.white, make_trail=True)

moon = sphere(pos=moonloc*scalefactor, radius=rmoon*scalefactor, color=color.cyan)

# initial values

vcraft=vector(0,3.2735e3,0) #initial velocity of the craft
pcraft=mcraft*vcraft #momentum of the craft 
t=0 #time begins

#Calculation
while t<5e7:
    rate(10000)
    t=t+dt #update the time
    rearthcraft=craftloc-planetloc #distance between the planet and the craft
    recmag=mag(rearthcraft) #magnitude of distance between the planet and the craft
    Fearth= -(G*mplanet*mcraft)/recmag**2 #calculating the force exerted on the craft by the earth
    rhatec=norm(rearthcraft) #calculating the unit vector of the direction from earth to the craft
    Fgearth=Fearth*rhatec #finding the vector force exerted by the earth to the craft
    rmooncraft=craftloc-moonloc #finding the distance between teh craft and the moon
    rmcmag=mag(rmooncraft) #finding the magnitude of distance between the moon and the craft
    Fmoon= -(G*mmoon*mcraft)/rmcmag**2 #calculating the magnitude of the force exerted by the the moon to the craft
    rhatmc= norm(rmooncraft) #calculating the unit vector of the direction form the moon to the craft
    Fgmoon=rhatmc*Fmoon #calculating the vector force exerted by the moon on the craft
    Fg=Fgmoon+Fgearth #calculating the total force on the spacecraft
    pcraft=pcraft+Fg*dt #updating the momentum of the craft with the momentum we just calculated with the code all above
    craft.pos=craft.pos+(pcraft/mcraft)*dt #updating the position of the craft
    craftloc=craftloc+(pcraft/mcraft)*dt #update the location of the craft
    craft.pos=craftloc*scalefactor #updating the craft according to the scale factor of the screen
    if recmag < rmoon:
        break
    if rmcmag< rplanet:
        break
    
    
    
    
    
    
    



    