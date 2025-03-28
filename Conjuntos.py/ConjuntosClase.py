# x={1,2,3,4,5,6}
# print(type(x))
# print(x)

# lista=[10,20,30]
# y=set(lista)
# print(type(y))
# print(y)

# lista.append(100)
#1 instancia de una clase, se crea apartir de una clase
#No indexable con for in range 


# c1=set()
# c1.add(10)
# print(c1)
# c1.add(11)
# print(c1)
# lista=[9,8,7]
# tupla=(23,24,9,7,8)
# c2={55,56}
# c1.update(c2)
# print(c1)
# c1.update(lista)
# print(c1)
# c1.update(tupla)
# print(c1)
# for elemento in c1:
#     print(elemento)


# import random
# original=set()
# duplicados=set()
# tam=random.randint(5,15)
# for i in range (tam):
#     num=random.randint(1,20)
#     if num not in original:
#         original.add(num)
#     else:
#         duplicados.add(num)
# print(original)
# print(duplicados)

# c3={1,2,3,4,5,6,7,8,9,0}
# c3.pop(10)
# print(c3)
# print(c3.pop())
# print(c3)

#Operaciones entre conjuntos
#| pipe
#& ampersant
#-diferencia
#^circunflejo
# A={1,2,3,4,5,7,9}
# B={1,3,6,7,8,9,0}
# print(A)
# print(B)
# union=A|B
# print(union)
 
# inter=A&B
# print(inter)

# diferencia=A-B
# print(diferencia)

# difsimetrica=A^B
# print(difsimetrica)

# import random
# cantidad=random.randint(5,15)
# c1={cantidad}
# c2={cantidad}
# cantidad=random.randint(5,15)
# for i in range (cantidad):
#     num=random.randint(1,20)
#     c1.add(num)
# tamaño=random.randint(5,15)
# for i in range (tamaño):
#     num=random.randint(1,20)
#     c2.add(num)
# print(c1)
# print(c2)

# union=c1|c2
# print(f"la union es:{union}")
 
# inter=c1&c2
# print(f"la inter es:{inter}")

# diferencia=c1-c2
# print(f"la diferencia es:{diferencia}")

# difsimetrica=c1^c2
# print(f"la difsimetrica es:{difsimetrica}")

# print("subset1",diferencia.issubset(c1))
# print("subset2",diferencia.issubset(c2))

# print("superset1",union.issuperset(c1))
# print("superset1",union.issuperset(c2))

# #issubset: busca si es subconjunto del otro
# #issuperset: busca si contiene el otr conjunto 


ingsof={"Algebralineal","palgoritmico","felectronica","matematicasdiscretas"}
ingind={1,3,6,7,8,9,0}
print(ingsof)
print(ingind)
union=ingsof|ingind
print(union)
 
inter=ingsof&ingind
print(inter)

diferencia=ingsof-ingind
print(diferencia)

difsimetrica=ingsof^ingind
print(difsimetrica)