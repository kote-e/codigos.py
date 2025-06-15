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

*Modificar diccionarios:* 
Al igual que las listas, los dicionarios son mutables, por lo que podemos:  
- Agregar elementos:  
```
atas = {'humano': 2, 'perro': 5, 'gato': 4}
patas['pulpo'] = 8 # esto agrega un llave llamada pulpo y se le asigna el valor 8
```   
- Eliminar elementos:   
```  
persona = {"nombre": "Juan", "edad": 20}
del persona["edad"] # esto borra la llave edad
```   
- Cambiar elementos:  
```  
patas = {'humano': 2, 'pulpo': 8, 'perro': 5, 'gato': 4}
patas["perro"] = 4
```   

## Otras operaciones útiles en Diccionarios
*Cantidad de elementos:*  
```
print(len(patas))
```  
*Saber si una llave está en el diccionario:*  
```
print('pulpo' in patas)  # True
```   
*Recorrer diccionarios:*    
Un ciclo for puede ser usado para recorrer un diccionario:
```
for pa in patas:
    print(pa)        #esto imprime las llaves
    print(patas[pa]) #esto imprime el elemento en la llave pa
```  

- Una de las grandes diferencias de las listas y los diccionarios es cuando usarlos, Cuando el orden o la secuencia es importante ysamos una lista y Cuando quieres asociar una clave con un valor (como un mini "archivo de datos") usamos un duiccionario.
- otra diferencia es que las listas si pueden tener elementos repetidos, en cambio en los diccionarios las claves no pueden repetirse (los valores sí).

### Cuándo usar listas y diccionarios

| Situación         | Usar listas cuando                                         | Usar diccionarios cuando                                                    |
|-------------------|------------------------------------------------------------|-----------------------------------------------------------------------------|
| Identificación    | No necesitas identificar los datos con un nombre especial  | Quieres asociar una clave con cada dato                                     |
| Orden             | El orden es importante                                     | El orden no es tan importante (aunque desde Python 3.7 sí conservan orden)  |
| Acceso            | Accedes a los datos por posición (índice)                  | Accedes por clave                                                           |
| Ejecución típica  | Recorrer secuencialmente                                   | Buscar rápidamente un dato por clave                                        |
| Tipo de datos     | Datos simples o secuencias                                 | Datos estructurados con relación clave-valor                                |

### Resumen express

| Quiero…                                 | Uso         |
|-----------------------------------------|-------------|
| Almacenar varios datos simples en orden | Lista       |
| Asociar un dato a un nombre o clave     | Diccionario |
| Recorrer por posición                   | Lista       |
| Acceder directo por nombre (clave)      | Diccionario |

---

**Tarea:**  
Crea un diccionario con información sobre ti (nombre / edad / carrera, trabajo o materias, etc.) y Agregarle una ciudad.