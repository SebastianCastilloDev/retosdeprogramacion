#   Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
#   y retorne lo siguiente:
#   - "X" si han ganado las "X"
#   - "O" si han ganado los "O"
#   - "Empate" si ha habido un empate
#   - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
#     O si han ganado los 2.
#   Nota: La matriz puede no estar totalmente cubierta.
#   Se podría representar con un vacío "", por ejemplo.


""" Función que analiza una matriz 3x3 compuesta por "X" y "O" """
# Ejemplo de matriz 1
# matriz = [
#     ["X", "O", "X"],
#     ["O", "X", "O"],
#     ["X", "", "X"]
# ]
# Resultado esperado
# return "X"

# Ejemplo de matriz 2
# matriz = [
#     ["0", "X", "0"],
#     ["X", "O", "X"],
#     ["O", "", "O"]
# ]
# Resultado esperado
# return "O"

# Ejemplo de matriz 3
# matriz = [
#     ["O", "X", "O"],
#     ["O", "X", "X"],
#     ["X", "", "O"]
# ]
# Resultado esperado
# return "Empate"


def tres_en_raya(matriz):
    """ Evaluar el gato """
    for i in range(len(matriz)):
        if matriz[i][0] == matriz[i][1] == matriz[i][2]:
            return matriz[i][0]
        if matriz[0][i] == matriz[1][i] == matriz[2][i]:
            return matriz[0][i]
    if matriz[0][0] == matriz[1][1] == matriz[2][2]:
        return matriz[0][0]
    if matriz[0][2] == matriz[1][1] == matriz[2][0]:
        return matriz[0][2]
    if "" not in matriz[0] and "" not in matriz[1] and "" not in matriz[2]:
        return "Empate"
    return "Nulo"


partida = [
    ["X", "O", "X"],
    ["O", "X", "O"],
    ["X", "", "X"]
]
print(tres_en_raya(partida))
