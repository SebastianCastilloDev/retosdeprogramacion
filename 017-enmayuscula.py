# /*
#  * Crea una función que reciba un String de cualquier tipo y se encargue de
#  * poner en mayúscula la primera letra de cada palabra.
#  * - No se pueden utilizar operaciones del lenguaje que
#  *   lo resuelvan directamente.
#  */

string = "poner en mayúscula la primera letra de cada palabra"
nuevo_string = ""
# hacer strip por espacios
palabras = string.split(" ")
# recorrer array
for palabra in palabras:
    # buscar cada primer caracter
    primer_caracter = palabra[0]
    # si el primer caracter esta entre 99 y 122 en la tabla ascii
    if 99 <= ord(primer_caracter) <= 122:
        # almacenar los caracteres restantes en una variable
        caracteres_restantes = palabra[1:]
        # obtener el primer caracter en mayuscula = codigo_ascii - 32
        caracter_mayuscula = chr(ord(primer_caracter)-32)
        # concatenar la primera letra mayuscula a los caracteres restantes
        nueva_palabra = caracter_mayuscula + caracteres_restantes
        # Concatenar cada palabra
    else:
        nueva_palabra = palabra

    nuevo_string += nueva_palabra + " "

print(nuevo_string)
