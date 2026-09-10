from file_2026 import *
from pile_2026 import * 

mafile = creeFile()

fileEnfiler(mafile, 'a')
fileEnfiler(mafile, 'b')
fileEnfiler(mafile, 'c')
fileEnfiler(mafile, 'd')

def fileInverser(F):
    pile_inverser = creePile()
    while not fileEstVide(F):
        element = fileDefiler(F)
        pileEmpiler(pile_inverser, element)
    while not pileEstVide(pile_inverser):
        element2 = pileDepiler(pile_inverser)
        fileEnfiler(F, element2) 
    return F    

print(fileInverser(mafile))
