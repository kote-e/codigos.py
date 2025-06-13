# Clase 5: Listas y Tuplas

## Objetivo

- Aprender a crear y manipular listas en Python.
- Conocer las operaciones comunes que se pueden realizar con listas.
- Comprender qué son las tuplas y en qué se diferencian de las listas.

---

## Listas

Una lista es una colección ordenada y mutable de elementos. Permite guardar varios valores en una sola variable.  
Se puede cambiar su tamaño y modificar sus elementos.   
> Mutable → podemos agregar, quitar o cambiar elementos. 
Crear listas:

*Sintaxis:*  
```
lista_vacia = []  # Lista vacía
lista_numeros = [1, 2, 3, 4, 5]  # Lista de números
frutas = ["manzana", "platano", "cereza"]  # Lista de frutas    
``` 

*Acceder a elementos:*  
```
print(lista_vacia)       # []
print(lista_numeros)     # [1, 2, 3, 4, 5]
print(lista_numeros[0])  # 1  → primer elemento
print(lista_numeros[-1]) # 5  → último elemento

print(frutas)            # ['manzana', 'platano', 'cereza']
print(frutas[0])         # manzana
print(frutas[-1])        # cereza
print(frutas[1:3])       # ['platano', 'cereza'] → slicing (sublistas)
```

*Modificar listas:*  
Como las listas son mutables, podemos:

Cambiar elementos:  
```
frutas[0] = "pera"
frutas[1] = "naranja"
```

Agregar elementos:  
```
frutas.append("kiwi")  # Agrega al final
```

Eliminar elementos:   
```
frutas.remove("naranja")  # Elimina por valor
frutas.pop()              # Elimina el último
del frutas[0]             # Elimina por índice
```

## Otras operaciones útiles

*Saber si la lista está vacía:*  
```
print(len(lista_vacia) == 0)  # True
```

*Saber si un elemento está dentro de la lista:*  
```
print("cereza" in frutas)  # True
```

*Saber cuántos elementos tiene la lista:*  
```
print(len(frutas))  # 1
```

*Recorrer una lista (muy importante):*  
```
for fruta in frutas:
    print(fruta)
```

*Copiar una lista:*  
```
nueva_lista = frutas.copy()
print(nueva_lista)
```

**Mini resumen**  
| Operación         | Código                        |
|--------------------|------------------------------|
| Crear              | `lista = []`                 |
| Acceso             | `lista[0]`                   |
| Modificar          | `lista[0] = nuevo_valor`     |
| Agregar            | `lista.append(valor)`        |
| Eliminar por valor | `lista.remove(valor)`        |
| Eliminar por índice| `del lista[indice]`          |
| Eliminar último    | `lista.pop()`                |
| Recorrer           | `for elemento in lista:`     |
| Copiar             | `nueva_lista = lista.copy()` |
