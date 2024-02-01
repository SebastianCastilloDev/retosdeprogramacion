<?php

/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */


function eliminaEspacios($cadena) {
    $resultado = "";
    for ($i = 0; $i < strlen($cadena); $i++) {
        if ($cadena[$i] != " ") {
            $resultado .= $cadena[$i];
        }
    }

    return $resultado;
}


function excluirCaracteres($cadena1, $cadena2) {
    $resultado = "";
    for ($i = 0; $i < strlen(eliminaEspacios($cadena1)); $i++) {
        $caracter = eliminaEspacios($cadena1)[$i];
        if (!str_contains(eliminaEspacios($cadena2), $caracter)) {
            $resultado .= $caracter;
        }
    }

    return $resultado;
}


function cadenasExcluyentes($str1, $str2) {
    $out1 = excluirCaracteres($str1, $str2);
    $out2 = excluirCaracteres($str2, $str1);

    return [$out1, $out2];
}

function imprimirResultados() {
    $str1 = "Hola";
    $str2 = "Chancho";

    $cadenas =  cadenasExcluyentes($str1, $str2);

    echo "Out1: " . $cadenas[0];
    echo "<br>";
    echo "Out2: " . $cadenas[1];
}

imprimirResultados();