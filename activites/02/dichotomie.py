def effectif(val,lst):
    result = 0
    for i in lst:
        if val == i:
            result += 1
    return result

print(effectif(1,[1, 4, 1, 6, 1, 7, 2, 1, 1])) #  5

# Question 2 -------------

def nombre_inversion(tab):
    cpt = 0 
    for i in range(len(tab)):
        cpt += effectif(tab,i)
    return cpt
# --------    


'''
constante O(n)
linéaire = O(n)
quadratique = O(n²)
tri fusion O(n*log(n))
'''

def moitie_gauche(tab):
    lst_gauche = []
    n = len(tab)
    if n%2 == 0:
        for i in range(n//2):
            lst_gauche.append(tab[i])
    else:
        for i in range(n//2+1):
            lst_gauche.append(tab[i])
    return lst_gauche

def moitie_droite(tab):
    lst_droite = []
    n = len(tab)
    if n%2 == 0:
        for i in range(n//2,n):
            lst_droite.append(tab[i])
    else:
        for i in range(n//2+1,n):
            lst_droite.append(tab[i])
    return lst_droite

print("Testing moitie_gauche function : ")
# test with even list    
print(moitie_gauche([1,5,5,4,6,8]))                
print(moitie_droite([1,5,5,4,6,8]))   
print('\n')
print("Testing moitie_gauche function : ")
     
# test with odd list
print(moitie_gauche([5,3,4,9,6]))    
print(moitie_droite([5,3,4,9,6]))                

def nb_inv_tab(tab1, tab2):
    # tab1 and tab2 already sorted
    cpt = 0
    for elem1 in tab1:
        for elem2 in tab2:
            if elem1 > elem2:
                cpt += 1 
            else:
                break
    return cpt            

print('------------------------')
def nombre_inversions_rec(tab):
    mg = moitie_gauche(tab)
    md = moitie_droite(tab)
    if len(tab) == 1:
        return 0
    mg1 = sorted(mg)
    md1 = sorted(md)
    return nombre_inversions_rec(mg) + nombre_inversions_rec(md) + nb_inv_tab(mg1, md1)

print(nombre_inversions_rec([7,6,5,3]))    
