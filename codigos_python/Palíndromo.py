def es_palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

x= input("Ingrese una palabra o frase: ")
es= es_palindromo(x)
if es:
    print(f"La palabra o frase '{x}' es un palíndromo.")
else:
    print(f"La palabra o frase '{x}' no es un palíndromo.")
