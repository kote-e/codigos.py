# Funcion que lee un archivo de speedruns y devuelve una lista de usuarios baneados
def baneados(nombre_archivo):
    archivo= open(nombre_archivo, "r")
    baneados = []
    for linea in archivo:
        speedruns = linea.strip().split(";")
        if speedruns[-1]== "Yes":
            if speedruns[0] not in baneados:
                baneados.append(speedruns[0])
    archivo.close()
    return baneados

# Funcion que convierte un tiempo en formato "HH:MM:SS" a segundos
def convertir_tiempo (tiempo_str):
    partes = tiempo_str.split(":")
    enteros = []
    for elemento in partes:
        enteros.append(int(elemento))
    return enteros[0] * 3600 + enteros[1] * 60 + enteros[2]

# Funcion que genera un ranking de speedruns por juego y categoria
def ranking(nombre_archivo, juego):
    archivo= open(nombre_archivo, "r")
    ranking_juego = {}
    us_ban= baneados(nombre_archivo)
    for linea in archivo:
        speedruns = linea.strip().split(";")
        jugador = speedruns[0]
        pais = speedruns[1]
        juego_jugado = speedruns[2]
        categoria = speedruns[3]
        tiempo = speedruns[4]
        
        if juego_jugado == juego and jugador not in us_ban:
            if categoria not in ranking_juego:
                ranking_juego[categoria] = []
            ranking_juego[categoria].append((jugador, pais, tiempo))

    archivo.close()
    for categoria in ranking_juego:
            lista = ranking_juego[categoria]
            for i in range(len(lista)):
                min= i
                for j in range(i + 1, len(lista)):
                    if convertir_tiempo(lista[j][2]) < convertir_tiempo(lista[min][2]):
                        min = j
                lista[i], lista[min] = lista[min], lista[i]
            ranking_juego[categoria] = lista[:3]

    return ranking_juego

# Funcion que genera un reporte de speedruns por juego y categoria
def reporte(nombre_archivo):
    archivo= open(nombre_archivo, "r")
    juegos=[]

    for linea in archivo:
        speedruns = linea.strip().split(";")
        juego= speedruns[2]
        if juego not in juegos:
            juegos.append(juego)
    archivo.close()
    
    for juego in juegos:
        ar_juego= open(f"{juego}.txt", "w")
        juego_ranking = ranking(nombre_archivo, juego)
        #print(juego, juego_ranking)
        
        for categoria in juego_ranking:
            ar_juego.write(f"{categoria}\n")
            for jugador, pais, tiempo in juego_ranking[categoria]:
                ar_juego.write(f"- {jugador} ({pais}): {tiempo}\n")
        ar_juego.close()
    
    return len(juegos)



''' programa principal '''
#usuarios_ban = baneados("speedruns.txt")
#print(usuarios_ban)
#ranking_juego = ranking("speedruns.txt", "Donkey Kong Country")
#print(ranking_juego)

# Genera el reporte de speedruns y guarda los resultados en archivos por juego. El reporte se guarda en archivos con el nombre del juego
reportee= reporte("speedruns.txt")
print(reportee)
