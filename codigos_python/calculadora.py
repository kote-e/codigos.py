def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"

a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

print("Suma:", sumar(a, b))
print("Resta:", restar(a, b))
print("Multiplicación:", multiplicar(a, b))
print("División:", dividir(a, b))