#2. Llenar dos arreglos de n elementos con números generados con la función random. Compararlos y decir:a. Cuál de los dos tiene la suma más alta
import random
def crearvector():
    n = random.randint(5, 15)
    return [random.randint(1, 100) for i in range(n)]
def comparacion():
    vec1 = crearvector()
    vec2 = crearvector()
    sum1 = 0
    for num in vec1:
        sum1 += num
    sum2 = 0
    for num in vec2:
        sum2 += num
    print(vec1)
    print(vec2)
    print("suma1", sum1)
    print("suma2", sum2)
    if sum1 > sum2:
        print("el vector 1 tiene la suma mas alta")
    elif sum2 > sum1:
        print("el vector 2 tiene la suma mas alta")
comparacion()