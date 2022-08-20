from unittest import result


resultado = 0

def suma(a,b):
    resultado = a + b
    return resultado

def resta(a,b):
    resultado = a + b
    return resultado

def multiplicacion(a,b):
    resultado = a * b
    return resultado

def division(a,b):
    resultado = a // b
    return resultado

n1 = int(input("Primer numero -->"))
n2 = int(input("Segundo numero -->"))

opciones = int(input("Elige una operacion del 1 al 4 -->"))

if opciones == 1:
    print("La suma de", n1, "y", n2, " es", suma(n1, n2))
elif opciones == 2:
    print("La resta de", n1, "y", n2, " es", resta(n1, n2))
elif opciones == 3:
    print("La multiplicacion de", n1, "y", n2, " es", multiplicacion(n1, n2))
elif opciones == 4:
    print("La divicion de", n1, "y", n2, " es", division(n1, n2))

