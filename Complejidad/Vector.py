# Manipulación de un vector de caracteristicas

"""Problema: Crear un arreglo en python que represente un vector de caracteristicas de un objeto (por ejemplo, altura, peso, edad)
Objetivo: Permite al usuario acceder a un elemento especifico por su indice, modificar su valor y calcular la media de todos los elementos"""

persona = [1.75, 70, 25]

print("Altura:", persona[0], "\nPeso:", persona[1], "\nEdad:", persona[2])

# Modificación de un valor (ejemplo: cambiar peso)

persona[1] = 72
print("Peso modificado:", persona[1])

# Calcular la media de los elementos

media = sum(persona) / len(persona)
print("Media:", media)
