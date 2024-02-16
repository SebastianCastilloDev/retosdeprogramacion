#!/bin/bash
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */

for i in {1..100}
do
    if [ $(($i % 3)) -eq 0 ] && [ $(($i % 5)) -eq 0 ]
    then
        echo $i "- fizzbuzz"
    elif [ $(($i % 3)) -eq 0 ]
    then
        echo $i "- fizz"
    elif [ $(($i % 5)) -eq 0 ]
    then 
        echo $i "- buzz"
    else
        echo $i
    fi
done