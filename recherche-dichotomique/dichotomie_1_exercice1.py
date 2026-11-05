def rechDichoIter(T,l,r,val):
    indice_gauche = l
    indice_droit = r
    while indice_gauche<=indice_droit:
        m = (indice_gauche+indice_droit)//2 
        if val == T[m]:
            return True
        elif val < T[m]:
            indice_droit = m-1 # val is not equal to T[m] so we can exclude m to save a few calculations
        else:
            indice_gauche = m+1
    return False            # if loop ends and found nothing it returns False


T = [1,2,3,4,5]    # list
print('----------------------------------------')
print('Iterrative Version')

print('----------------------------------------')


print(rechDichoIter(T,0,4,2)) # Test 1
print(rechDichoIter(T,0,4,38)) # Test 2
print(rechDichoIter(T,0,4,10)) # Test 3

print('----------------------------------------')
print('Recursive Version')

print('----------------------------------------')

#----------------------------------------------------
# Recursive Version
#----------------------------------------------------

def rechDichoRecu(T,l,r,val):
    indice_g = l
    indice_d = r
    m = (indice_g + indice_d)//2
    if indice_g <= indice_d:
        if val == T[m]:
            return True
        elif val < T[m]:
            return rechDichoRecu(T,l,m-1,val)
        else:
            return rechDichoRecu(T,m+1,r,val)
    return False        

print(rechDichoIter(T,0,4,2)) # Test 1
print(rechDichoIter(T,0,4,38)) # Test 2
print(rechDichoIter(T,0,4,10)) # Test 3
