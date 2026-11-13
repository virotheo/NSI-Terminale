class Noeud:
    def __init__(self,cle,gauche,droit):
        self.cle = cle
        self.gauche = gauche
        self.droit = droit

class Arbre:
    def __init__(self, racine):
        self.racine = racine
    def sag(self):
        return Arbre(self.racine.gauche)
