#UNIVERSIDAD ESTATAL AMAZONICA
#WILLIAM DELGADO
#FUNDAMENTOS DE PROGRAMACION
#Programa 1: Búsqueda en Arreglo Multidimensional
matriz = [
    [4, 7, 2, 10],
    [1, 9, 6, 13],
    [8, 3, 5, 12],
    [14, 16, 15, 11]
]

VB = 15
encontrado = False

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == VB:
            print(f"Se encontró {VB} en la posición ({i}, {j}).")
            encontrado = True
            break
    if encontrado:
        break

if not encontrado:
    print(f"{VB} no se encontró en la matriz.")