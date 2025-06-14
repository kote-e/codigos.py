# Clase 5: Listas y Tuplas

## Objetivo

- Trabajar con colecciones de datos y cadenas de texto. 
- Aprender a crear y manipular listas en Python y conocer las operaciones comunes que se pueden realizar con estas.

---

## Strings

Son el tipo de dato usado para representar texto en python.  
*Strings en entradas y salidas de datos*
```
nombre = input("Ingrese su nombre: ")
nombre= 'Juan'
print("Mi nombre es",nombre)
```
* Los valores literales '' y "" representan strings vacíos, es decir, un texto que no contiene caracteres.   
*importante:* No es lo mismo " " (espacio) que "" (vacío total)  
```
print("")
a= " "
```
*Estructura de un String*  
un string esta compuesto por caracteres.  
*por ejemplo:* "hola mundo!" tiene 11 caracteres. 
los cuales estan numerados por indices. Los caracteres de un string se numeran de izquierda a derecha, comenzando en `0`de la siguiente forma:  

| h | o | l | a |   | m | u | n | d | o | ! |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |

Se puede acceder al caracter que se encuentra en una posicion.
*ejempli:*
```
a = "hola mundo!"
#obtiene el caracter que esta en el indice 5 y lo muestra por pantalla
print(a[5])
```  

También se puede enumerar los caracteres de un string desde el final hacia el inicio, usando índices negativos que comienzan en `-1`:

| h  | o  | l  | a  |   | m  | u  | n  | d  | o  | !  |
|----|----|----|----|---|----|----|----|----|----|----|
| -11| -10| -9 | -8 | -7| -6 | -5 | -4 | -3 | -2 | -1 |

### Substrings 
Son una parte del string y se escriben de esta forma: ```nom_lista[inicio : fin]```
esto devuelve un string que tiene todos los caracteres desde el indice ```inicio``` hasta el indice ```fin-1```.  
*Ejemplo:*   
```
 a= "hola mundo"
 s= a[3:7]
```  
Visualmente:

| h | o | l | a |   | m | u | n | d | o |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

Entonces:

- `a[3:7]` toma desde el índice `3` hasta el índice `7` (sin incluirlo).
- El resultado es `'a mu'` (caracteres en las posiciones 3, 4, 5 y 6).


* Algunos operadores definidos anteriormente para números, también tienen una función al aplicarse sobre strings
    - Concatenación de strings (+)  ```"hola" +  "mundo"```   → 'holamundo'
    - Repetición de strings (*)     ```"aa" * 3 ```           → 'aaaaaa'
    - contenido de un string (in)   ```"pollo" in "Repollo"```→ True
    - Cantidad de caracteres (lend) ```lend("hola") ```       → 4
 

---

## Listas

Una lista es una colección ordenada y mutable de elementos. Permite guardar varios valores en una sola variable.  
Se puede cambiar su tamaño y modificar sus elementos.   
> Mutable → podemos agregar, quitar o cambiar elementos. 

*Crear listas:*    
```
lista_vacia = []                           # Lista vacía
lista_numeros = [1, 2, 3, 4, 5]            # Lista de números
frutas = ["manzana", "platano", "cereza"]  # Lista de frutas   
numeros =list(range(5))                    # lista de secuencia ordenada de números enteros ordenados, va desde 0 hasta fin−1.
``` 

*Acceder a elementos:*  
Al igual que los Strings, las listas tienen índices para enumerar sus elementos.

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

- Cambiar elementos:  
```
frutas[0] = "pera"
frutas[1] = "naranja"
```  
- Agregar elementos:  
```  
frutas.append("kiwi")  # Agrega al final
```
- Eliminar elementos:   
```  
frutas.remove("naranja")  # Elimina por valor
frutas.pop()              # Elimina el último
del frutas[0]             # Elimina por índice
```

## Otras operaciones útiles con listas

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
Un ciclo for puede ser usado para recorrer una listas
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


Las listas tiene una cualidad que es que podemos hacer una listas de listas o listas anidadas. Se caracterizan por que al menos un elemento de la lista es, a su vez, otra lista. 
Las listas de listas tienen las mismas caractersiticas que una lista normal:
    - Se les puede aplicar los métodos ya vistos: .append(), .sort(), .remove(), etc.
    - Estas listas pueden tener cualquier tamaño, incluso pueden crearse como listas vacias.
    - Pueden contener cualquier tipo de dato
*Ejemplo:*  
```
L1 = [1,2,3, [4,5,6,7,8], 9]
```   
Los elementos de la lista L1 son 5: 1, 2, 3, [4, 5, 6, 7, 8], 9.
Entonces, el cuarto elemento, es decir el elemento con el índice 3, es: [4, 5, 6, 7, 8].

---

**Tarea:**   
Crea una lista con los nombres de 5 amigos, luego modifica el segundo nombre en la lista y elimina el tercer nombre de la lista. 

