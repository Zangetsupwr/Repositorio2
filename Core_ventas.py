import numpy as np 

# Genera datos de ventas aleatorias para el número de productos, tiendas y días especificados
def generar_datos_ventas(productos, tiendas, dias):
    return np.random.randint(0, 101, (productos, tiendas, dias))

#Calcular el total de de las ventas por producto a lo largo de la semana 
def calcular_totales_ventas_semana(datos):
    return np.sum(datos, axis=2)  # Suma las ventas de cada producto a lo largo de la semana.
productos, tiendas, dias = 5, 3, 7  # 5 productos, 3 tiendas, 7 días (semanal)
datos_ventas = np.random.randint(0, 101, (productos, tiendas, dias))
totales_por_producto = calcular_totales_ventas_semana(datos_ventas)
print("Total de ventas de producto semanal:",totales_por_producto) 

# Calcula el total de ventas por tienda a lo largo de la semana 
def calcular_totales_ventas_tienda(datos):
    return np.sum(datos, axis=1)  # Suma las ventas de cada tienda a lo largo de la semana.
tiendas, dias = 3, 7  # 3 tiendas, 7 días (semanal)
datos_ventas = np.random.randint(0, 101, (productos, tiendas, dias))
totales_por_tienda = calcular_totales_ventas_tienda(datos_ventas)
print("Total de ventas por tienda a lo largo de la semana:", totales_por_tienda) 

 # Calcula el promedio de ventas por producto por día
def calcular_promedio_ventas_por_producto(datos):
     return np.mean(datos, axis=2)  # Calcula el promedio de ventas por producto por día.
productos, tiendas, dias = 5, 3, 7  # 5 productos, 3 tiendas, 7 días (semanal)
datos_ventas = np.random.randint(0, 101, (productos, tiendas, dias))
promedio_por_producto = calcular_promedio_ventas_por_producto(datos_ventas)
print("Promedio de ventas por producto :",promedio_por_producto)


 # Encuentra el producto con mayor y menor ventas totales en la semana
def encontrar_productos_mayor_y_menor_venta(datos):
    # Sumar todas las ventas por producto durante la semana
    ventas_totales = np.sum(datos, axis=(1, 2))
    # Encontrar índices del producto con mayor y menor ventas
    indice_max = np.argmax(ventas_totales)  # Producto con más ventas
    indice_min = np.argmin(ventas_totales)  # Producto con menos ventas
    return indice_max, ventas_totales[indice_max], indice_min, ventas_totales[indice_min]
productos, tiendas, dias = 5, 3, 7  # 5 productos, 3 tiendas, 7 días
datos_ventas = np.random.randint(0, 101, (productos, tiendas, dias))
indice_max, ventas_max, indice_min, ventas_min = encontrar_productos_mayor_y_menor_venta(datos_ventas)
print(f"Producto con más ventas: {indice_max} ({ventas_max} unidades)")
print(f"Producto con menos ventas: {indice_min} ({ventas_min} unidades)")

# Encuentra la tienda con mayor y menor ventas totales en la semana

def encontrar_tiendas_mayor_y_menor_venta(datos):
    import numpy as np
    # Sumar todas las ventas por tienda durante la semana
    ventas_totales = np.sum(datos, axis=(0, 2))
    # Encontrar índices de la tienda con mayor y menor ventas
    indice_max = np.argmax(ventas_totales)  # Tienda con más ventas
    indice_min = np.argmin(ventas_totales)  # Tienda con menos ventas
    return indice_max, ventas_totales[indice_max], indice_min, ventas_totales[indice_min]
productos, tiendas, dias = 5, 3, 7  # 5 productos, 3 tiendas, 7 días
datos_ventas = np.random.randint(0, 101, (productos, tiendas, dias))
indice_max, ventas_max, indice_min, ventas_min = encontrar_tiendas_mayor_y_menor_venta(datos_ventas)
print(f"Tienda con más ventas: {indice_max} ({ventas_max} unidades)")
print(f"Tienda con menos ventas: {indice_min} ({ventas_min} unidades)")
