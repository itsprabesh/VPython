from vpython import *
#GlowScript 2.7 VPython

#Defining the variables
s=1.19
n=1
A=5.83403
#Functions
def circleradius(A):
    return (A/pi)**(1/2)


#Creating the big circle
radius_big_circle=circleradius(A)
big_circle=cylinder(pos=vec(0,0,0), axis=vec(0,0,0.01), radius=radius_big_circle, opacity=0.9)
#List for the circle
circlelist=[]
#The total area of the circles
sum_circles=0
#Creating the first circle
    #sum_circles+=(1/n**s)
r=random()*1.36272-circleradius(1/n**s)
theta=random()*2*3.121592    
x=r*cos(theta)
y=r*sin(theta)
circle=cylinder(pos=vec(x,y,0.01), axis=vec(0,0,0.01), radius=circleradius(1/n**s), color=color.red)
circlelist.append(circle)
sum_circles+=(1/n**s)
#Checking the overlap

def checkoverlap(x,y, r,  circlelist):
    for index in circlelist:
        if mag(index.pos-vec(x,y,0.01))<index.radius+r:
            return True
    return False
n=2
while sum_circles<A:
    rate(50000000)
    #sum_circles+=(1/n**s)
    r=random()*1.36272-circleradius(1/n**s)
    theta=random()*2*3.141592
    x=r*cos(theta)
    y=r*sin(theta)
    if not checkoverlap(x,y, circleradius(1/n**s), circlelist):
        test_circle=cylinder(pos=vec(x,y,0.01), axis=vec(0,0,0.01), radius=circleradius(1/n**s), color=vec(random(),random(),random()))
        circlelist.append(test_circle)
        n=n+1

     