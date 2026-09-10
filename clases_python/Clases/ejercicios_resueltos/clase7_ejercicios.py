""" Crear un archivo mis_notas.txt y escribir en él tus notas de 3 materias distintas. 
Luego Leer el archivo e imprimir su contenido completo línea por línea y agregar una línea adicional al archivo."""

# Crear y escribir en el archivo mis_notas.txt
with open('mis_notas.txt', 'w') as file:
    file.write("Matemáticas: 85\n")
    file.write("Programación:: 90\n")
    file.write("Inglés: 75\n")   

# Leer el archivo e imprimir su contenido línea por línea
with open('mis_notas.txt', 'r') as file:
    for line in file:
        print(line.strip())

# Agregar una línea adicional al archivo
with open('mis_notas.txt', 'a') as file:
    file.write("Física: 62\n")

# Leer nuevamente el archivo e imprimir su contenido actualizado línea por línea
with open('mis_notas.txt', 'r') as file:
    for line in file:
        print(line.strip())



