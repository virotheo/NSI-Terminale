class Arbre:
    def __init__(self, etiquette, sous_arbre_gauche=None, sous_arbre_droit=None):
        self.etiquette = etiquette
        self.sous_arbre_gauche = sous_arbre_gauche
        self.sous_arbre_droit = sous_arbre_droit

    def pgde_somme(self):
        if self.sous_arbre_gauche != None and self.sous_arbre_droit != None:
            hg = self.sous_arbre_gauche.pgde_somme()
            hd = self.sous_arbre_droit.pgde_somme()
            return self.etiquette + max(hg,hd)
        if self.sous_arbre_gauche != None:
            return self.etiquette + self.sous_arbre_gauche.pgde_somme()
        if self.sous_arbre_droit != None:
            return self.etiquette + self.sous_arbre_droit.pgde_somme()
        return self.etiquette

    def est_magique(self)->bool:
        if self.sous_arbre_gauche != None and self.sous_arbre_droit != None:
            return self.sous_arbre_gauche.est_magique() and self.sous_arbre_droit.est_magique() \
                and self.sous_arbre_gauche.pgde_somme() == self.sous_arbre_droit.pgde_somme()
        elif self.sous_arbre_gauche != None:
            return self.sous_arbre_gauche.est_magique()
        elif self.sous_arbre_droit != None:
            return self.sous_arbre_droit.est_magique()
        return True    



# --- Partie de ce code généré avec IA (Gemini)
if __name__ == "__main__":
    #        10
    #       /  \
    #      5    3
    #     /    / \
    #    2    4   4
    feuille_2 = Arbre(2)
    feuille_4a = Arbre(4)
    feuille_4b = Arbre(4)
    noeud_5 = Arbre(5, feuille_2, None)
    noeud_3 = Arbre(3, feuille_4a, feuille_4b)
    arbre_magique = Arbre(10, noeud_5, noeud_3)

    print("Plus grande somme  :", arbre_magique.pgde_somme())
    print("Est magique  :", arbre_magique.est_magique())

    #        10
    #       /  \
    #      5    3
    #     /    / \
    #    2    4   1 
    noeud_3_faux = Arbre(3, feuille_4a, Arbre(1))
    arbre_non_magique = Arbre(10, noeud_5, noeud_3_faux)

    print("Plus grande somme  :", arbre_non_magique.pgde_somme())
    print("Est magique  :", arbre_non_magique.est_magique())
