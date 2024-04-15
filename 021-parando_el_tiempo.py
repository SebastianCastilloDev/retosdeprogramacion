
# PARANDO EL TIEMPO
# Crea una función que sume 2 números y retorne su resultado pasados
# unos segundos.
# - Recibirá por parámetros los 2 números a sumar y los segundos que
#   debe tardar en finalizar su ejecución.
# - Si el lenguaje lo soporta, deberá retornar el resultado de forma
#   asíncrona, es decir, sin detener la ejecución del programa principal.
#   Se podría ejecutar varias veces al mismo tiempo.
# 

import asyncio

async def sumar_asincrono(a,b,segundos):
    await asyncio.sleep(segundos)
    return a + b

async def main():
    resultado = await sumar_asincrono(3,5,2)
    print(resultado)

asyncio.run(main())