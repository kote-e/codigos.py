# Clase 1: Instalación y Configuración

## Objetivo

- Entender qué es un algoritmo
- Instalar Python y un entorno de desarrollo integrado (IDE).
- Familiarizarse con la terminal y la interfaz del IDE.
- Ejecutar el primer programa en Python: "Hello, World!".

---

## ¿Qué es un algoritmo?

Antes de instalar nada, tenemos que entender qué es programar y que es un algoritmo.  
Un algoritmo es una secuencia ordenada de pasos para resolver un problema. En este caso sirven para que la computadora entienda lo que queremos hacer.  

 *Ejemplo: preparar té*  
   * Calentar agua
  * Poner el té en la taza
  * Verter agua caliente
  * Esperar 3 minutos
  * Servir 

Esto también es un algoritmo, pero en programación le daremos estas instrucciones a una computadora usando un lenguaje: en este caso, Python.  

## Instalación de Python

- Ve al sitio oficial de Python: [Descarga desde](https://www.python.org/downloads/)
- Descarga la versión más reciente de Python compatible con tu sistema operativo.  
  **IMPORTANTE:** Marcar la casilla “Add Python to PATH” en el instalador ya que le dice al computadora cómo encontrar Python cuando lo uses en la terminal.

---

## Instalación del IDE

**Primero, ¿qué es un IDE?**

Un IDE (Entorno de Desarrollo Integrado) es una aplicación de software que combina varias herramientas necesarias para desarrollar código de forma eficiente.  
Es como un cuaderno inteligente donde vamos a escribir y ejecutar nuestro código cómodamente.

### Paso 1: Descarga e Instalación de un IDE

- PyCharm: [Descarga desde](https://www.jetbrains.com/es-es/pycharm/download/?section=windows) (si quieres algo más profesional).
- VS Code: [Descarga desde](https://code.visualstudio.com/download) (más liviano, ideal para iniciar).  
  Sigue las instrucciones de instalación específicas para tu sistema operativo.

### Paso 2: Configuración del IDE

- Abre el IDE instalado.
- Crea un nuevo proyecto de Python.
- Configura el intérprete de Python en el IDE, asegurándote de seleccionar la versión de Python que acabas de instalar.

---

## Introducción a la Terminal y al IDE

- **Terminal:** La terminal es esa pantallita negra donde vamos a ejecutar comandos. Es como hablarle directamente a la computadora.  
  Para usarla:
  - Presiona la tecla de Windows y la letra `R` para abrir la ventana de "Ejecutar".
  - Escribe `cmd` y presiona Enter.
  - O bien búscalo directamente en la barra de búsqueda.

Para comprobar si Python quedó instalado, escribe:

```python --version```

Si todo está bien, deberían ver algo como: Python 3.12.2 (la versión puede variar)

## Primer programa: ¡Hola Mundo!
Vamos a escribir nuestro primer código:

- Creamos un archivo llamado hello.py.
- Dentro escribimos:
    ```print("Hello, World!")```

- Ahora lo ejecutamos en la terminal:
    python hello.py
Si ven el mensaje Hello, World!, ¡felicitaciones¡

¿Qué hicimos?
- print() es una función que muestra el texto en pantalla.
- "Hello, World!" es un string (cadena de texto).

---

## Recursos Extra

[Documentación oficial de Python](https://docs.python.org/3/)  
[W3Schools Python Tutorial](https://www.w3schools.com/python/)
