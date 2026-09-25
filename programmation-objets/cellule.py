class Cellule:
    def __init__(self,valeur,suivant=None):
        self.valeur = valeur
        self.suivant = suivant

class Liste:
    def __init__(self,valeur):
        self.tete = Cellule(valeur)

    def listeEstVide(self):
        return self.tete == None

    def retournerTete(self):
        if not self.listeEstVide():
            return self.tete.valeur
        return None
    def ajouterTete(self,valeur):
        x = self.tete
        nouveau = Cellule(valeur,x)
        self.tete = nouveau
    def listeTaille(self):
        nb_cellules = 0
        x = self.tete
        while x != None:
            nb_cellules +=1
            x = x.suivant
        return nb_cellules
    def listeRetournerElement(self,n):
        # renvoie la valeur de rang n dans la liste 
        # ou la nieme valeur
        # la tete de la liste est le premier élément
        assert n >= 1 and n <= self.listeTaille()
        x = self.tete
        for i in range(n-1):
            x = x.suivant
        return x.valeur        
maliste = Liste(25)
maliste.ajouterTete(8)
maliste.ajouterTete(7)    
print(maliste.listeTaille())        
print(maliste.listeRetournerElement(2))        
