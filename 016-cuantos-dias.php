<?php
/*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
 */

function esFechaValida($fecha)
{
    $partes = explode('/', $fecha);
    return count($partes) === 3 && checkdate($partes[1], $partes[0], $partes[2]);
}

function diasEntreFechas($fecha1, $fecha2)
{
    if (!esFechaValida($fecha1) || !esFechaValida($fecha2)) {
        throw new Exception('Al menos una de las fechas no es válida.');
    }

    $fecha1 = new DateTime(str_replace('/', '-', $fecha1));
    $fecha2 = new DateTime(str_replace('/', '-', $fecha2));

    return abs($fecha1->diff($fecha2)->days);
}

?>

<!-- Generar html para recibir dos fechas y mostrar la cantidad de días entre ellas. -->

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dias entre fechas</title>
</head>

<body>

    <form action="016-cuantos-dias.php" method="post">
        <label for="fecha1">Fecha 1:</label>
        <input type="text" name="fecha1" id="fecha1" placeholder="dd/MM/yyyy" required>
        <br>
        <label for="fecha2">Fecha 2:</label>
        <input type="text" name="fecha2" id="fecha2" placeholder="dd/MM/yyyy" required>
        <br>
        <input type="submit" value="Calcular">
    </form>

    <?php
    if ($_POST) {
        $fecha1 = $_POST['fecha1'];
        $fecha2 = $_POST['fecha2'];

        try {
            echo "Días entre las fechas: " . diasEntreFechas($fecha1, $fecha2);
        } catch (Exception $e) {
            echo $e->getMessage();
        }
    }
    ?>

</body>

</html>