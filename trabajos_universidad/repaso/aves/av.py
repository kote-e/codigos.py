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
    
    mejores=[]
    for j in aves:
        mejores.append((aves[j], j))
    mejores.sort(reverse=True)

    for i in range(3):
        mas_vistos.write(f"se observaron {mejores[i][1]} especimenes de {mejores[i][0]}\n")

    archivo.close()
    mas_vistos.close()
    return contador



def vistos_por_ciudad(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    ciudades={}
    mas_vistos_ciudad= open("mas_vistos_ciudad.txt", "w")
    num_ciudades=0
    for linea in archivo:
        datos= linea.strip().split(":")
        ciudad= datos[1]
        pajaros= datos[-1].strip().split(",")
        fecha = datos[0]
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
        fecha= datos[0][0].strip().split("/")
        datos.sort()
    
    for ci in ciudades:
        mas_vistos_ciudad.write(f"{ci}:\n")
        for i in ciudades[ci]:
            mas_vistos_ciudad.write(f"{i[0]}: {i[1]}\n")

    archivo.close()
    mas_vistos_ciudad.close
    return num_ciudades


def agrupa_por_ciudad_y_especie(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    observaciones= {}
    for linea in archivo:
        datos= linea.strip().split(":")
        ciudad= datos[1]
        pajaros= datos[-1].strip().split(",")
        fecha = datos[0]
        for pa in pajaros:
            if pa not in observaciones:
                observaciones[pa] = {}
            if ciudad not in observaciones[pa]:
                observaciones[pa][ciudad] = []
            observaciones[pa][ciudad].append(fecha)
            observaciones[pa][ciudad].sort()

    for especie in observaciones:
        new_archivo = open(f"vistos_por_ciudad_{especie}.txt", "w")
        new_archivo.write(f"{especie}:\n")
        new_archivo.write("\n")
        for ciudad in observaciones[especie]:
            new_archivo.write(f"{ciudad}:\n")
            for fecha in observaciones[especie][ciudad]:
                new_archivo.write(f"{fecha}\n")
            new_archivo.write("\n")
        new_archivo.close()

    archivo.close()
    return 0



print(vistos_por_ciudad("observaciones.txt"))
print(mas_vistos("observaciones.txt"))
print(agrupa_por_ciudad_y_especie("observaciones.txt"))