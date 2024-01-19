<!-- /*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */


// Solución: con un contador
// - Recorremos la expresión carácter a carácter.
// - Si es un delimitador de apertura, incrementamos el contador.
// - Si es un delimitador de cierre, decrementamos el contador.
// - Si el contador es distinto de 0, la expresión no está equilibrada.
// - Al finalizar, si el contador es 0, la expresión está equilibrada. -->


<?php

class ExpressionTester {
    private $expression;
    private $parentesisBalancer;
    private $corchetesBalancer;
    private $llavesBalancer;

    public function __construct($expression) {
        $this->expression = $expression;
        $this->parentesisBalancer = 0;
        $this->corchetesBalancer = 0;
        $this->llavesBalancer = 0;
    }

    public function isBalanced() {
        for ($i = 0; $i < strlen($this->expression); $i++) {
            $char = $this->expression[$i];
            if ($char === "(") {
                $this->parentesisBalancer++;
            } elseif ($char === ")") {
                $this->parentesisBalancer--;
            } elseif ($char === "[") {
                $this->corchetesBalancer++;
            } elseif ($char === "]") {
                $this->corchetesBalancer--;
            } elseif ($char === "{") {
                $this->llavesBalancer++;
            } elseif ($char === "}") {
                $this->llavesBalancer--;
            }
        }

        return $this->parentesisBalancer === 0 &&
            $this->corchetesBalancer === 0 &&
            $this->llavesBalancer === 0;
    }

    public function getExpression() {
        return $this->expression;
    }

    public function getParentesisBalancer() {
        return $this->parentesisBalancer;
    }

    public function getCorchetesBalancer() {
        return $this->corchetesBalancer;
    }
    
    public function getLlavesBalancer() {
        return $this->llavesBalancer;
    }

    public function printResult(){
        if ($this->isBalanced()) {
            echo "La expresión está equilibrada";
        } else {
            echo "La expresión no está equilibrada";
        }
    }
}



$expresion = "{ [ a * ( c + d ) ] - 5 }";
$expressionTester = new ExpressionTester($expresion);
echo "Expresión: " . $expressionTester->getExpression() . "<br>";
$expressionTester->printResult();
echo "<br>";
echo "<br>";
echo "Si la expresion esta equilibrada, todos los contadores de los delimitadores deben ser igual a 0 <br>";
echo "Parentesis: " . $expressionTester->getParentesisBalancer() . "<br>";
echo "Corchetes: " . $expressionTester->getCorchetesBalancer() . "<br>";
echo "Llaves: " . $expressionTester->getLlavesBalancer() . "<br>";

