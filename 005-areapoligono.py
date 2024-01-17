
# /*
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */

def triangulo(base, altura):
    return base*altura/2


def cuadrado(lado):
    return lado**2


def rectangulo(base, altura):
    return base*altura


def area(tipo):
    if tipo == "triangulo":
        base = float(input('Ingrese la base: '))
        altura = float(input('Ingrese la altura: '))
        return triangulo(base, altura)
    elif tipo == "cuadrado":
        lado = float(input('Ingrese el lado del cuadrado: '))
        return cuadrado(lado)
    elif tipo == "rectangulo":
        base = float(input('Ingrese la base: '))
        altura = float(input('Ingrese la altura: '))
        return rectangulo(base, altura)
    else:
        raise ValueError('No soporto mas tipos de poligonos')
