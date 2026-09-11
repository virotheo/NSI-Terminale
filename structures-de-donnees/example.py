from file_2026 import *
from pile_2026 import * 

mafile = creeFile()

fileEnfiler(mafile, 'a')
fileEnfiler(mafile, 'b')
fileEnfiler(mafile, 'c')
fileEnfiler(mafile, 'd')

def fileInverser(F):
    pile_inverser = creePile()
    while not fileEstVide(F):
        element = fileDefiler(F)
        pileEmpiler(pile_inverser, element)
    while not pileEstVide(pile_inverser):
        element2 = pileDepiler(pile_inverser)
        fileEnfiler(F, element2) 
    return F    

print(fileInverser(mafile))



test = creePile()
pileEmpiler(test, '(')
pileEmpiler(test, '(')
pileEmpiler(test, '(')
pileEmpiler(test, 'a')
pileEmpiler(test, 'b')
pileEmpiler(test, ')')
pileEmpiler(test, ')')
pileEmpiler(test, ')')

test2 = creePile()
pileEmpiler(test2, '(')
pileEmpiler(test2, '(')
pileEmpiler(test2, '(')
pileEmpiler(test2, 'a')
pileEmpiler(test2, 'b')
pileEmpiler(test2, ')')
pileEmpiler(test2, ')')
pileEmpiler(test2, ')')
pileEmpiler(test2, '(')
pileEmpiler(test2, 'a')
pileEmpiler(test2, 'b')
pileEmpiler(test2, ')')


def bien_parenthese(mot):
    P = creePile()
    for c in mot:
        if c == '(':
            pileEmpiler(P, c)
        elif c == ')':
            if pileEstVide(P):
                return False
            else:    
                pileDepiler(P)
    return pileEstVide(P)            

print(bien_parenthese(test))    
print(bien_parenthese(test2))    

# Exercice 2
'''
calcul d'expression numérique postfixée / notation polobaise inversée
73-2*8+
42*8+
88+
16

7 8 4 + * 7 2 + -
7 12 * 7 2 + - 
84 7 2 + -
84 9 -
75


5 2 + 3 * 4 + 2 *
7 3 * 4 + 2 *
21 4 + 2 * 
25 2 *
50
'''

def calcul_postfixe(calc):
    M = creePile()
    numbers = []
    for n in range (101): 
        numbers.append(n)
    signes = ["+","/","*","-"]
    for i in calc:
        if i in numbers:
            pileEmpiler(M, i)
        elif i in signes:
            un = pileDepiler(M)
            deux = pileDepiler(M)
            if i == '+':
                resultat = un + deux
            elif i == '*':
                resultat = un * deux
            elif i == '-':
                resultat = deux - un
            elif i == '/':
                resultat = deux / un    
            pileEmpiler(M, resultat)    
    return pileDepiler(M)

print(calcul_postfixe([2,3,'*']))
print(calcul_postfixe([45,75,'*',45,'/',100,'+',100,'-']))
print(calcul_postfixe([5,2,'+',3,'*',4,'+',2,'*']))

def calcul_postfixe_correction(calc2:list)->float:
    L = creePile()
    for x in calc2:
        if x not in ['+','-','*','/']:
            pileEmpiler(L,x)
        else:
            y = pileDepiler(L)
            z = pileDepiler(L)
            if x == '+':
                pileEmpiler(L,y+z)    
            elif x == '*':
                pileEmpiler(L,y*z)    
            elif x == '-':
                pileEmpiler(L,z-y)    
            else:
                pileEmpiler(L,z//y)          
    return pileDepiler(L)            

print(calcul_postfixe_correction([5,2,'+',3,'*',4,'+',2,'*']))
