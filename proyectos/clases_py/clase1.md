# Clase 1: Instalación y Configuración

## Objetivo

- Instalar Python y un entorno de desarrollo integrado (IDE).
- Familiarizarse con la terminal y la interfaz del IDE.
- Ejecutar el primer script en Python: "Hello, World!".

---

## 1. Instalación de Python

- Ve al sitio oficial de Python: [Descarga desde](https://www.python.org/downloads/)
- Descarga la versión más reciente de Python compatible con tu sistema operativo.  
  **IMPORTANTE:** Marcar la casilla “Add Python to PATH” en el instalador ya que le dice al computadora cómo encontrar Python cuando lo uses en la terminal.

---

## 2. Instalación del IDE

**Primero, ¿qué es un IDE?**

Es una aplicación de software que combina varias herramientas necesarias para desarrollar código de forma eficiente.  
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

## 3. Introducción a la Terminal y al IDE

- **Terminal:** La terminal es esa pantallita negra donde vamos a ejecutar comandos. Es como hablarle directamente a la computadora.  
  Para usarla:
  - Presiona la tecla de Windows y la letra `R` para abrir la ventana de "Ejecutar".
  - Escribe `cmd` y presiona Enter.
  - O bien búscalo directamente en la barra de búsqueda.

Para comprobar si Python quedó instalado, escribe:

```python --version```
Si todo está bien, deberían ver algo como: Python 3.12.2 (la versión puede variar)

## 4. Primer programa: ¡Hola Mundo!
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

**Tarea:**
Prueben hacer más mensajes con print(). Por ejemplo, imprimir tu nombre, edad, o lo que quieras.