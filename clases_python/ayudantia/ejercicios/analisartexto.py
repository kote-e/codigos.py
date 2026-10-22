def validar_texto(texto):
    return texto.strip() != ""


def contar_vocales(texto):
    vocales = "aeiouáéíóú"
    cantidad = 0

    for caracter in texto.lower():
        if caracter in vocales:
            cantidad += 1

    return cantidad


def contar_consonantes(texto):
    vocales = "aeiouáéíóú"
    cantidad = 0

    for caracter in texto.lower():
        if caracter.isalpha() and caracter not in vocales:
            cantidad += 1

    return cantidad


def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)


def invertir_texto(texto):
    invertido = ""

    for posicion in range(len(texto) - 1, -1, -1):
        invertido += texto[posicion]

    return invertido


def analizar_texto(texto):
    if not validar_texto(texto):
        return "error: debe ingresar un texto"

    resultado = ""
    resultado += "Texto original: " + texto + "\n"
    resultado += "Cantidad de caracteres: " + str(len(texto)) + "\n"
    resultado += "Cantidad de palabras: " + str(contar_palabras(texto)) + "\n"
    resultado += "Cantidad de vocales: " + str(contar_vocales(texto)) + "\n"
    resultado += "Cantidad de consonantes: " + str(contar_consonantes(texto)) + "\n"
    resultado += "Texto invertido: " + invertir_texto(texto)

    return resultado


texto_usuario = input("Ingrese un texto: ")
print("\n" + analizar_texto(texto_usuario))