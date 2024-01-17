
# /*
#  * Crea un programa se encargue de transformar un número
#  * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
#  */

def decimal_a_binario(n):
    numero = n
    binario = ''

    while numero != 0:
        residuo = round(numero % 2)
        numero = round(numero/2)
        binario = str(residuo)+str(binario)
    return binario


print(decimal_a_binario(9))
