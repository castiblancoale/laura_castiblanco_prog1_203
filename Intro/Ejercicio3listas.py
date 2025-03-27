#b. Cuál de los dos tiene el número mayorimport random
import random
def crearvector():
    n = random.randint(5, 15) 
    return [random.randint(1, 100) for i in range(n)]
def comparacion():
    vec1 = crearvector() 
    vec2 = crearvector()  
    mvec1 = 0
    for num in vec1:
        if num > mvec1:
            mvec1 = num 
    mvec2 = 0 
    for num in vec2:
        if num > mvec2:
            mvec2 = num 
    print(vec1)
    print("numero mayor vec1", mvec1)
    
    print(vec2)
    print("numero mayor vec2", mvec2)
    if mvec1 > mvec2:
        print("el # mas grande esta en el vector1", mvec1)
    elif mvec2 > mvec1:
        print("el # mas grande esta en el vector2", mvec2)
comparacion()