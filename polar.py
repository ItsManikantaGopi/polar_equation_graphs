#exp(sin(o))-2*cos(4*o)+(sin((2*o-pi)/24))
from matplotlib import pyplot as plt
from mpmath import *
from matplotlib import *
from numpy import *

plt.style.use('dark_background')
def polar():
    print("use o for theta")
    at=eval(input("eneter the theta initial point:-"))
    bt=eval(input("eneter the theta final point:-"))
    tt=arange(at,bt+0.0001,0.0001)
    r=input("enter the  equation : r=")
    x=[]
    y=[]
    for i in range(len(tt)):
             o=O=tt[i]
             xa=eval(r)*cos(o)
             x.append(xa)
             ya=eval(r)*sin(o)
             y.append(ya)
    d=0
    for i in range(len(x)-1):
        d=d+sqrt(((x[i+1]-x[i])**2)+((y[i+1]-y[i])**2))
    #print("length of the curve:=",d)
    plt.plot(x,y,color='blue')
    plt.fill(x,y,color='white',alpha=0.9)
    plt.title("r="+r+" , o=Ø\n"+"length of the curve :="+str(d))
    plt.show()    
while(1):
    polar()
    print("======================================================================")

