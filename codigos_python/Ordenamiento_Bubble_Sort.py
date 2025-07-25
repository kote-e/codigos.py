'''  Ordena una lista de números utilizando el algoritmo de Bubble Sort.

    Parámetros:
    lista (list): La lista de elementos (números) que se desea ordenar.
    Retorna:
    list: Una nueva lista con los elementos ordenados de menor a mayor.'''


def bubble_sort(lista):
    n = len(lista)      # Longitud de la lista
    for i in range(n):
        for j in range(0, n-i-1):                           # Últimos i elementos ya están ordenados
            if lista[j] > lista[j+1]:                       # Compara el elemento actual con el siguiente
                lista[j], lista[j+1] = lista[j+1], lista[j] # Intercambia si están en el orden incorrecto
    return lista


print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))