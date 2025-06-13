# Clase 4: Funciones en Python

## Objetivo

- Aprender a definir y utilizar funciones en Python.
- Entender cómo funcionan los argumentos y parámetros en las funciones.
- Conocer cómo se utiliza ```return``` para devolver valores desde una función.

---

## Definición y Uso de Funciones

***¿Qué es una función?***  
Es un bloque de código que podemos reutilizar cada vez que queramos.  
*Sintaxis:*  
```
def nombre_funcion(parametros):
    # código
    return resultado
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

def suma(a, b):
    return a + b
```
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

---

***Tarea:***  
Crear una función es_par(numero) que devuelva True o False.  
Crear una función area_rectangulo(ancho, alto) que calcule el área.

