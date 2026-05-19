
# Función que calcula cuántas unidades se deben pedir
def calcular_pedido(actual, minimo):
    if actual < minimo:
        return minimo - actual
    return 0


# Matriz de inventario
inventario = [
    ["Arroz", 10, 20],
    ["Azúcar", 25, 20],
    ["Aceite", 5, 15],
    ["Sal", 30, 25],
    ["Harina", 8, 12]
]

print("LISTA DE PEDIDOS")

for articulo in inventario:
    nombre = articulo[0]
    stock_actual = articulo[1]
    stock_minimo = articulo[2]

    pedido = calcular_pedido(stock_actual, stock_minimo)

    print(nombre, "-> Cantidad a pedir:", pedido)
