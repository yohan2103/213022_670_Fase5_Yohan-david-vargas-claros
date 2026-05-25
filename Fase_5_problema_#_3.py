
# Función que calcula cuántas unidades se deben pedir
def calcular_pedido(actual, minimo):
    if actual < minimo: 
        return minimo - actual
    return 0


# Matriz de inventario
inventario = [
    ["001", "Arroz", 10, 20],
    ["002", "Azúcar", 25, 20],
    ["003", "Aceite", 5, 15],
    ["004", "Sal", 30, 25],
    ["005", "Harina", 8, 12]
]

print("LISTA DE PEDIDOS")

for articulo in inventario: 
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    pedido = calcular_pedido(stock_actual, stock_minimo)

    print( codigo, nombre, "-> Cantidad a pedir:", pedido)
