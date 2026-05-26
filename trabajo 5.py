# Problema 3: Auditoría de inventario y cálculo de reabastecimiento

# Función para calcular la cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

# Lista para guardar el inventario
inventario = []

# Pedir datos de 5 artículos
for i in range(5):
    print("\nArtículo", i + 1)

    codigo = input("Ingrese el código del artículo: ")
    nombre = input("Ingrese el nombre del artículo: ")
    stock_actual = int(input("Ingrese el stock actual: "))
    stock_minimo = int(input("Ingrese el stock mínimo: "))

    inventario.append([codigo, nombre, stock_actual, stock_minimo])

# Mostrar resultados
print("\n===================================")
print("      LISTA DE REABASTECIMIENTO")
print("===================================")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    print("\nArtículo:", nombre)
    print("Código:", codigo)
    print("Cantidad a pedir:", cantidad_pedir)