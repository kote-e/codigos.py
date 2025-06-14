'''Condicionales'''
edad = 20

if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes exactamente 18 años")
else:
    print("Eres mayor de edad")




'''Operadores lógicos y de comparación'''
a = True
b = False
if a and b:
    print("Ambos son verdaderos")
elif a or b:
    print("Al menos uno es verdadero")
else:
    print("Ninguno es verdadero")

# Comparación de números
x = 10
y = 20
if x < y:
    print("x es menor que y")
elif x == y:
    print("x es igual a y")
else:
    print("x es mayor que y")




'''Bucles'''
# Bucle while
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
# Bucle for
for i in range(5):
    print("Número:", i)




'''Funciones útiles'''

# Función range() para generar una secuencia de números
for i in range(5):
    print(i)  # imprimirá del 0 al 4

# Función len() para obtener la longitud de una lista
frutas = ["manzana", "banana", "cereza"]
print(len(frutas))  # salida: 3