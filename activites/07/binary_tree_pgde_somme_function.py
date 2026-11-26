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
