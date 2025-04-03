#d. Cuál es el promedio conjunto (uniendo los dos arreglos
import random
def crearvector():
    n = random.randint(5, 15)
    return [random.randint(1, 100) for i in range(n)]
def comparacion():
    vec1 = crearvector() 
    vec2 = crearvector() 
    sum1 = vec1 + vec2 
    sum2= 0
    for num in sum1:
        sum2=sum2+num 
    cantidad= len(sum1)
    promedio = sum2/ cantidad
    print(vec1)
    print(vec2)
    print("promedio de vectores", promedio)
comparacion()