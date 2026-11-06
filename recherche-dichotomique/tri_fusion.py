from timeit import *

def fusion(T1:list,T2:list):
    Tfinal=[]
    while len(T1)>0 and len(T2)>0:
        if T1[0]<T2[0]:
            Tfinal.append(T1.pop(0))
        else:
            Tfinal.append(T2.pop(0))
    Tfinal+=T1
    Tfinal+=T2
    return Tfinal

print(fusion([1,3,4,6,7,9],[2,5,8,10]))
