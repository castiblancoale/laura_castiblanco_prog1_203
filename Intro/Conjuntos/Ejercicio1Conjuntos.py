ingsof={"Algebra lineal","Pensamiento Algorítmico","Fundamentos de Electrónica","Fundamentos de Ingeniería","Matemáticas Discreta","Pensamiento sistemico y automatizacion","Razonamiento logico y cuantitativo","Cálculo Diferencial","programacion1","Física Mecánica","Estadística, Probabilidad e Inferencial","comunicacion y pensamiento critico","calculo integral","programacion2","Fisica optica y ondas","Ciudadania del siglo 21","Comunicacion y pensamiento critico2","lengua extrangera","Calculo multivariado","Programacion Web","Estructura de datos","requerimientos de software","Arquitectura de hardware y software","diseño y modelacion de bases de datos","lengua extrangera2","Ecuaciones Diferenciales","Desarrolo nativo para dispositivos moviles","Sistemas operativos","Interfaz hombre maquina","Seguridad informatica","Motores y gestores en bases de datos","lengua extrangera3"}
ingind={"Algebra lineal","Pensamiento Algorítmico","Fundamentos de Electrónica","Fundamentos de Ingeniería","Matemáticas Discreta","Pensamiento sistemico y automatizacion","Razonamiento logico y cuantitativo","Cálculo Diferencial","programacion1","Física Mecánica","Estadística, Probabilidad e Inferencial","comunicacion y pensamiento critico","calculo integral","programacion2","Fisica optica y ondas","Ciudadania del siglo 21","Comunicacion y pensamiento critico2","lengua extrangera","Calculo multivariado","Fisica electrividad y magnetismo","operaciones en ingenieria","prospectiva estrategica","ingenieria de metodos","lengua extrangera2","Ecuaciones Diferenciales","analisis de datos","fundamentos de economia","control y aseguramiento de calidad","planeacion y programacion de operaciones","lengua extrangera3",}

print(f"Materias de ingenieria software:{ingsof}")
print(f"Materias de ingenieria industrial:{ingind}")

union=ingsof|ingind
print(f"la union entre ingenieria industrial y ingenieria en software es:{union}")
 
inter=ingsof&ingind
print(f"la interseccion entre ingenieria industrial y ingenieria en software es:{inter}")

diferencia=ingsof-ingind
print(f"la diferencia entre ingenieria industrial y ingenieria en software es:{diferencia}")

difsimetrica=ingsof^ingind
print(f"la diferencia simetrica entre ingenieria industrial y ingenieria en software es:{difsimetrica}")
