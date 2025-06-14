#"Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta. Cada venta debe incluir las siguientes claves:
#«fecha»: una cadena de texto que represente la fecha de la venta (por ejemplo, «2024-01-01»).
#«producto»: una cadena de texto que represente el nombre del producto vendido.
#«cantidad»: un número entero que represente la cantidad de productos vendidos.
#«precio»: un número flotante que represente el precio unitario del producto.
#«total»: un número flotante que represente el total de la venta (cantidad * precio).

import pandas as pd # Importar librería pandas 


ventas = [
    {"fecha": "2026-01-01", "producto": "Laptop", "cantidad": 2, "precio": 999.99},
    {"fecha": "2023-01-03", "producto": "Mouse inalámbrico", "cantidad": 5, "precio": 25.50},
    {"fecha": "2025-01-05", "producto": "Monitor 24 pulgadas", "cantidad": 1, "precio": 189.99},
    {"fecha": "2025-01-07", "producto": "Teclado mecánico", "cantidad": 3, "precio": 75.00},
    {"fecha": "2026-01-10", "producto": "Disco duro externo 1TB", "cantidad": 4, "precio": 59.95},
]

# Calcular ingresos totales
ingresos_totales = sum(venta["cantidad"] * venta["precio"] for venta in ventas)
print(f"Ingresos totales: ${ingresos_totales:.2f}")

# Calcular ventas por producto
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    ventas_por_producto[producto] = ventas_por_producto.get(producto, 0) + cantidad

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

print("\nVentas por producto:")
for producto, cantidad in ventas_por_producto.items():
    print(f"{producto}: {cantidad} unidades")

print(f"\nProducto más vendido: {producto_mas_vendido} ({cantidad_mas_vendida} unidades)")

# Calcular precio promedio por producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    ingreso_total = venta["cantidad"] * venta["precio"]
    cantidad_total = venta["cantidad"]
    if producto in precios_por_producto:
        precios_por_producto[producto][0] += ingreso_total
        precios_por_producto[producto][1] += cantidad_total
    else:
        precios_por_producto[producto] = [ingreso_total, cantidad_total]

print("\nPrecio promedio por producto:")
for producto, (suma_total, cantidad_total) in precios_por_producto.items():
    precio_promedio = suma_total / cantidad_total
    print(f"{producto}: ${precio_promedio:.2f}")


# ingresos totales por dia 
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingresos = venta["cantidad"] * venta["precio"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingresos
    else:
        ingresos_por_dia[fecha] = ingresos

# Mostrar los ingresos totales por día
print("\nIngresos totales por día:")
for fecha, ingresos in ingresos_por_dia.items():
    print(f"{fecha}: ${ingresos:.2f}")
# Generar archivo Excel
ventas_df = pd.DataFrame(ventas)
ventas_df.to_excel('ventas.xlsx')