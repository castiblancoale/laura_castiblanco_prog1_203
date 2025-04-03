#Sumar posiciones pares e impares (por separado)
import random
cantidad = random.randint(5, 15)
vector = []
for i in range(cantidad):
    num = random.randint(1, 100)
    vector.append(num)

print(vector)
sum1 = 0
sum2= 0
for i in range(len(vector)):
    if i%2==0:
        sum1=sum1+vector[i]
    else:
        sum2=sum2+vector[i]
print(sum1)
print(sum2)