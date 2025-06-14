"""Hacer un programa que pida un número y diga si es par o impar."""

# Pedir un número
numero = int(input("Introduce un número: "))

# Comprobar si es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

