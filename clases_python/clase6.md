# Diccionarios

## Objetivo
- Aprender a crear y utilizar diccionarios para almacenar pares clave-valor.
- Conocer las operaciones básicas que se pueden realizar en un diccionario.

---

## Diccionarios

Un diccionario es una colección de pares ue permite asociar **clave** con **valor**, donde cada clave es única.  
Cada clave debe ser única. Son mutables, es decir, podemos modificar su contenido.

El funcionamiento de diccionarios es muy parecido a cuando accedemos un elemento de una lista usando su índice.  
* En este caso el índice de la lista es una ''llave'' y el elemento es el ''valor''
* las llaves pueden ser: números (int o float), strings o listas.
* una llave no puede aparecer dos veces. (deben ser únicas)

Los elementos de un diccionario son: 
- El diccionario está delimitado por paréntesis de llave { }.
- Cada par llave-valor se separa del resto con coma ,.
- Cada llave se separa de su valor utilizando el caracter dos puntos :.


*Ejemolo:*
```  
promedios = { 
    "pepito" : 82,
    "Juan" : 55,
    "Francisca" : 20,
    "camila" : 97,
    }
# muestra la nota de Pepito
print(promedio["Pepito"])
```     
*Crear diccionarios:*  
```  
dicionario_vacio2 = {} 
dicionario_vacio2 = dict()
estudiante = {
    "nombre": "Felipe",
    "cursos": { "Matemáticas": 95,
                "Programación": 98,
                "Ingles": 50
    } }
```  

*Acceder a elementos:* 
```  
patas = {'humano': 2, 'pulpo': 8, 'perro': 4, 'gato': 4}
print(patas['gato']) → imprime el elemento que esta en la llave gato en este caso 4
```  

---


**Tarea:**  
Crea un diccionario con información sobre ti (nombre, edad, carrera, etc.)