def mas_vistis(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    mas_vistos= open("mas_vistos.txt", "w")
    contador=0
    aves = {}
    for linea in archivo:
        datos= linea.strip().split(";")
        #ciudad= datos[1]
        #fecha= datos[0]
        pajaros= datos[-1].strip().split(",")
        for pa in pajaros:
            if pa not in aves:
                aves[pa]=0
            aves[pa]+=1
            contador+=1
    print(contador)

    mejores=[]
    for j in aves:
        mejores.append((aves[j], j))
    mejores.sort(reverse=True)


    for i in range(3):
        mas_vistos.write(f"se observaron {mejores[i][1]} especimenes de {mejores[i][0]}\n")
    
    archivo.close()
    mas_vistos.close()
    return 0


a= mas_vistis("observaciones.txt")