" imprime todos los números enteros del 0 al 100." 
for i in range (0,101):
    print(i)

"imprime todos los números múltiplos de 2 entre 2 y 500"
for i in range(2,501,2):
    print(i)

    "imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, imprime “baby”"
    for i in range (1,101):
        if (i % 5 == 0): 
            print("ice-ice")
    else: (i % 10 == 0)
    print("baby")

    "suma los números pares del 0 al 500,000 e imprime la suma total. (Sorpresa, será un número gigante)."
    suma = 0
    for i in range (0,50001):
        if (i % 2 == 0):
            suma += i
    print(suma)

    "imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3."
    for numero in range (2024,0,-3):
        print("cuenta regresiva: ",numero)

    "establece tres variables: numInicial, numFinal y multiplo. Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo." 
    "Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas)."    
    
    numInicial = 2
    numFinal =12
    multiplo = 3
    for i in range (numInicial,numFinal + 1):
         if i % multiplo == 0:
          print(i)