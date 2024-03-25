"""
La carrera de obstáculos
"""

#   Crea una función que evalúe si un/a atleta ha superado correctamente una
#   carrera de obstáculos.
#   - La función recibirá dos parámetros:
#        - Un array que sólo puede contener String con las palabras
#          "run" o "jump"
#        - Un String que represente la pista y sólo puede contener "_" (suelo)
#          o "|" (valla)
#   - La función imprimirá cómo ha finalizado la carrera:
#        - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
#          será correcto y no variará el símbolo de esa parte de la pista.
#        - Si hace "jump" en "_" (suelo), se variará la pista por "x".
#        - Si hace "run" en "|" (valla), se variará la pista por "/".
#   - La función retornará un Boolean que indique si ha superado la carrera.
#   Para ello tiene que realizar la opción correcta en cada tramo de la pista.


def carrera_de_obstaculos(carrera, pista):
    """ Función que evalúa si un/a atleta ha superado correctamente una carrera de obstáculos """
    # Ejemplo de carrera
    # carrera = ["run", "jump", "run", "jump", "run", "jump"]
    # Ejemplo de pista
    # pista = "_|_|_|"
    # Resultado esperado
    # pista = "_|_|_|"
    # return True

    # Recorrer la carrera
    for i in range(len(carrera)):
        # Si el atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
        if carrera[i] == "run" and pista[i] == "_":
            continue
        elif carrera[i] == "jump" and pista[i] == "|":
            continue
        elif carrera[i] == "jump" and pista[i] == "_":
            pista = pista[:i] + "x" + pista[i+1:]
        elif carrera[i] == "run" and pista[i] == "|":
            pista = pista[:i] + "/" + pista[i+1:]

    print(pista)
    return True


def main():
    """ Función principal """
    print('Carrera de obstáculos')
    carrera = ["run", "run", "run", "jump", "run", "jump"]
    pista = "_|_|_|"
    carrera_de_obstaculos(carrera, pista)


if __name__ == "__main__":
    main()
