def creeFile():
    return []

def fileEstVide (F):    
    return len(F) == 0

def fileEnfiler (F, element):
    F.append(element)

def fileDefiler(F):
    if fileEstVide(F):
        return None
    else:
        return F.pop(0)

def filetete(F):
    return F[0]    

def fileTaille(F):
    return len(F)    
 
def fileVider(P):
    while not fileEstVide(P):
        fileDefiler(P)
    return
