""" Crear una función es_par(numero) que devuelva True o False.  /  Crear una función area_rectangulo(ancho, alto) que calcule el área. /  Importar math y usar sqrt, pow, pi. """

# Ejercicio 1: Crear una función es_par(numero) que devuelva True o False.
def es_par(numero):

    return numero % 2 == 0

# Ejercicio 2: Crear una función area_rectangulo(ancho, alto) que calcule el área.
def area_rectangulo(ancho, alto):
    return ancho * alto

# Ejercicio 3: Importar math y usar sqrt, pow, pi.
import math


""" prueba de las funciones """

#numeros par e impar
nummero= int(input("Introduce un número para comprobar si es par: "))
if es_par(nummero):
    print(f"El número {nummero} es par.")
else:
    print(f"El número {nummero} es impar.")

#area del rectangulo
ancho = float(input("Introduce el ancho del rectángulo: "))
alto = float(input("Introduce el alto del rectángulo: "))
area= area_rectangulo(ancho, alto)
print(f"El área del rectángulo es: {area}")


# Usando funciones de math

print("Raíz cuadrada de 16:", math.sqrt(16))              # Raíz cuadrada de 16           (la funcion sqrt devuelve la raíz cuadrada de un número)
print("Potencia de 2 elevado a 3:", math.pow(2, 3))       # Potencia de 2 elevado a 3     (la función pow devuelve el resultado de elevar un número a una potencia)
print("Potencia de 2 elevado a 5:", math.pow(2, 5))       # Potencia de 2 elevado a 5)    (la función pow devuelve el resultado de elevar un número a una potencia)
print("Valor de pi:", math.pi)                            # Valor de pi                   (la constante pi de la librería math representa el valor de pi)
