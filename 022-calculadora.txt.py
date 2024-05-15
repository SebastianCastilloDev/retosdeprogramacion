

def calculadora(operacion):
    if "+" in operacion:
        # separar los números
        numeros = operacion.split("+")
        # sumar los números
        resultado = float(numeros[0]) + float(numeros[1])
        return operacion + " = " + str(resultado)
    elif "-" in operacion:
        numeros = operacion.split("-")
        resultado = float(numeros[0]) - float(numeros[1])
        return operacion + " = " + str(resultado)
    elif "*" in operacion:
        numeros = operacion.split("*")
        resultado = float(numeros[0]) * float(numeros[1])
        return operacion + " = " + str(resultado)
    elif "/" in operacion:
        numeros = operacion.split("/")
        resultado = float(numeros[0]) / float(numeros[1])
        return operacion + " = " + str(resultado)
    else:
        return "No se ha podido resolver la operación"
    

def main():
    archivo = open("022-Challenge22.txt")
    lineas = archivo.readlines()
    
    for linea in lineas:
        operacion = linea.strip()
        print(calculadora(operacion))
    
    archivo.close()

if __name__ == "__main__":
    main()
    