<?php

$frase = "Anita lava la tina";
$otraFrase = "Esta es otra frase";

function minusculas($frase) {
    return strtolower($frase);
}

function eliminaEspacios($frase) {
    $cadena = "";
    for ($i=0; $i < strlen($frase); $i++) {
        $caracter = substr($frase,$i,1);
        if ($caracter != " ") {
            $cadena = $cadena . $caracter;
        }
    }
    return $cadena;
}

function invertirCadena($frase) {
    $cadena = "";
    for($i=0; $i < strlen($frase); $i++){
        $cadena = $frase[$i] . $cadena;
    }
    return $cadena;
}

function esPalindromo($frase) {
    return minusculas(eliminaEspacios($frase)) === invertirCadena(minusculas(eliminaEspacios($frase)));
}

function resultadoPalindromo($frase) {
    if (esPalindromo($frase)) {
        echo "La frase: " . $frase . " es palíndromo";
    } else {
        echo "La frase: " . $frase . " NO es palíndromo";
    }
}

resultadoPalindromo($frase);
echo "<br>";
resultadoPalindromo($otraFrase);

