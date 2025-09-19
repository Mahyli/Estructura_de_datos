# Entenamiento de una red neuronal
import time as time

entrada = [1, 2]

# Matriz pesos 3 x 2
#
pesos = [
    [4, 1, 5, 6],
    [4, 1, 5, 6],
    [3, 1, 1, 6],
]

salida = [0, 0, 0, 0]

start_time = time.time()
end_time = time.time()


for j in range(len(pesos[0])):
    for i in range(len(entrada)):
        salida[j] += entrada[i] * pesos[i][j]

print("Inicio:", start_time)
print("Tiempos :", end_time - start_time)
print("Matriz Entrada", entrada)
print("Matriz Pesos", pesos)
print("Matriz Salida", salida)
