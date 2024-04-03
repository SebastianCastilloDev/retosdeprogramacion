#!/bin/bash
#  Crea una función que reciba días, horas, minutos y segundos (como enteros)
#  y retorne su resultado en milisegundos.
#

# Función que recibe días, horas, minutos y segundos y retorna su resultado en milisegundos|

function conversion_tiempo(){
    local dias=$1
    local horas=$2
    local minutos=$3
    local segundos=$4

    local milisegundos=$(( (dias * 86400 + horas * 3600 + minutos * 60 + segundos) * 1000 ))
    echo $milisegundos
}

