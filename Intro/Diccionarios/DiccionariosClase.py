#persona={"nombre":"angela martinez", "documento":1234567, "correo":"amartinez@gmil.com","clases":["programacion","algebra","estadistica"],"ubicacion":{"municipio":"soacha","barrio":"san mateo"}}

#print(type(persona))
#print(persona)
#print(persona["ubicacion"])
#print(persona["documento"])
#persona["promedio"]=3.5
#print(persona)
#persona.clear()
#x=persona.copy()
#claves=("universidad""programa")
#valores=none
#academia=dict.fromkeys(claves,valores)
#print(academia)
#print(persona.keys())
#print(persona.values())
#print(persona.items())
#for key in persona.keys():
#    print(key)
#for val in persona.values():
#    print(val)
#for item in persona.items():
#    print(item)


animales={"gato":"cat","perro":"dog","vaca":"cow","conejo":"rabbit","cocodrilo":"cocodrile","serpiente":"snake","raton":"mouse","pajaro":"bird","rana":"frog","caballo":"horse",}

palabra=(input("ingrese el animal que desea traducir"))
if palabra in animales.keys():
    print(animales[palabra])

for key,value in animales.items():
   if palabra==value:
       print(key)
