import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

class Point:

    def __init__(self, abscisse, ordonnee):
        self.abscisse = abscisse
        self.ordonnee = ordonnee

    def __str__(self):
        return (str(self.abscisse) + str(self.ordonnee))

class Triangle:
    def __init__(self, s1:Point, s2:Point, s3:Point):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def tracer(self, couleur='black'):
        # Obtenir l'objet axes
        fig, ax = plt.subplots()
        # Ajuster les limites du graphique
        ax.set_xlim(-100, 100)
        ax.set_ylim(-100, 100)
        ax.set_aspect('equal', adjustable = 'box') # Pour un tracé non déformé
        tr = patches.Polygon([(self.s1.abscisse,self.s1.ordonnee),(self.s2.abscisse,self.s2.ordonnee),(self.s3.abscisse,self.s3.ordonnee)],fill = True, color=couleur, alpha=0.5)
        ax.add_patch(tr)
A = Point(25,25)
B = Point(70,70)
C = Point(50,15)
T = Triangle(A,B,C)
plt.gca().set_axis_off()
print(Triangle.tracer(T))
# Afficher le graphique
plt.title("Exemple de polygone tracé avec matplotlib")
#plt.grid(True)
plt.show() 
