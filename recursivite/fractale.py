import turtle as t

# prise en mains de turtle
'''
t.hideturtle()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
'''
 # Q1
def Koch(n, a):
    if n==0: # cas de base
        t.forward(a)
        return
    else:
        Koch(n-1, a/3) 
        t.left(60)
        Koch(n-1,a/3)
        t.right(120)
        Koch(n-1,a/3)
        t.left(60)
        Koch(n-1,a/3)
#print(Koch(3,200))   

# Q2
t.up()
t.goto(-200,200)
t.speed('fastest')
t.width(2)
t.down()
def flocon(n,a):
    for i in range (4):
        Koch(n,a)
        t.right(90)

print(flocon(4,400))        
t.exitonclick()
t.mainloop()
