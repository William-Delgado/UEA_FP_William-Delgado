# UNIVERSIDAD ESTATAL AMAZONICA
# WILLIAM DELGADO
# FUNDAMENTOS DE PROGRAMACION
# Programa 2: Ordenación de una Fila en una Matriz Bidimensional

# Función para ordenar una fila usando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])  # Longitud de la fila
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                # Intercambiar elementos si están desordenados
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Matriz bidimensional de 4x4
matriz = [
    [4, 7, 10, 2],
    [13, 9, 6, 1],
    [8, 3, 12, 5],
    [14, 16, 15, 11]
]

# Mostrar la matriz original
print("Matriz Original:")
for fila in matriz:
    print(fila)

# Ordenar la fila que se quiere
FO = 2  # Índice de la fila (0-based)
ordenar_fila(matriz, FO)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la Fila Ordenada:")
for fila in matriz:
    print(fila)