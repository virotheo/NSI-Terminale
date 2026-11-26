'''
1a) 4 7 5 30 20 10 
1b) C'est le parcours infixe
2a) le 28 à gauche du 30
2b) 4
3a) La valeur renvoyée est 30 
3b) Cette valeur représente le plus grand nombre de l'arbre
4)
'''
def rechercher (a, e):
    if est_vide(a):
        return False
    elif a.racine == e :
        return True
    elif e < racine(a):
        return rechercher(sous_arbre_gauche, e)
    else:
        return rechercher(sous_arbre_droit, e)           
