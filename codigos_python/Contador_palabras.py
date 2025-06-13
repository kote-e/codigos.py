def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

texto = input("Ingrese una palabra o frase: ")
print(contar_palabras(texto))