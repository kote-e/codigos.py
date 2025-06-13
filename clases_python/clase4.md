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



