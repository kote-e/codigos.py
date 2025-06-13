# Clase 2: Sintaxis Básica

## Objetivo

- Entender cómo declarar y usar variables en Python.
- Conocer los tipos de datos básicos y cómo funcionan.
- cómo escribir un código bien documentado.

---

## Variables y Tipos de Datos

Las variables son espacios en la memoria que almacenan datos  
(en Python no es necesitas declarar el tipo de variable se asigna el tipo automáticamente según lo que guardemos.)  

**Tipos de datos básicos:**

| Tipo            | Ejemplo      | Código           |
| --------------  | ------------ | ---------------- |
| Entero (int)    | 5            | x = 5            |  
| Flotante (float)| 3.14         | pi = 3.14        |
| Cadena (str)    | "Hola"       | saludo = "Hola"  |
| Booleano (bool) | True / False | activo = True    |

Ejemplo completo:

```
x = 10
pi = 3.14
nombre = "tu nombre"
activo = True

print(x, type(x))
print(nombre, type(nombre)) 
```

---

## Operaciones Matemáticas Básicas

En python se pueden hacer sumas, restas, multiplicaciones, divisiones y más...  
Operaciones comunes:  
-Suma (+)
-Resta (-)
-Multiplicación (*)
-División (/)
-Potencia (**)
-Módulo (%): Retorna el residuo de la división

Ejemplo:  
```
a = 10
b = 3

print(a + b)  # suma: 13
print(a - b)  # resta: 7
print(a * b)  # multiplicación: 30
print(a / b)  # división: 3.3333333333333335
print(a ** b) # potencia: 1000
print(a % b)  # módulo: 1
```

## Comentarios y buenas prácticas

Los comentarios son líneas en el código que Python ignora al ejecutar. Se usan para explicar partes del código y mejorar la legibilidad. (nos ayudan a entender el código.)  
Sintaxis de Comentarios:  
* Comentarios de una línea: Se usan con el símbolo #.
* Comentarios de múltiples líneas: Se pueden hacer usando comillas triples """.  
Ejemplo:  
```  
# Esto es un comentario de una línea

"""
Esto es un comentario 
de varias líneas.
"""
x = 5     # Le asignamos a x un valos
print(x)  # Esto imprime el valor de x
```

Siempre usen nombres de variables descriptivos y comenten las partes importantes.

---

**Tarea:**  
Escribe un programa que que tome dos números y realice todas las operaciones matemáticas con ellos, mostrando los resultados y con comentarios explicando cada línea.
