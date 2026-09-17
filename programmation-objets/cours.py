import random 
import inspect

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur # Attribut 1 
        self.largeur = largeur # Attribut 2

    def calcul_aire(self):
        return self.longueur * self.largeur    

    def calcul_perimetre(self):
        return 2*(self.longueur + self.largeur)    

    def __str__ (self):
        return "Ce rectangle a pour longueur " + str(self.longueur) + " et pour largeur " + str(self.largeur)    

mon_rectangle1 = Rectangle(100,50)
mon_rectangle2 = Rectangle(100,50)

print(mon_rectangle1)
print(mon_rectangle1.longueur)

print(mon_rectangle1.calcul_aire())
print(mon_rectangle1.calcul_perimetre())

print(mon_rectangle1 == mon_rectangle2)

