#7-Cuantos y cuales son primos
import random
def crearvector():
    n = random.randint(5, 15)
    return [random.randint(1, 100) for i in range(n)] 
def primo(num):
    for i in range(2, num): 
        if num % i == 0: 
            return
    return num
def comparacion():
    vec1 = crearvector()
    vec2 = crearvector()
    
    pvec1 = [num for num in vec1 if primo(num)]
    pvec2 = [num for num in vec2 if primo(num)]
    print(vec1)
    print("Primos", pvec1)
    print("Cantidad de # primos v1", len(pvec1))
    
    print(vec2)
    print("Primos", pvec2)
    print("Cantidad de # primos v2", len(pvec2))
comparacion()