#
#  Crea una función que reciba días, horas, minutos y segundos (como enteros)
#  y retorne su resultado en milisegundos.
#


def conversor_tiempo(dias, horas, minutos, segundos):
    dias_ms = dias * 24 * 60 * 60 * 1000
    horas_ms = horas * 60 * 60 * 1000
    minutos_ms = minutos * 60 * 1000
    segundos_ms = segundos * 1000
    return dias_ms + horas_ms + minutos_ms + segundos_ms
