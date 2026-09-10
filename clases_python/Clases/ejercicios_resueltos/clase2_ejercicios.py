""" Escribe un programa Pida dos números al usuario y realice todas las operaciones matemáticas con ellos, mostrando los resultados y con comentarios explicando cada línea."""

# pedir al usuario los dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

#realizar las operaciones matemáticas
suma = num1 + num2             # Suma de los dos números
resta = num1 - num2            # Resta del primer número menos el segundo
multiplicacion = num1 * num2   # Multiplicación de los dos números
division = num1 / num2         # División del primer número entre el segundo
potencia = num1 ** num2        # Potencia del primer número elevado al segundo
resto = num1 % num2            # Resto de la división del primer número entre el segundo

# Mostrar los resultados
print(f"La suma de {num1} y {num2} es: {suma}")
print(f"La resta de {num1} y {num2} es: {resta}")
print(f"La multiplicación de {num1} y {num2} es: {multiplicacion}")
print(f"La división de {num1} entre {num2} es: {division}")
print(f"{num1} elevado a la potencia de {num2} es: {potencia}")
print(f"El resto de la división de {num1} entre {num2} es: {resto}")

# Fin del programa
# Comentarios explicativos:
# 1. Se piden dos números al usuario y se convierten a tipo float para permitir decimales.
# 2. Se realizan las operaciones matemáticas básicas: suma, resta, multiplicación, división, potencia y resto.
# 3. Se almacenan los resultados de cada operación en variables correspondientes.
# 4. Finalmente, se imprimen los resultados de cada operación de forma clara y concisa.
# 5. El programa finaliza mostrando todos los resultados al usuario.
