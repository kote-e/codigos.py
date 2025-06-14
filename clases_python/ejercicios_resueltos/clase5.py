# Ejemplos de listas en Python
lista_vacia = [] # Lista vacía
lista_numeros = [1, 2, 3, 4, 5] # Lista de números  
frutas = ["manzana", "platano", "cereza"] #Lista de frutas

'''Imprimir las listas'''
print(lista_vacia)  # []


print(lista_numeros)  # [1, 2, 3, 4, 5]
print(lista_numeros[0])  # 1
print(lista_numeros[-1]) # 5

print(frutas)  # ['manzana', 'platano', 'cereza']
print(frutas[0])  # manzana
print(frutas[-1]) # cereza
print(frutas[1:3])  # ['platano', 'cereza']

# Modificar listas
frutas[0] = "pera"  # Cambiar el primer elemento
frutas[1] = "naranja" # Cambiar el segundo elemento
frutas.append("kiwi") # Añadir un nuevo elemento al final de la lista
print(frutas)  # ['pera', 'naranja', 'cereza', 'kiwi']
frutas.remove("naranja") # Eliminar un elemento específico
print(frutas)  # ['pera', 'cereza', 'kiwi']
# Eliminar el último elemento
frutas.pop()  # Eliminar el último elemento
print(frutas)  # ['pera', 'cereza']
# Eliminar un elemento por su índice
del frutas[0]  # Eliminar el primer elemento    
print(frutas)  # ['cereza']

'''Operaciones con listas'''
# Comprobar si una lista está vacía
print(len(lista_vacia) == 0)  # True
# Comprobar si un elemento está en la lista
print("cereza" in frutas)  # True
# Comprobar la longitud de la lista
print(len(frutas))  # 1                     
# Recorrer una lista
for fruta in frutas:
    print(fruta)  # cereza


# Crear una nueva lista con los elementos de otra lista
nueva_lista = frutas.copy()  # Copiar la lista
print(nueva_lista)  # ['cereza']

