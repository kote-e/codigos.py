# Clase 7: Manejo de Archivos

## Objetivo

- Aprender a abrir, leer y escribir archivos de texto en Python.
- Conocer los distintos modos de apertura de archivos.
- Entender cómo manejar errores al trabajar con archivos.

---

## ¿Por qué trabajar con archivos?

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


## Escribir en Archivos

Puedes escribir texto en un archivo existente o crear uno nuevo si no existe.


---

**Tarea:**  
Crear un archivo mis_notas.txt y escribir en él tus notas de 3 materias distintas. Luego Leer el archivo e imprimir su contenido completo línea por línea y agregar una línea adicional al archivo.