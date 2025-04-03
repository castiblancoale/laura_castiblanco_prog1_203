#Cómo puede bienestar estudiantil utilizar conjuntos de Python para la gestión de grupos en la Universidad de Cundinamarca. Escriba el enunciado de todas las posibilidades y desarrolle los ejercicios en python

danzas={"Ana", "Luis", "Carlos", "María", "Pedro", "Ana", "Lucía", "Juan","Sofía","Andy","Esteban","Laura","Camila","Johnatan","Nicolas"}
deporte={"Juana", "Luis", "Camilo", "María", "Pablo", "Alicia", "Lucía", "Boris","Sofía","Andy","Esteban","Camila","Johnatan","Camilo"}
print(f"el grupo de danzas es:{danzas}")
print(f"el grupo de deportes es:{deporte}")
union=danzas|deporte
print(f"Union de los grupos danza y deporte es:{union}")
inter=danzas&deporte
print(f"la interseccion de los grupos danza y deporte es:{inter}")
diferencia=danzas-deporte
print(f"la diferencia entre los grupos danza y deporte es:{diferencia}")
diferencia2=deporte-danzas
print(f"la diferencia entre los grupos deporte y danza es:{diferencia2}")
difsimetrica=danzas^deporte
print(f"la difsimetrica entre los grupos danza y deporte es:{difsimetrica}")