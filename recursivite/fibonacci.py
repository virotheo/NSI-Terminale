# la suite de fibonacci : u0 = 0 
# u1 = 0+1 = 1
# u2 = 1+1 = 2
# u3 = 1 + 2 = 3
# u4 = 2 + 3 = 5
# u5 = 3 + 5 = 8

def fibonacci(n:int)->int:
    if n <= 1:
        return 1    
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(1,11):
    print(f"{i} {fibonacci(i)}")
