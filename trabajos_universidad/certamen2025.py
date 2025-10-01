"""def filas_secas(invernadero, umbral):
    i=0
    contador=0
    while i<len(invernadero):
        fila=""
        while i<len(invernadero) and invernadero[i]!="|":
            fila= fila+invernadero[i]                     # fila= 6-2-5
            i+=1 
        j=0
        seca= True
        while j<len(fila):
            if fila[j] != "-":
                if int(fila[j])>=umbral:
                    seca= False
            j+=1
        if seca:
            contador+=1
 
        i+=1
    return contador"""

def filas_secas(invernadero, umbral):
    contador=0
    fila=""
    for i in invernadero: 
        if i != "|":
            fila= fila+i                    # fila= 6-2-5
    
        else:
            seca = True
            for j in fila:
                if j != "-":
                    if int(j) >= umbral:
                        seca = False
            
            if seca:
                contador += 1
            fila = ""
            

x='5-7-3-5|8-2|6-2-5|9-1-1-1-9'
print(filas_secas(x, 4))
print(filas_secas("5-7-3-5|8-2|6-2-5|9-1-1-1-9", 8))
print(filas_secas("5-7-3-5|8-2|6-2-5|9-1-1-1-9", 7))
