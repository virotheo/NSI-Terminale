#exercice3_correction.py
import matplotlib
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from math import *
import inspect

class Point:

    def __init__(self, abscisse, ordonnee):
        self.abscisse = abscisse
        self.ordonnee = ordonnee

    def __str__(self):
        return "("+str(self.abscisse) + "," + str(self.ordonnee)+")"
    
    def as_tuple(self):
        return self.abscisse,self.ordonnee

def translater(A,a,b):
    return Point(A.abscisse + a, A.ordonnee + b)

def homothetie(A,Omega,k):
    x = A.abscisse
    y = A.ordonnee
    w1 = Omega.abscisse
    w2 = Omega.ordonnee
    return Point(k*(x-w1)+w1, k*(y-w2) + w2)

    

def rotation(A,Omega, teta):
    x = A.abscisse
    y = A.ordonnee
    w1 = Omega.abscisse
    w2 = Omega.ordonnee
    a, b = cos(teta) , sin(teta)
    return Point(a*(x-w1)-b*(y-w2)+w1,b*(x-w1)+a*(y-w2)+w2)

class PolyReg:

    def __init__(self,centre,sommet,n):
        self.nbrsommet = n
        self.centre = centre
        self.Sommet = [sommet]
        A = sommet
        for i in range(n-1):
            image = rotation(A,centre,2*pi/n)
            self.Sommet.append(image)
            A = image
        
    def tracer(self,couleur="black",do_fill=False):
        temp=[]
        for x in self.Sommet:
            temp.append(x.as_tuple())
        tr=patches.Polygon(temp,fill=do_fill,color=couleur)
        ax.add_patch(tr)    


def poly_homothetie(T:PolyReg,centre:Point,k:float)->PolyReg:
    return PolyReg(homothetie(T.centre,centre,k), homothetie(T.Sommet[0], centre,k),T.nbrsommet)



fig, ax=plt.subplots()
ax.set_xlim(-100,100)
ax.set_ylim(-100,100)
ax.set_aspect('equal',adjustable='box')

A = Point(10,10)
B = Point(50,35)
C = Point(25,25)
D = Point(60,60)
T = PolyReg(B,A,16)
T1 = PolyReg(A,C,8)
T2 = PolyReg(D,B,1000)
T3 = PolyReg(C,A,1000)
print(poly_homothetie(T,B,1))
print(poly_homothetie(T1,A,1.5))
print(poly_homothetie(T2,D,2))
print(poly_homothetie(T3,C,3))

plt.show()

