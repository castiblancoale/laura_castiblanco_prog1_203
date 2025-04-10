#Crear 5 diccionarios
# vendedor={"nombre":"Maria Lopez","area":"cosmeticos","lider":"Jose Perez","productos":["Shampoo","jabon","bloqueador", "crema"], "precio":[20000,10000,25000,12000,30000]}

# vendedor={"nombre":"Laura Castiblanco","area":"cosmeticos","lider":"Alejandra","productos":["Labial","rubor","polvos","base","iluminador"], "precio":[10000,15000,20000,25000,30000]}
# vendedor={"nombre":"Laura Castiblanco","area":"Perecederos","lider":"Alejandra","productos":["uvas","manzanas","bananos","carne","pollo"], "precio":[8000,1500,2000,25000,11000]}
# vendedor={"nombre":"Laura Castiblanco","area":"cosmeticos","lider":"Alejandra","productos":["pestañina","corrector","delineador","lapiz de labios","brochas"], "precio":[17000,15000,10000,2500,32000]}
# vendedor={"nombre":"Laura Castiblanco","area":"no perecederos","lider":"Alejandra","productos":["miel","atun","sopas","maiz enlatado","cafe"], "precio":[5000,9000,6000,2500,10000]}
# vendedor={"nombre":"Laura Castiblanco","area":"congelados","lider":"Alejandra","productos":["huevos","queso","hierbas","hongos","pescado"], "precio":[12000,12000,2000,2500,30000]}

#inmdexacion y slicing
# lista=[10,30,20,50,5,7,11,21,31,100]
# print(lista[0])
# print(lista[5])
# print(lista[-1])
# print(lista[1:4])
# print(lista[0:5])
# print(lista[:5])
# print(lista[-1:-6:-1])
# print(lista[::2])
# print(lista[-2::-2])
# print(lista[-6:-1])
# print(lista[5:11])
# print(lista[5:])

#lenar una lista (tamaño 10 a 20 elementos) con numeros aleatoreos entre 1 y 100. cerciorese con codigo que el tamaño sea siempre par 
#usando slicing encuentre la suma y los promedios de las siguientes partes:
#Primera mitad
#segunda mitad
#posiciones pares
#posiciones impares


import random
cantidad = random.randint(10, 20)
if cantidad % 2 != 0:
    cantidad=cantidad+1
lista = [random.randint(1, 100) for i in range(cantidad)]
print(lista)
print(len(lista))

mitad1 = lista[:cantidad//2]
mitad2 = lista[cantidad//2:]
pares = lista[::2]
impares = lista[1::2]

suma1mitad = 0
for i in mitad1:
    suma1mitad=suma1mitad+i
    promedio1mitad=suma1mitad / len(mitad1)
print("primera mitad suma", suma1mitad, "promedio:",promedio1mitad)

suma2mitad = 0
for i in mitad2:
    suma2mitad=suma2mitad+ i
    promedio2mitad= suma2mitad / len(mitad2)
print("segunda mitad suma", suma2mitad, "promedio:",promedio2mitad)

sumpar = 0
for i in pares:
    sumpar=sumpar+i
    promediopar=sumpar / len(pares)
print("suma pares", sumpar, "promedio:", promediopar)

sumimpar = 0
for i in impares:
    sumimpar=sumimpar+i
    promedioimpar=sumimpar / len(impares)
print("suma impares", sumimpar, "promedio:", promedioimpar)