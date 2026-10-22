def contar_letras(texto):
    resultado = []
    for letra in texto:
        if letra.isalpha():  # Verifica si el carácter es una letra
            encontrada = False
            for elemento in resultado:
                if elemento[0] == letra:
                    elemento[1] += 1
                    encontrada = True
                    break
            if not encontrada:
                resultado.append([letra, 1])
    resultado.sort()
    return resultado

texto= input("Ingrese un texto: ")

print(contar_letras(texto))