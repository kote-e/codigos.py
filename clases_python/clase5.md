# Clase 5: Listas y Tuplas

## Objetivo

- Aprender a crear y manipular listas en Python.
- Conocer las operaciones comunes que se pueden realizar con listas.
- Comprender qué son las tuplas y en qué se diferencian de las listas.

---

## Listas

Una lista es una colección ordenada y mutable de elementos. Se puede cambiar su tamaño y modificar sus elementos.  
> Mutable → podemos agregar, quitar o cambiar elementos. 
Crear listas:

*Sintaxis:*  
```
lista_vacia = []
frutas = ["manzana", "platano", "cereza"] 
``` 

*Acceder a elementos:*  
```
print(frutas[0])  # manzana
print(frutas[-1]) # cereza
```

*Modificar listas:*  
```
frutas[1] = "naranja"
frutas.append("kiwi")
frutas.remove("naranja")
```
