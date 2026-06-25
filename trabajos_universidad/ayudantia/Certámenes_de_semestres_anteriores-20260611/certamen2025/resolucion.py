def mayores_generadoras(nombre_archivo, tipo_energia, energia):
    dic={}
    lista = []
    archivo = open(nombre_archivo, 'r')
    for linea in archivo:
        datos = linea.strip().split(',')
        empresa = datos[1]
        capacidad = int(datos[4])
        tipo = datos[3]
        sies= False

        for i in tipo_energia:
            if i == tipo and tipo_energia[i] == energia:
                sies= True
                break
                
        if sies:
            if empresa not in dic:
                dic[empresa] = 0
            dic[empresa] += capacidad
    print(dic)
    
    for empresa in dic:
        lista.append([dic[empresa], empresa])

    lista.sort(reverse=True)
    lista_final = []
    for i in range(3):
        lista_final.append([lista[i][1], lista[i][0]])

    archivo.close()
    return lista_final

tipo_energia = {
    "Petróleo": "No Renovable",
    "Gas": "No Renovable",
    "Carbón": "No Renovable",
    "Nuclear": "No Renovable",
    "Solar": "Renovable",
    "Eólica": "Renovable",
    "Geotérmica": "Renovable",
    "Biomasa": "Renovable",
    "Mareomotriz": "Renovable",
    "Hidroeléctrica de pasada": "Renovable",
    "Hidroeléctrica de embalse": "Renovable",
    "Hidroeléctrica de bombeo": "Renovable"
}

print(mayores_generadoras("centrales.csv", tipo_energia, "Renovable"))