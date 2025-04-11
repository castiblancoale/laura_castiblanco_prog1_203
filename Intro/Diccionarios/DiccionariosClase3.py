vendedores=[
{
'nombre':'Maria Lopez',
'area':'cosmeticos',
'lider':'Jose Perez',
'productos':['shampoo', 'jabón', 'bloqueador','crema dental','gel'],
'precio':[20000,10000,25000,12000,30000]
},

{"nombre":"Laura Castiblanco","area":"cosmeticos","lider":"Alejandra","productos":["Labial","rubor","polvos","base","iluminador"], "precio":[10000,15000,20000,25000,30000]},
{"nombre":"Laura Castiblanco","area":"Perecederos","lider":"Alejandra","productos":["uvas","manzanas","bananos","carne","pollo"], "precio":[8000,1500,2000,25000,11000]},
{"nombre":"Laura Castiblanco","area":"cosmeticos","lider":"Alejandra","productos":["pestañina","corrector","delineador","lapiz de labios","brochas"], "precio":[17000,15000,10000,2500,32000]},
{"nombre":"Laura Castiblanco","area":"no perecederos","lider":"Alejandra","productos":["miel","atun","sopas","maiz enlatado","cafe"], "precio":[5000,9000,6000,2500,10000]},
{"nombre":"Laura Castiblanco","area":"congelados","lider":"Alejandra","productos":["huevos","queso","hierbas","hongos","pescado"], "precio":[12000,12000,2000,2500,30000]},

{
    "nombre": "Jhonatan",
    "area": "cosmeticos",
    "lider": "Ducuara",
    "productos": ["sombras", "esmalte", "crema facial", "serum", "toallitas desmaquillantes"],
    "precio": [18000, 7000, 25000, 30000, 12000]
},

{
    "nombre": "Jhonatan",
    "area": "Perecederos",
    "lider": "Ducuara",
    "productos": ["lechuga", "tomate", "pera", "res", "cerdo"],
    "precio": [3000, 3500, 2500, 27000, 21000]
},

 {
    "nombre": "Jhonatan",
    "area": "cosmeticos",
    "lider": "Ducuara",
    "productos": ["brillo labial", "mascarilla facial", "tinte de cejas", "crema antiarrugas", "kit de maquillaje"],
    "precio": [8500, 22000, 15000, 27000, 45000]
},

 {
    "nombre": "Jhonatan",
    "area": "no perecederos",
    "lider": "Ducuara",
    "productos": ["arroz", "lentejas", "harina", "aceite", "azúcar"],
    "precio": [5000, 4000, 3500, 12000, 4500]
},
{
    "nombre": "Jhonatan",
    "area": "congelados",
    "lider": "Ducuara",
    "productos": ["nuggets", "vegetales mixtos", "helado", "empanadas", "filete de merluza"],
    "precio": [11000, 8000, 9500, 6000, 28000]
    }
]
#print(vendedores)

#for v in vendedores:
    #print(v["nombre"])
    #print(v["productos"])
    # #print(v["-"*50)
    # for key in v.keys():
    #     if v[key]=="cosmeticos":
    #         print(["nombre"])
    #         print(["productos"])

#Calcular el promedio de precios de cada vendedor
# for v in vendedores:
#     for key in v.keys():
#         if key=="precio":
#             suma=0
#             for x in v["precio"]:
#                 suma+=x
#     promedio=suma/len(v["precio"])
#     print(v["nombre"])
#     print(f"la suma es: {suma}")
#     print(f"el promedio es: {promedio}")


#Mostrar el vendedor que vende el producto mas costoso (de todos los productos) y decir cual es el producto y el vendedor
mayores=[]
for v in vendedores:
    for key in v.keys():
        if key=="precio":
            num=0
            for x in v["precio"]:
                if x>num:
                    num=x
            mayores.append(num)

print(f"el mayor es{max(mayores)}")    
print(v["nombre"])