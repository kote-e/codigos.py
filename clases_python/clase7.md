# Clase 7: Manejo de Archivos

## Objetivo

- Aprender a abrir, leer y escribir archivos de texto en Python.
- Conocer los distintos modos de apertura de archivos.
- Entender cómo manejar errores al trabajar con archivos.

---

## ¿Por qué trabajar con archivos? 

primero ¿Qué es un archivo de texto?, Un archivo de texto (.txt) contiene información legible por humanos: letras, números, símbolos.

Muchas veces los programas necesitan:   
- Leer información previamente guardada.
- Guardar resultados o datos generados.
- Manipular archivos externos.

Python nos permite trabajar con archivos de forma sencilla.  
Los archivos de texto están compuestos únicamente por caracteres legibles por los humanos (como letras, dígitos y caracteres de puntuación)  
Al igual que todos los archivos, los archivos de texto tienen un nombre en el dispositivo donde se almacenan.

---

## Abrir y Cerrar Archivos

Para trabajar con archivos en Python, primero necesitas abrirlos usando la función ``` open()```.
```
archivo = open("archivo.txt", "modo")
```

*Los modos de apertura son:*   
- Lectura: 'r'.
- Escritura: 'w'.
- Agregar al final del archivo: 'a'.

Cuando terminamos de usar el archivo, es importante cerrarlo para liberar recursos:   
```
archivo.close()
```   

## Leer Archivos

Puedes leer archivos completos, leer línea por línea, o leer un número específico de caracteres.   
``` 
archivo= open("datos.txt", "r")
for linea in archivo:
    print(linea.strip())        # .strip() elimina saltos de línea
archivo.close() 
``` 


## Escribir en Archivos

Puedes escribir texto en un archivo existente o crear uno nuevo si no existe.   
``` 
archivo= open("nuevo.txt", "w")
archivo.write("Primera línea\n")
archivo.write("Segunda línea\n")  
archivo.close() 
``` 

---

**Muchos errores vienen por no saber dónde se está creando o buscando el archivo.**

``` 
# Ruta relativa (funciona si estás en el mismo directorio):
with open("archivo.txt", "r") as f:

# Ruta absoluta (desde la raíz del disco):
with open("C:/Usuarios/Kote/Desktop/archivo.txt", "r") as f:
``` 

---
### Diferencia entre .read(), .readline() y .readlines()
Para que el estudiante tenga más herramientas al leer archivos:

``` 
with open("datos.txt", "r") as f:
    print(f.read())       # Todo el contenido como string
    print(f.readline())   # Una sola línea
    print(f.readlines())  # Lista con todas las líneas
``` 


### Leer datos numéricos o estructurados
Introduce el concepto de parsear datos. Ejemplo:

``` 
# archivo.txt
# 5
# 10
# 15

with open("archivo.txt") as f:
    total = 0
    for linea in f:
        total += int(linea.strip())
print("Suma:", total)
``` 

---

**Tarea:**  
Crear un archivo mis_notas.txt y escribir en él tus notas de 3 materias distintas. Luego Leer el archivo e imprimir su contenido completo línea por línea y agregar una línea adicional al archivo.