import numpy as np  # Importamos Numpy


def diagonal_difference(arr):
    # Suma de la diagonal principal
    diagonal_principal = np.trace(arr)

    # Suma de la diagonal secundaria (diagonal de la matriz invertida)
    diagonal_secundaria = np.trace(np.fliplr(arr))

    # Diferencia absoluta
    diferencia = abs(diagonal_principal - diagonal_secundaria)

    return diferencia


if __name__ == "__main__":
    matriz = np.array([[11, 2, 4], [4, 5, 6], [10, 8, -12]])

    resultado = diagonal_difference(matriz)
    print("La diferencia diagonal es:", resultado)
