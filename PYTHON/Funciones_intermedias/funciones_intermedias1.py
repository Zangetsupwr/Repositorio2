matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [

{"nombre": "Ricky Martin", "pais": "Puerto Rico"},

{"nombre": "Chayanne", "pais": "Puerto Rico"}

]

ciudades = {

"México": ["Ciudad de México", "Guadalajara", "Cancún"],

"Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

coordenadas = [

{"latitud": 8.2588997, "longitud": -84.9399704}

]

#Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz = [[10, 15, 20], [3, 7, 14]]
matriz[1][0] = 6  # Cambia el valor 3 a 6
print(matriz) 

#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes[0]["nombre"]="Enrique Martin Morales"
print(cantantes)

#En ciudades, cambia “Cancún” por “Monterrey”
ciudades["Mexico"[1]] = "Monterrey"
print(ciudades)

#En coordenadas, cambia el valor de latitud por 9.9355431
coordenadas[0]["latitud"]=9.9355431
print(coordenadas)


#-----------------------------------------------
cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]

#Ietracion de cantantes e imprima cada llave de la lista
for cantante in cantantes:
   print("Nombre:",cantante["nombre"] ,"- Pais:",cantante["pais"])

#Crea la función iterarDiccionario2(llave, lista) que reciba una cadena con el nombre de una llave y una lista de diccionarios.
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])
print(iterarDiccionario2("nombre", cantantes)) 
print(iterarDiccionario2("pais", cantantes))


costa_rica = {

   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],

   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]

}

#Crea una función imprimirInformacion(diccionario) que reciba un diccionario en donde los valores son listas. 
#La función debe imprimir el nombre de cada clave junto con el tamaño de su lista y seguido de esto los valores de la lista para esa clave.

    
def imprimirInformacion(diccionario):
    for clave in diccionario:
        print(clave, ":", len(diccionario[clave]))
        for valor in diccionario[clave]:
            print(valor)

imprimirInformacion(costa_rica) 

#crea una función que reciba una lista de números y regresa la sumatoria de estos menos la longitud de la lista.
#Ejemplo: sumatoria_menos_longitud([1, 2, 3, 4]) debe devolver 6 (sumatoria de números: 10 – longitud: 4)
def sumatoria_menos_longitud(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma - len(lista)
print(sumatoria_menos_longitud([1, 2, 3, 4]))



# escribe una función que reciba una lista y crea una nueva lista con todos los valores multiplicados por el segundo número. 
# Imprime la longitud de la lista y regresa la nueva lista. Si la lista tiene menos de 2 elementos, 
# haz que la función regrese una lista vacía.

def multiplica_por_segundo(lista):
    if len(lista) < 2:
        return []
    nuevo_lista = [x * lista[1] for x in lista]
    print(len(nuevo_lista))
    return nuevo_lista
print(multiplica_por_segundo([1, 3, 5, 7]))