import matplotlib
from math import *
import inspect

class Point:

    def __init__(self, abscisse, ordonnee):
        self.abscisse = abscisse
        self.ordonnee = ordonnee

    def __str__(self):
        return "Abscisses = " + str(self.abscisse) + " Ordonnées = " + str(self.ordonnee)    

    def translater(self, a, b):
        return Point(self.abscisse + a, self.ordonnee + b)

def distance(point1, point2):
    x1 = point1.abscisse
    x2 = point2.abscisse
    y1 = point1.ordonnee
    y2 = point2.ordonnee
    return sqrt((x1-x2)**2 + (y1-y2)**2) 
# Exercice 2
class Triangle:
    def __init__(self, s1:Point, s2:Point, s3:Point):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def perimetre(self):
        return distance(self.s1, self.s2) + distance(self.s1, self.s3) + distance(self.s2, self.s3)

def translate_triangle(T:Triangle,a,b):
    new_T=T
    new_T.s1.translater(a,b)
    new_T.s2.translater(a,b)
    new_T.s3.translater(a,b)
    return new_T



A = Point(10,10)
B = Point(20,20)
C = Point(30,15)

print(A)
print(B)
print(C)

print(Point.translater(A,3,3))
print(Point.translater(A,3,3))
print(distance(A, B))

triangle = Triangle(A,B,C)
print(triangle.perimetre())

new_t=translate_triangle(triangle,5,10)
print(new_t.s1,new_t.s2,new_t.s3)
