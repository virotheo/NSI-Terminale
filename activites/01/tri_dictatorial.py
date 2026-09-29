def tri_dictatorial(serie:list)->list:
    try: serie2 = [serie[0]]
    except IndexError:
        return serie 
    for i in range(1,len(serie)):
        if serie[i] >= serie[i - 1]:
            serie2.append(serie[i])
    return serie2                

liste_a_trier = [8,2,9,6,12]        
print(tri_dictatorial([]))
