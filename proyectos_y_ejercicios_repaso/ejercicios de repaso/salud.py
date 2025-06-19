# funcion que calcula el promedio del IMC por estado de salud y escribe en un archivo
def  promedioIMC_por_estado_de_salud (nombre_archivo, estado_salud):
    archivo = open(nombre_archivo, "r")
    archivo_chec= open(f"{estado_salud}-IMC.txt", "w")
    chequeoimc= {}
    for linea in archivo:
        todo= linea.strip().split(";")
        estado= todo[0]
        chequeo= todo[1]
        imc= todo[-1]
        if estado == estado_salud:
            if chequeo not in chequeoimc:
                chequeoimc[chequeo]=[]
            chequeoimc[chequeo].append(float(imc))
           
    #for xd in chequeoimc:
        #print(xd)
        #print (chequeoimc[xd])
   
    for prom in chequeoimc:
        suma= sum(chequeoimc[prom])
        cantidad= len(chequeoimc[prom])
        promedio= suma/cantidad
        archivo_chec.write(f"{prom}: {promedio}\n")
   
    archivo.close
    archivo_chec.close
    return chequeoimc

# Función que analiza el estado de salud y escribe en archivos separados. según si hacen ejercicio o no, y cuenta cuántos estados de salud hay.
def estado_de_salud(nombre_archivo):
    contador = 0
    archivo = open(nombre_archivo, "r")
    dicionario={}
    for linea in archivo:
        todo= linea.strip().split(";")
        estado= todo[0]
        ejercicio = todo[2]
        if estado not in dicionario:
            dicionario[estado]=[0 , 0]
        if ejercicio == "Yes":
            dicionario[estado][0] += 1
        else:
            dicionario[estado][1] += 1
   
    for cosas in dicionario:
        contador+=1
        archivo_xd= open(f"estado_de_salud_{cosas}-IMC.txt", "w")
        archivo_xd.write(f"Exercise: {dicionario[cosas][0]}\nNo Exercise: {dicionario[cosas][1]}")
        archivo_xd.close
    print (contador)
    return 0

""" programa principal"""
# print(promedioIMC_por_estado_de_salud ("datos.csv",  "Excellent"))
a= promedioIMC_por_estado_de_salud ("datos.csv",  "Excellent")
b=estado_de_salud("datos.csv")