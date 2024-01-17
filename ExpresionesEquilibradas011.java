
/*
 * Reto #10
 * EXPRESIONES EQUILIBRADAS
 * Fecha publicación enunciado: 07/03/22
 * Fecha publicación resolución: 14/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y
 * corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y
 * de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más
 * importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 *
 */

/*
 Análisis: Si una expresión está equilibrada, el numero de paréntesis que abren y cierran es el mismo.
 Si sumamos y restamos una unidad por cada parentesis de abertura y de cierre, respectivamente,
 el resultado final debe ser 0, para cada tipo de paréntesis.

 Resolución:
    1.- Crear una variable para cada tipo de paréntesis.
    2.- Recorrer la expresión caracter a caracter.
    3.- Si el caracter es un paréntesis de apertura, sumar 1 a la variable correspondiente.
    4.- Si el caracter es un paréntesis de cierre, restar 1 a la variable correspondiente.
    5.- Si el resultado de alguna de las variables es distinto de 0, la expresión no está equilibrada.


*/

public class ExpresionesEquilibradas011 {
    public static void main(String[] args) {

        // Expresion de prueba.
        // String expresion = "{ [ a * ( c + d ) ] - 5 }";
        String expresion = "{ [ ( a * ( c + d ) ] - 5 }";

        int parentesis = 0;
        int llaves = 0;
        int corchetes = 0;

        for (int i = 0; i < expresion.length(); i++) {
            switch (expresion.charAt(i)) {
                case '(':
                    parentesis++;
                    break;
                case ')':
                    parentesis--;
                    break;
                case '{':
                    llaves++;
                    break;
                case '}':
                    llaves--;
                    break;
                case '[':
                    corchetes++;
                    break;
                case ']':
                    corchetes--;
                    break;
                default:
                    break;
            }
        }

        if (parentesis == 0 && llaves == 0 && corchetes == 0) {
            System.out.println("La expresión está equilibrada.");
        } else {
            System.out.println("La expresión no está equilibrada.");
        }

    }

}