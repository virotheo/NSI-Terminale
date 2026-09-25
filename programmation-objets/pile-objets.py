class Cellule:
    def __init__(self,valeur,suivant=None):
        self.valeur = valeur
        self.suivant = suivant

class Pile:
    def __init__(self,valeur=None):
        self.sommet = Cellule(valeur)
    def pileEstVide(self):
        return self.sommet == None
    def pileRenvoyerSommet(self):
        if not self.pileEstVide():
            return self.sommet.valeur
        return None        
    def pileEmpiler(self,val):
        self.sommet = Cellule(val, self.sommet)
    def pileDepiler(self):
        if self.pileEstVide():
            return        # même chose que return None
        x = self.sommet
        self.sommet = x.suivant
        return x.valeur    

mapile = Pile()
mapile.pileEmpiler(5)
mapile.pileEmpiler(10)
mapile.pileEmpiler(20)
print(mapile.sommet.valeur)
mapile.pileDepiler()
print(mapile.sommet.valeur)

