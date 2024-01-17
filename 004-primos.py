# /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

def es_primo(n):

    divisores = 0

    for i in range(n):
        if n % (i+1) == 0:
            divisores += 1

    return divisores == 2


for i in range(100):
    if es_primo(i+1):
        print(str(i+1) + " es primo")
