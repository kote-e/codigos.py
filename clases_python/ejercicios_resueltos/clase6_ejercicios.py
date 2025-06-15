""" Crea un diccionario con información sobre ti (nombre / edad / carrera, trabajo o materias, etc.) y Agregarle una ciudad."""

# Ejemplo de diccionario
mi_informacion = {
    "nombre": "Maria", 
    "edad": 21,
    "carrera": "Ingeniería en informatica"
}

# Agregar una ciudad al diccionario
mi_informacion["ciudad"] = "Santiago"

# Mostrar el diccionario completo
print(mi_informacion)
# Mostrar un valor específico del diccionario
print(mi_informacion["nombre"])
# Mostrar todos los valores del diccionario
print(mi_informacion.values())
# Mostrar todas las claves del diccionario
print(mi_informacion.keys())

# Mostrar todos los items del diccionario
print(mi_informacion.items())
# Mostrar el tipo de dato del diccionario
print(type(mi_informacion))
# Mostrar la longitud del diccionario
print(len(mi_informacion))
# Mostrar si una clave existe en el diccionario
print("nombre" in mi_informacion)  # True
print("apellido" in mi_informacion)  # False
# Eliminar una clave del diccionario
del mi_informacion["edad"]
# Mostrar el diccionario después de eliminar una clave
print(mi_informacion)
