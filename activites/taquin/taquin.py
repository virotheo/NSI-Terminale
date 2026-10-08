from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
# Théo BODIN Terminale 1
# solver site si bloqué : https://www.dcode.fr/solveur-taquin

tab = [5,3,8,0,1,2,7,6,4]
tab1 = [1,2,3,4,5,6,7,8,0]

class Taquin:
    def __init__(self):
        self.tab = [0,1,2,3,4,5,6,7,8]
        self.pile = Pile()
        self.mode_resolution = False

    def est_gagnant(self,):
        return self.tab == [0,1,2,3,4,5,6,7,8]      

    def indice(self, numero):
        assert type(numero) == int, 'numero doit etre entier'
        assert 0 <= numero <= 8, 'numero de case non valide'
        i = 0
        while self.tab[i] != numero:
            i += 1
        return i
        
    def jouer(self,numero):
        if self.est_possible(numero) == True:
            i = self.indice(numero)
            j = self.indice(0)
            self.tab[j] = numero
            self.tab[i] = 0
            if not self.mode_resolution:
                if not self.pile.est_vide():
                    sommet = self.pile.depiler()
                    if sommet != numero:
                        self.pile.empiler(sommet)
                        self.pile.empiler(numero)
                else:
                    self.pile.empiler(numero)

    def melanger(self,n):
        precedent = None
        i = 0
        while i!= n:
            possibilites = self.coups_possibles()
            choix = random.choice(possibilites)
            if choix != precedent:
                self.jouer(choix)
                precedent = choix
                i += 1        
    def coups_possibles(self):
        return [n for n in range(1, 9) if self.est_possible(n)]     

    def resoudre(self):
        self.mode_resolution = True
        while not self.pile.est_vide():
            numero = self.pile.depiler()
            self.jouer(numero)
            print(numero)
        self.mode_resolution = False

    def est_possible(self, numero) -> bool:
        i = self.indice(numero)
        j = self.indice(0)
    
        if (j == i + 1 or j == i - 1) and (i // 3 == j // 3):
            return True
        
        if j == i + 3 or j == i - 3:
            return True
        
        return False


class Pile(list):
    def est_vide(self):
        return len(self) == 0    
    def empiler(self,valeur):
        self.append(valeur)
    def depiler(self):
        if not self.est_vide():
            return self.pop()
        return None

root = Tk()
root.title("Taquin")
root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)
# A Partir d'ici, code généré par IA (Gemini) pour l'interface Tkinter
frm = ttk.Frame(root, padding=10)
frm.grid()

boutons_grille = []

def actualiser_grille():
    for i in range(9):
        valeur = jeu.tab[i]
        if valeur == 0:
            boutons_grille[i].configure(text="", state="disabled")
        else:
            boutons_grille[i].configure(
                text=str(valeur), 
                state="normal", 
                command=lambda v=valeur: clic_bouton(v)
            )

def clic_bouton(numero):
    jeu.jouer(numero)
    actualiser_grille()
    if jeu.est_gagnant(): 
        messagebox.showinfo("Taquin", "Bravo, le taquin est résolu !")

def bouton_melanger():
    jeu.melanger(10) 
    actualiser_grille()
    if jeu.est_gagnant(): 
        messagebox.showinfo("Taquin", "Bravo, le taquin est résolu !")

def bouton_resoudre():
    jeu.resoudre()
    actualiser_grille()

jeu = Taquin()    

grille_frame = ttk.Frame(frm)
grille_frame.pack(pady=20)

for i in range(9):
    btn = ttk.Button(grille_frame, width=5)
    btn.grid(row=i // 3, column=i % 3, padx=5, pady=5, ipadx=10, ipady=10)
    boutons_grille.append(btn)

actions_frame = ttk.Frame(frm)
actions_frame.pack(pady=10)

ttk.Button(actions_frame, text="Mélanger", command=bouton_melanger).pack(side="left", padx=5)

ttk.Button(actions_frame, text="Résoudre", command=bouton_resoudre).pack(side="left", padx=5)

ttk.Button(frm, text="Quitter", command=root.destroy).pack(pady=10)

actualiser_grille()

root.mainloop()
