from tkinter import *
from tkinter import ttk
import random

# initialization
root = Tk()
root.title("Taquin")
frm = ttk.Frame(root, padding=10)
frm.grid()

#examples
tab = [5,3,8,0,1,2,7,6,4]
tab1 = [1,2,3,4,5,6,7,8,0]

class Taquin:
    def __init__(self):
        self.tab = [0,1,2,3,4,5,6,7,8]

    def est_gagnante(self,tab:list)->bool:
        y = 1
        for x in range(8):
            if self.tab[x] == y:
                x+=1
                y+=1
                if x == 7:
                    return True
            else:
                return False        

    def indice(self, numero):
        assert type(numero) == int, 'numero doit etre entier'
        assert numero >= 1 or numero <= 9, 'numero de cas non valide'
        i = 0
        while tab[i] != numero:
            i += 1
        return i

    def est_possible(self,numero):
        
    def jouer(self,numero):
        if est_possible(numero) == True:
            i = self.indice(numero)
            j = self.indice(0)
            j = numero
            i = 0

    def melanger(self,n):
        precedent = None
        i = 0
        while i!= n:
            possibilites = t;coups_possibles()
            choix = random.choice(tab)
            if choix != precedent:
                self.jouer(choix)
                precedent = choix
                i += 1        
                 

# geometry
root.geometry("500x500")
root.minsize(500,500)
root.maxsize(500,500)






 








# leaving button
ttk.Button(frm, text="Quit", command=root.destroy).pack(padx=200,pady=450)

root.mainloop()   # keep the window running
