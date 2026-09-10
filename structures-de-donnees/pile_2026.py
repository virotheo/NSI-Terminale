def creePile():
    return []

def pileEstVide (P):    
    return len(P) == 0

def pileEmpiler (P, element):
    P.append(element)

def pileDepiler(P):
    if not pileEstVide(P):
        return P.pop()
    return None

def pileSommet(P):
    if not pileEstVide(P):
        return P[-1]
    return None

def pileVider(P):
    while not pileEstVide(P):
        pileDepiler(P)
    return

def sortpile(P):
    if pileEstVide(P):
        return
    else:
        element = pileDepiler(P) 
        if element % 2 == 0:
            pileEmpiler(pilePair, element)
        else:
            pileEmpiler(pileImpair, element)
        sortpile(P)