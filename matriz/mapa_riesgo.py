# Mapa de riesgo para la navegación de un vehículo autónomo

# Crear una matriz de 8x8
matriz = [
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1],
    [0, 1, 2, 1, 2, 0, 1, 1],
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
    print()

area_precaucion = 0  # 1
area_riesgo = 0  # 2

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == 1:
            area_precaucion += 1
        if matriz[i][j] == 2:
            area_riesgo += 1
    print()

print("Area de precaución (1): {area_precaucion}")
print("Area de riesgo(2): {area_riesgo}")

# Cambiar todos los 2 por 1
print("Actualización de matriz de navegación")

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz == 2:
            matriz[i][j] = 1
    print()

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end="")
    print()

area_precaucion_actualizda = 0
area_riesgo_actualizada = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz == 1:
            area_precaucion_actualizda += 1
            if matriz == 2:
                area_precaucion_actualizda += 1
    print()

print("Area de precaución (1): {areaprecaucion_actualizda}")
print("Area de riesgo(2): {area_riesgo_actualizada}")
