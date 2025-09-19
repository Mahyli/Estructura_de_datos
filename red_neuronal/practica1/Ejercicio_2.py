# Matriz de productos: [ID, cantidad, precio]
inventario = [[101, 50, 20], [102, 30, 15], [103, 80, 10]]

# Imprimir inventario
print("Inventario:")
for producto in inventario:
    print(producto)

# Calcular valor total del segundo producto (índice 1)
cantidad = inventario[1][1]
precio = inventario[1][2]
valor_total = cantidad * precio
print(f"\nValor total del producto con ID {inventario[1][0]}: {valor_total}")

# Actualizar stock tras vender 10 unidades
inventario[1][1] -= 10
print(f"Nuevo stock del producto {inventario[1][0]}: {inventario[1][1]}")
