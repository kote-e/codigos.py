""" Crea una lista con los nombres de 5 amigos, luego modifica el segundo nombre en la lista y luego elimina el tercer nombre de la lista. """

# Crea una lista con los nombres de 5 amigos
amigos= ["Joaquin", "valentina", "Andres", "Javiera", "mauricio"]
# Modificar el segundo nombre (índice 1) en la lista
amigos[1] = " federico"
# Eliminar el tercer nombre (índice 2) de la lista
del amigos[2]  # Eliminar el tercer elemento (Andres)
# Imprimir la lista modificada
print(amigos)



#otra dorma de hacer la lista con un cilco for
amigos= []
for i in range(5):
    nombre = input("Ingrese el nombre del amigo: ")
    amigos.append(nombre)
# Modificar el segundo nombre (índice 1) en la lista
amigos[1] = "federico"  
# Eliminar el tercer nombre (índice 2) de la lista
del amigos[2]  # Eliminar el tercer elemento
# Imprimir la lista modificada
print(amigos)



# otra dorma de cambiar los elementos con un cilco for
amigos= ["Joaquin", "valentina", "Andres", "Javiera", "mauricio"]
for i in range(len(amigos)):
    if i == 1:
        amigos[i] = "federico"  # Modificar el segundo nombre
    elif i == 2:
        del amigos[i]  # Eliminar el tercer nombre
# Imprimir la lista modificada
print(amigos)



# Otra forma de hacerlo es con una lista por comprensión
amigos = ["Joaquin", "valentina", "Andres", "Javiera", "mauricio"]
amigos = [nombre if i != 1 else "federico" for i, nombre in enumerate(amigos) if i != 2]
# Imprimir la lista modificada
print(amigos)



# Otra forma de hacerlo es con el método pop
amigos = ["Joaquin", "valentina", "Andres", "Javiera", "mauricio"]
amigos[1] = "federico"  # Modificar el segundo nombre
amigos.pop(2)  # Eliminar el tercer nombre
# Imprimir la lista modificada
print(amigos)



# Otra forma de hacerlo es con el método remove
amigos = ["Joaquin", "valentina", "Andres", "Javiera", "mauricio"]
amigos[1] = "federico"  # Modificar el segundo nombre
amigos.remove("Andres")  # Eliminar el tercer nombre
# Imprimir la lista modificada
print(amigos)


# como vemos hay muchas formas de hacer lo mismo, pero la mejor forma es la que se adapte a tus necesidades y a tu estilo de programación.