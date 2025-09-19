# Sistema de recomendación de películas con matrices

# Definir matriz de calificaciones (usuarios x películas)
# 5 usuarios y 4 películas (ejemplo)
calificaciones = [
    [5, 4, 3, 2],  # Usuario 1
    [3, 5, 4, 1],  # Usuario 2
    [4, 4, 5, 3],  # Usuario 3
    [2, 3, 2, 4],  # Usuario 4
    [5, 5, 4, 5],  # Usuario 5
]

# 1. Imprimir matriz completa
print("Matriz de calificaciones (usuarios x películas):")
for fila in calificaciones:
    print(fila)

# 2. Calcular promedio de una película específica
pelicula = int(input("\nElige el número de película (0 a 3): "))
suma = 0
for usuario in range(len(calificaciones)):
    suma += calificaciones[usuario][pelicula]

promedio = suma / len(calificaciones)
print(f"Promedio de la película {pelicula}: {promedio:.2f}")

# 3. Mostrar calificaciones de un usuario en particular
usuario = int(input("\nElige el número de usuario (0 a 4): "))
print(f"Calificaciones del usuario {usuario}: {calificaciones[usuario]}")
