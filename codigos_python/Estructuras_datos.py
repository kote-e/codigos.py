lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3)
conjunto = {1, 2, 3, 3}
diccionario = {"nombre": "un mobre", 
               "edad": 22}

print(lista, tupla, conjunto, diccionario)
# Acceso a elementos de una lista
for i in range(len(lista)):
    print(f"Elemento {i}: {lista[i]}")


# Acceso a elementos de una tupla
for i in range(len(tupla)):
    print(f"Elemento {i}: {tupla[i]}")


# Acceso a elementos de un conjunto
for i, elemento in enumerate(conjunto):
    print(f"Elemento {i}: {elemento}")

# Acceso a elementos de un diccionario
for clave, valor in diccionario.items():
    print(f"{clave}: {valor}")