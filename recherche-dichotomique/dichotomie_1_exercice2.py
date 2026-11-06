from timeit import *


def simple_exp(x,p): # simple exponantial function
    res = 1
    for i in range(p):
        res = res * x
    return res    
print(simple_exp(2,16)) # Test
print('------------------------------------------')
def recursive_exp(x, p):
    if p == 0: # base
        return 1
    
    if p % 2 == 0: # testing parity
        res = recursive_exp(x, p // 2) # x**p = (x**(p/2))**2 
        return res * res
    
    else: # if p is odd
        return x * recursive_exp(x, p - 1) 

print(recursive_exp(2,16)) # Test

x=1.001
n=100000

temps_expRapideRec=timeit(lambda:recursive_exp(x,n),number=100)

temps_expRapideIter=timeit(lambda:simple_exp(x,n),number=100)
print('------------------------------------------')
print("Iterative time : \n")
print(temps_expRapideIter)
print('------------------------------------------')

print("Recursive time : \n")
print(temps_expRapideRec)
print('------------------------------------------')
