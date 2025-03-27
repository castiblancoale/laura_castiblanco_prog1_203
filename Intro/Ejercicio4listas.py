#c. Cuál de los dos tiene el número menor
import random
def crearvector():
    n = random.randint(5, 15) 
    return [random.randint(1, 100) for i in range(n)]
def comparacion():
    vec1 = crearvector() 
    vec2 = crearvector()  
    mvec1 = 0 
    for num in vec1:
        if mvec1 == 0:
            mvec1 = num 
        elif num < mvec1:
            mvec1 = num
    mvec2 = 0
    for num in vec2:
        if mvec2 == 0:
            mvec2 = num 
        elif num < mvec2: 
            mvec2 = num 
    print(vec1)
    print("numero menor en vec1:", mvec1)
    print(vec2)
    print("numero menor en vec2", mvec2)
    if mvec1 < mvec2:
        print("el # menor esta en v1", mvec1)
    elif mvec2 < mvec1:
        print("el # menor esta en v2", mvec2)
comparacion()