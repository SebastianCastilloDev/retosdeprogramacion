<?php
/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */

 function contarDigitos($numero) {
    $divisor = 10;
    $potencia = 1;

    while ($numero / ($divisor ** $potencia) >= 1) {
        $potencia++;
    }

    return $potencia;
}

function esNumeroArmstrong($numero) {
    $nDigitos = contarDigitos($numero);
    $originalNumero = $numero; // Almacena el valor original de $numero
    $digitos = [];

    for ($i = 0; $i < $nDigitos; $i++) {
        $digitos[] = $numero % 10;
        $numero = (int)($numero / 10);
    }

    $suma = 0;

    foreach ($digitos as $digito) {
        $suma += $digito ** $nDigitos;
    }

    return $suma === $originalNumero; // Compara con el valor original
}

$numero = 371;

if (esNumeroArmstrong($numero)) {
    echo "$numero es un número de Armstrong.";
} else {
    echo "$numero no es un número de Armstrong.";
}

$numero = 372;

if (esNumeroArmstrong($numero)) {
    echo "$numero es un número de Armstrong.";
} else {
    echo "$numero no es un número de Armstrong.";
}