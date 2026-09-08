'''
f(5) = 5 x fac(4)
fac(4) = 4 x fac(3)
etc...
fac(1) = 1 x facc(0)
fac(0) = 1 (convention)
donc 1 x fac(0) = 1
2 x fac(1) = 2 x 1
3 x fac(2) = 3x2 = 6 
etc...
'''

def factoriel(n):
    # n = 0 --> cas de base : return 1 sinon return n*fac(n-1)
    # une fonction est recursive si elle s'appelle elle meme
    # n doit etre un entier positif ou nul
    if n == 0:
        return 1
    elif n > 0:
        return n*factoriel(n-1)    
    else:
        return "Erreur n doit être positif ou nul"    

print(factoriel(5))        
print(factoriel(1))        
print(factoriel(-5))        
# -----------------
"""
puissance(4) = 4 x puissance(3)
puissance(3) = 3 x puissance(2)
etc...
puissance(1) = 1 x puissance(0)
puissance(0) = 1 (cas de base)
"""
def puissance (x,n):
    # calculer x exposent n 
    # relation de recurence --> x¨n = x*x¨n-1
    # il y a n multiplications donc la complexité est O(n) donc ** linéaire **
    if n == 0:
        return 1
    elif n>0:
        return x*puissance(x,n-1)    
    else:
        return "Erreur n doit être positif ou nul"    

print(puissance(5,4))        
print(puissance(5,0))        
print(puissance(0,4))        
print(puissance(6,-4))        

# Exercice 1
# calculer le reste de la division euclidienne revient à soustraire par le même nombre
# jusqu'a que l'on ne puisse plus
#sous(4) = 4 x sous(3)
#etc ...
# sous(1) = 1 x sous(0)
# sous(0) = retourner le resultat

def reste2(a,b:int)->int:
    if b == 0:
        return "Division par 0 impossible !"   
    elif a<b:
        return a
    else:
            return reste2(a-b,b)      

print(reste2(2,1))
print(reste2(10,5))
print(reste2(11,4))

# meme principe mais sans recursivite
def reste(a,b:int)->int:
    while a >= b:
        a = a - b
    return a

print(reste(2,1))
print(reste(10,5))
print(reste(11,4))

def quotient (a,b:int,q=0)->int:
    if b == 0:
        return "Division par 0 impossible !"   
    elif a<b:
        return q
    else:
        return quotient(a-b,b,q+1)     

print(quotient(45,8))     
print(quotient(66,8))           

# Exercice 2
# ex:17 en base 2 --> 17/2 = 8+1 --> 8/2 = 4+0 --> 4/2 = 2+0 --> 2/2 = 1+0 --> 1/2 = 0+1
# et on lit du bas le reste : 10001
def dec_binv1(a):
    chaine = ""
    while a>0:
        r = a%2
        chaine = str(r) + chaine
        a = a//2
    return chaine
print(dec_binv1(17))    
print(dec_binv1(8))

def dec_binv2(x):
    if x == 0:
        return ""
    else:
        return dec_binv2(x // 2) + str(x % 2)

print(dec_binv2(17))   # 10001
print(dec_binv2(8))    # 1000
print(dec_binv2(195))  # 11000011

# Exercice 3
#manière itérative
def est_palindrome(mot):
    liste = []
    for lettre in mot:
        liste.append(lettre)
    nv_liste = liste[::-1]
    if liste == nv_liste:
        return True
    else:
        return False    

print(est_palindrome('kayak'))
print(est_palindrome('tapat'))
print(est_palindrome('bonjour'))

# manière récursive
def est_palindrome_coorection(mot:str)->bool:
    if len(mot) == 1:
        return True
    elif mot[0] != mot[-1]:
        return False
    else:
        return est_palindrome_coorection(mot[1:len(mot)-1])        

print(est_palindrome_coorection('kayak'))        
print(est_palindrome_coorection('bonjour'))        
print(est_palindrome_coorection('aaaaaaaaaaaaaaa'))        

# Exercice 4
def nb_chiffres(chiffre:int)->int:
    if chiffre <10:
        return 1
    return nb_chiffres(chiffre//10) + 1

    
print(nb_chiffres(255555550))
print(nb_chiffres(255550))
print(nb_chiffres(2))

# Exercice 5 
def paysan_russe(a,b):
    if a > 0: #variant
        if a % 2 == 0:
            return paysan_russe(a//2,b*2)
        else:
            return paysan_russe(a-1,b) + b
    else:
        return 0    
    

print(paysan_russe(51,14))    
print(paysan_russe(12,5))
