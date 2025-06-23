# Clase 4: Funciones en Python

## Objetivo

- Aprender a definir y utilizar funciones en Python.
- Entender cómo funcionan los argumentos y parámetros en las funciones.
- Conocer cómo se utiliza ```return``` para devolver valores desde una función.

---

## Definición y Uso de Funciones

***¿Qué es una función?***  
Es un bloque de código que ejecuta una tarea específica, que podemos reutilizar cada vez que queramos.  
*Sintaxis:*  
```
def nombre_funcion(parametros):
    # código que realiza una tarea
    return valor  # (opcional)
```

*Ejemplo:*  
```
def saludar(nombre):
    mensaje = "Hola, " + nombre + "!"
    return mensaje

print(saludar("nombre"))
```

---

## Parámetros y argumentos

- Parámetros: Lo que va entre los paréntesis al definir la función.  
- Argumentos: Lo que pasamos al llamar la función.  

*Ejemplo:*  
```
def suma(a, b):
    return a + b

# Llamada a la función con argumentos
resultado = suma(5, 7)
print(resultado)  # Salida: 12
```

---

## Devolver varios valores

La palabra clave ```return``` se utiliza para devolver un valor desde una función.  
Podemos devolver más de un resultado:  
```
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

s, r = operaciones_basicas(10, 4)
print("Suma:", s)
print("Resta:", r)
```

* *Puedes llamar funciones dentro de otras:*


---

## bibliotecas

*¿Qué es una biblioteca?*
Las bibliotecas en Python simplifican la programación al proporcionar código reutilizable para realizar tareas comunes. En lugar de escribir código desde cero para cada proyecto, puedes importar bibliotecas que ya implementan esas funcionalidades, ahorrando tiempo y esfuerzo. Por ejemplo, si necesitas realizar cálculos matemáticos complejos, puedes importar la biblioteca math en lugar de escribir todas las funciones tú mismo.

### *¿Cómo importar bibliotecas?*  

Para incluir una biblioteca o funcion en particular es sencillo y se realiza con la palabra clave ```import``` . Existen diferentes formas de importar: 

- *Importar toda la biblioteca:*  
```
    import nombre_de_la_biblioteca
```   

- Importar solo funciones específicas: 
```   
    from nombre_de_la_biblioteca import nombre_de_la_funcion
```   
Con esta opción, puedes usar la función directamente sin necesidad de especificar el nombre de la biblioteca. Por ejemplo:
```
    from math import sqrt
    resultado = sqrt(25)
    print(resultado)  # Salida: 5.0
```


Para utilizar una función de la biblioteca importada, debes usar el nombre de la biblioteca seguido de un punto y el nombre de la función. 
*Por ejemplo:*   
```
    import math
    resultado = math.sqrt(16)
    print(resultado)  # Salida: 4.0
```

*Ejemplos de bibliotecas populares:*  
* math: Ofrece funciones matemáticas como sqrt, sin, cos, etc.
* random: Genera números aleatorios.
* datetime: Maneja fechas y horas.
* pandas: Para análisis y manipulación de datos.
* numpy: Para cálculos numéricos y manipulación de arrays.

---

**Tarea:**  
Crear una función es_par(numero) que devuelva True o False.  
Crear una función area_rectangulo(ancho, alto) que calcule el área.
Importar math y usar sqrt, pow, pi.

