animales={"gato":"cat","perro":"dog","vaca":"cow","conejo":"rabbit","cocodrilo":"cocodrile","serpiente":"snake","raton":"mouse","pajaro":"bird","rana":"frog","caballo":"horse",}

palabra1=(input("ingrese el animal que desea agragar en español"))
palabra2=(input("ingrese el animal que desea agragar en ingles"))
if palabra1 not in animales.keys():
   animales[palabra1]
# if palabra1 not in animales.values():
#    animales[palabra2]
print(animales)