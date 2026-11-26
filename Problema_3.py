# Problema 3: Control de inventario

# Matriz con los datos de los articulos
# [Codigo, Nombre, Stock actual, Stock minimo]

inventario = [
    [101, "Teclado", 8, 10],
    [102, "Mouse", 15, 10],
    [103, "Monitor", 3, 5],
    [104, "Cable HDMI", 12, 8],
    [105, "Audifonos", 4, 7]
]


# Funcion para calcular la cantidad que se debe pedir
def calcular_cantidad(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad


# Mostrar los resultados del inventario
print("CONTROL DE INVENTARIO")
print("------------------------------")

# Recorrer la matriz de articulos
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_cantidad(stock_actual, stock_minimo)

    print("Codigo:", codigo)
    print("Articulo:", nombre)
    print("Cantidad a pedir:", cantidad_pedir)
    print("------------------------------")

print("Proceso finalizado.")