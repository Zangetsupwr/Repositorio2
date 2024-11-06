#Python es un lenguaje de programacion interpretado es decir no necesitas compilar tu codigo
#Python es un lenguaje que no es fuertemente tipado es decir que no es necesarios declarar el tipo de variable que se va a utlizar
# Es una lenguaje de programacion orientado a objetos
# No se necesita de llaves para definir bloques de codigo , em su lugar utliza indentacion

nombre ="Mirsson"
edad =32 
estatura =1.80
graduado =True
motocicleta = False
grupo_sanguinario= 'A'

"Listas"
grupos_musicales =['Metallica','Pink Floyd','Led Zeppelin']

"Apuntes Python"  
#Listas: Tipo de datos mutable (que puede cambiar) y contiene un conjunto de distintos valores. Suele utilizarse para almacenar información relacionada.
lista_vacia = []

gatos = ["Garfield", "Silvestre", "Hello Kitty"]

print(gatos[2]) #Imprime: Silvestre

gatos[1] = "Tom"

gatos.append("Felix")

print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty', 'Felix']

gatos.pop()

print(gatos) #Imprime: ['Garfield', 'Tom', 'Hello Kitty']

gatos.pop(1)

print(gatos) #Imprime: ['Garfield', 'Hello Kitty']

#Tuplas: Tipo de datos inmutable (que no se puede modificar) y contiene un conjunto de distintos valores. Pueden contener distintos tipos de datos.
perro = ("Scooby Doo", "Gran Danés", "Scooby Galletas", 7)

print(perro[0]) #Imprime: Scooby Doo

perro[2] = "comida de perro" #ERROR: Las tuplas no pueden ser modificadas (TypeError: 'tuple' object does not support item assignment)


#Diccionarios: Nos permite almacenar contenido a través de una llave y un valor. Podemos acceder a sus datos a través de su índice único (que en este caso llamaremos llave o clave). 
diccionario_vacio = {}

persona = {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False}

persona['nombre'] = 'Valeria'  # Actualiza si el valor de la llave existente

persona['hobbies'] = ['jugar videojuegos', 'programación'] 

# Agrega esa clave-valor si no existía previamente

print(persona)

# Imprime: {'nombre': 'Carmen', 'edad': 31, 'altura': 1.71, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']}

altura = persona.pop('altura')  # Elimina la clave indicada y devuelve el valor

print(altura)    # Imprime: 1.71

print(persona) 

# salida: {'nombre': 'Carmen', 'edad': 31, 'usa_lentes': False, 'hobbies': ['jugar videojuegos', 'programación']} 