# Imagen simulada como una matriz de píxeles
imagen = [
    [255, 0, 0],
    [0, 255, 0],
    [0, 0, 255],
    [255, 255, 0],
    [0, 255, 255],
    [255, 0, 255],
    [192, 192, 192],
    [128, 128, 128],
    [0, 0, 0],
]

# Color que queremos buscar (verde)
color_objetivo = [0, 255, 0]
contador = 0

# Recorrer la matriz para contar los píxeles del color objetivo
for fila in imagen:
    for pixel in fila:
        if pixel == color_objetivo:
            contador += 1
print(f"Cantidad de píxeles del color {color_objetivo}: {contador}")
