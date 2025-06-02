def eliminar_espacios_sobrantes(texto):
    resultado = ""
    agregar_espacio = False
    i=0

    while i < len(texto):
        letra = texto[i]
        if letra != " ":
            resultado += letra
            agregar_espacio = True
        else:
            if agregar_espacio:
                resultado += " "
                agregar_espacio = False
        i += 1

    if len(resultado) > 0 and resultado[len(resultado) - 1] == " ":
        resultado = resultado[:len(resultado) - 1]

    return resultado

def invertir_palabras(texto):
    i = 0
    texto_inv = ""

    while i < len(texto):
        if texto[i] in "aeiou":
            j = i
            palabra = ""
            while j < len(texto) and texto[j] != " ":
                palabra += texto[j]
                j += 1
            k = len(palabra) - 1
            while k >= 0:
                texto_inv += palabra[k]
                k -= 1
            i = j 
        elif texto[i] != " ":
            j = i
            while j < len(texto) and texto[j] != " ":
                texto_inv += texto[j]
                j += 1
            i = j
        else:
            texto_inv += " "
            i += 1

    return texto_inv

def impar(texto):
    i = 0
    texto_mensaje=""
    while i < len(texto):
        j = i
        palabra = ""
        while j < len(texto) and texto[j] != " ":
            palabra += texto[j]
            j += 1
        if (len(palabra) % 2 == 1) and len(palabra) > 0:
            texto_mensaje += palabra[0]
        i = j + 1

    return texto_mensaje

def eliminar_signos(texto):
    limpio = ""
    i = 0
    while i < len(texto):
        letra = texto[i]
        if (("a" <= letra <= "z") or letra == " "):
            limpio += letra
        i += 1
    return limpio


mensaje = input("Mensaje recibido: ").lower()  

while mensaje.lower() != "fin":             
    mensaje = eliminar_signos(mensaje)   
    mensaje = eliminar_espacios_sobrantes(mensaje)
    mensaje = invertir_palabras(mensaje)
    mensaje_oculto = impar(mensaje)   
    print("Mensaje oculto:", mensaje_oculto.upper())
    mensaje = input("\nMensaje recibido: ").lower()


