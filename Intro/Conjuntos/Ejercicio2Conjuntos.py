#Genere dos conjuntos de números entre 1 y 20 (generados aleatoriamente), Cada conjunto debe tener entre 15 y 20 elementos. Desarrolle todas las operaciones entre conjuntos.

import random
can=random.randint(15,20)
Andy={can}
Laura={can}
can=random.randint(15,20)
for i in range (can):
    num=random.randint(1,20)
    Andy.add(num)
    can=random.randint(15,20)
for i in range (can):
    num=random.randint(1,20)
    Laura.add(num)
tam=random.randint(15,20)
for i in range (tam):
    num=random.randint(1,20)
    Andy.add(num)
tam=random.randint(15,20)
for i in range (tam):
    num=random.randint(1,20)
    Laura.add(num)

print(f"el conjunto uno es:{Andy}")
print(f"el conjunto dos es:{Laura}")

union=Andy|Laura
print(f"la union de los conjuntos es:{union}")
 
inter=Andy&Laura
print(f"la interseccion de los conjuntos es:{inter}")

diferencia=Andy-Laura
print(f"la diferencia entre los conjuntos es:{diferencia}")

difsimetrica=Andy^Laura
print(f"la difsimetrica entre los conjuntos es:{difsimetrica}")