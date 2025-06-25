def mas_vistos(nombre_archivo):
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



def vistos_por_ciudad(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    ciudades={}
    mas_vistos_ciudad= open("mas_vistos_ciudad.txt", "w")
    num_ciudades=0
    for linea in archivo:
        datos= linea.strip().split(";")
        ciudad= datos[1]
        pajaros= datos[-1].strip().split(",")
        fecha = datos[0].strip().split("/")
        if ciudad not in ciudades:
            ciudades[ciudad]= []
            for pa in pajaros:
                ciudades[ciudad].append([fecha, pa])
        else:
            for pa in pajaros:
                ciudades[ciudad].append([fecha, pa])
    
    for ciudad in ciudades:
        datos= ciudades[ciudad]

        num_ciudades+=1
        
            




    archivo.close()
    return a0


a= mas_vistos("observaciones.txt")