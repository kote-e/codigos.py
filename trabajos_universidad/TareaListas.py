def generos_mejor_calificados(series):
    mejores_generos = []
    acumulados = []
    for serie in series:
        calificacion = serie[3]
        genros = serie[5]
        for genero in genros:
            encontrado = False
            for i in acumulados:
                if i[0] == genero:
                    i[1] += calificacion
                    i[2] += 1
                    encontrado = True
                    break
            if not encontrado:
                acumulados.append([genero, calificacion, 1])

    for i in acumulados:
        i[1] = i[1] / i[2]
    n = len(acumulados)
    for i in range(n):
        for j in range(0, n - i - 1):
            if acumulados[j][1] < acumulados[j + 1][1]:
                acumulados[j], acumulados[j + 1] = acumulados[j + 1], acumulados[j]

    mejores_generos = [item[0] for item in acumulados[:5]]
    return mejores_generos

def recomendar_series(series, año, lista_generos):
    recomendadas = []
    for s in series:
        inicio = s[1]
        fin = s[2]
        if fin == "NA":
            fin = float("inf")
        
        if inicio <= año <= fin:
            serie_genros = s[5]
            if not lista_generos or any(g in serie_genros for g in lista_generos):
                titulo = s[0]
                calificacion = s[3]
                votos = s[4]
                genros_ordenados = sorted(serie_genros)
                recomendadas.append([titulo, genros_ordenados, calificacion, votos])

    for i in range(len(recomendadas)):
        for j in range(0, len(recomendadas) - i - 1):
            if recomendadas[j][2] < recomendadas[j + 1][2]:
                recomendadas[j], recomendadas[j + 1] = recomendadas[j + 1], recomendadas[j]
            elif recomendadas[j][2] == recomendadas[j + 1][2] and recomendadas[j][3] < recomendadas[j + 1][3]:
                recomendadas[j], recomendadas[j + 1] = recomendadas[j + 1], recomendadas[j]

    return [[r[0], r[1]] for r in recomendadas[:5]]



# programa principal
series=[["The Office",2005,2013,9,770815,["Comedia"]],
["Breaking Bad",2008,2013,9.5,2314919,["Crimen", "Drama", "Suspenso"]],
["Band of Brothers",2001,2001,9.4,559518,["Acción", "Drama", "Histórica"]],
["Game of Thrones",2011,2019,9.2,2422280,["Acción","Aventura","Drama"]],
["The Simpsons",1989,"NA",8.6,451961,["Animación", "Comedia"]],
["The Sopranos",1999,2007,9.2,520737,["Crimen", "Drama"]],
["Attack on Titan",2013,2023,9.1,602664,["Acción", "Aventura", "Animación"]],
["Chernobyl",2019,2019,9.3,943168,["Drama", "Histórica", "Suspenso"]],
["Friends",1994,2004,8.9,1140227,["Comedia", "Romance"]],
["Lost",2004,2010,8.3,638100,["Aventura", "Drama", "Fantasía"]],
["Dark",2017,2020,8.7,488096,["Crimen", "Drama", "Misterio"]],
["Sherlock",2010,2017,9.1,1044777,["Crimen", "Drama", "Misterio"]],
["31 minutos",2002,2014,9.1,1710,["Comedia", "Familiar", "Fantasía"]],
["Stranger Things",2016,2025,8.6,1435806,["Drama", "Fantasía", "Terror"]],
["Narcos",2015,2017,8.7,498592,["Biográfica", "Crimen", "Drama"]],
["The Mandalorian",2019,"NA",8.6,621020,["Acción", "Aventura", "Fantasía"]],
["House of Cards",2013,2018,8.6,545828,["Drama"]]]

#ejercicio 1
print("P1:")
print(generos_mejor_calificados(series))

#ejercicio 2
print("P2:")
print(recomendar_series(series,2017,["Drama"]))
print(recomendar_series(series,2020,["Animación"]))
print(recomendar_series(series,2010,[]))
print(recomendar_series(series,2022,["Fantasía","Animación"]))
print(recomendar_series(series,2024,["Biográfica"]))
