<?php
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */

 function factorial($n) {
    if($n == 0 || $n == 1) {
        return 1;
    } else {
        return $n * factorial($n-1);
    }
 }

 $n = 5;

 echo factorial($n);


