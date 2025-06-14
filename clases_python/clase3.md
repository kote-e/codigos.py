# Clase 3: Estructuras de Control

## Objetivo

- Comprender y utilizar condicionales (if, else, elif) .
- Trabajar con bucles (for, while).
- Introducir funciones útiles como range() y len().

---

##  Condicionales (Decisiones)

Los condicionales permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.  
**Sintaxis básica:**  

```
if condicion1:  
    # código que se ejecuta si la condicion1 se cumple.

elif condicion2: 
    # código si la  condicion 2 se cumple
    
else: #Se usa si ninguna de las condiciones se cumple.
    # código cuando ninguna de las condiciones anteriores se cumple
```

* No siempre se utilizan todos los condicionales, puedes ocupar solo un if si tienes 1 condicion.

*Ejemplo:*

```
edad = 20

if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes exactamente 18 años")
else:
    print("Eres mayor de edad")
```

---

## Bucles (Repeticiones)

Los bucles permiten repetir un bloque de código varias veces.
*Tipos de bucles:*  
-while: Repite el bloque de código mientras la condición sea verdadera.  
-for: Itera sobre una secuencia (como una lista, cadena, o rango).  

*Ejemplos:*  

* for:  
```
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
```  
* while
```
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1
```

---

## Funciones útiles

- range(): Genera una secuencia de números.  
```
for i in range(5):
    print(i)  # imprimirá del 0 al 4
```  

- len(): Nos dice cuántos elementos tiene algo.  
```
frutas = ["manzana", "banana", "cereza"]
print(len(frutas))  # salida: 3
```

---

**Tarea:**  
Hacer un programa que pida un número y diga si es par o impar.

