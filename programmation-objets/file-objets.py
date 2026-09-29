class Cellule:
    def __init__(self,val,suivant=None):
        self.valeur=val
        self.suivant=suivant

class File:
    def __init__(self,valeur=None):
        self.tete = None

    def fileEstVide(self):
        return self.tete == None

    def fileRenvoyerTete(self):
        if not self.fileEstVide():
            return self.tete.valeur
        return None

    def fileEnfiler(self,valeur):
        if self.fileEstVide():
            self.tete = Cellule(valeur, None)
        else:
            x = self.tete
            while x.suivant != None:
                x = x.suivant
            x.suivant = Cellule(valeur, None)        

    def fileDefiler(self):
        if not self.fileEstVide():
            x = self.tete
            self.tete = x.suivant
            return x.valeur

        return None    

    def fileAfficher(self):
        x = self.tete
        while x != None:
            print(x.valeur, end='  ')
            x = x.suivant

def tests():
    maFile = File()
    maFile.fileEnfiler(10)
    maFile.fileEnfiler(20)
    maFile.fileEnfiler(30)    
    maFile.fileAfficher()

print(tests())
