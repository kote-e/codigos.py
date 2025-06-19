# Clase 2: Sintaxis Básica

## Objetivo

- Aprender a usar print() para mostrar datos.
- Entender cómo declarar y usar variables en Python.
- Conocer los tipos de datos básicos y cómo funcionan.
- Usar input() para obtener información del usuario.
- cómo escribir un código bien documentado.

---

## ¿Qué es print()?

Es una función de salida.  
Sirve para mostrar información en la Terminal.
```
print("Hola mundo")
print(3 + 5)
```

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

*Ejemplo completo:*  
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
- Suma (+)  
- Resta (-)  
- Multiplicación (*)  
- División (/)  
- Potencia (**)  
- Módulo (%): Retorna el resto de la división  

*Ejemplo:*
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

---

## Entrada de datos desde la terminal

Hasta ahora nosotros hemos asignado los valores directamente en el código.  
Pero muchas veces queremos que sea el usuario quien ingrese los datos mientras el programa se está ejecutando.  
Para eso usamos la función ```input()```.  

*Ejemplo:*
```
nombre = input("Por favor ingresa tu nombre: ")
print("Hola", nombre)
```   
Cuando corran este programa, la consola va a mostrar:

```Por favor ingresa tu nombre:```  
y el usuario podrá escribir su nombre, que quedará guardado en la variable nombre.

**Recordatorio sobre tipos:**  
Todo lo que viene desde ```input()``` es siempre un string (cadena de texto), aunque el usuario escriba un número.  
Si queremos usar esos datos como números, debemos convertirlos.  

***Conversión a entero o flotante:***  
```
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros: "))

print("Tienes", edad, "años y mides", altura, "metros.")
```   
Fíjense que usamos ```int()``` para convertir a entero, o ```float()``` para convertir a número decimal.

---

## Comentarios y buenas prácticas

Los comentarios son líneas en el código que Python ignora al ejecutar. Se usan para explicar partes del código y mejorar la legibilidad. (nos ayudan a entender el código.)  
Sintaxis de Comentarios:  
* Comentarios de una línea: Se usan con el símbolo #____.
* Comentarios de múltiples líneas: Se pueden hacer usando comillas triples """----""".  
*Ejemplo:*  
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

## Recomendaciones

- Usa nombres claros para tus variables (nombre, edad, total, etc.).
- Agrega comentarios que te ayuden a recordar qué hace cada parte.
- Prueba siempre tu código varias veces cambiando los valores de entrada.

---


**Tarea:**  
Escribe un programa Pida dos números al usuario y realice todas las operaciones matemáticas con ellos, mostrando los resultados y con comentarios explicando cada línea.
