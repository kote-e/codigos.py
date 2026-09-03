n= int(input("Ingrese un número impar mayor o igual a 3: "))

#comprobamos que el número ingresado sea impar y mayor o igual a 3
while n < 3 or n % 2 == 0:
    n= int(input("Ingrese un número impar mayor o igual a 3: "))

# inicializamos variables
espacios= 0
numeros= n
numero_actual= 1
centro= n // 2 + 1

#ciclo principal
for i in range(1, n + 1):
    for j in range(espacios):
        print(" ", end="")
    for num in range(numeros):
        print(numero_actual, end="")

    print()
    if i < centro:
        espacios += 1
        numeros -= 2
        numero_actual += 1
    else:
        espacios -= 1
        numeros += 2
        numero_actual -= 1
