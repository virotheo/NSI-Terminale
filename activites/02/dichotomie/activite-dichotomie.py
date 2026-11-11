def effectif(val,lst):
    result = 0
    for i in lst:
        if val == i:
            result += 1
    return result

print(effectif(1,[1, 4, 1, 6, 1, 7, 2, 1, 1])) #  5

def majo_abs_1(lst):
    moitie_liste = len(lst)//2
    for val in lst:
        if effectif(val,lst) > moitie_liste:
            return val
    return None

print(majo_abs_1([1,2,3,4,5,6,7,8,9,1,1,1,1,1,1,1,1,1,1])) # [1]
print(majo_abs_1([1,2,3,4,5,6,7,8,9])) # None

def eff_dico(lst):
    dico_sortie = {}
    for element in lst:
        cle = str(element)
        if element in dico_sortie:
            dico_sortie[element] += 1
        else:
            dico_sortie[cle] = 1
    return dico_sortie

print(eff_dico([1, 4, 1, 6, 1, 7, 2, 1, 1]))

def majo_abs2(lst)->list:
    n = len(lst)
    dico = eff_dico(lst)
    for val, eff in dico.items():
        if eff > n / 2:
            return val
    return None

def majo_abs3(lst):
    n = len(lst)
    if n == 1:
        return lst[0]                  
    else:
        lst_g = lst[:n//2]
        lst_d = lst[n//2:]
        maj_g = majo_abs3(lst_g)
        maj_d = majo_abs3(lst_d)
        if maj_g is not None:
            eff = effectif(maj_g, lst) 
            if eff > n/2:
                return maj_g
        if maj_d is not None:
            eff = effectif(maj_d, lst)
            if eff > n/2:
                return maj_d
    return None
