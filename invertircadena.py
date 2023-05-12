
# /*
#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#  */

cadena = 'Hola mundo'


def al_reves(cadena):
    texto_al_reves = ''
    for i in cadena:
        texto_al_reves = i+texto_al_reves
    return texto_al_reves


print(al_reves(cadena))
