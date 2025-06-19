# solicita el ancho y largo del terreno.
ancho = int(input("Ingrese el ancho del terreno (m):"))
largo = int(input("Ingrese el largo del terreno (m):"))

# solicita el lado de cada sembradío.
lado_t=int(input("Ingrese el lado de cada sembradío (m):"))

# Verifica si el lado del sembradío es válido. Debe ser menor o igual al largo y ancho del terreno, y mayor que 0
if (lado_t> largo or lado_t > ancho or lado_t<0):
    print("No hay solución posible")
else:
  area_terreno= ancho * largo          # área del terreno en m2
  area_sembradio= lado_t * lado_t      # área de cada sembradío en m2

#Cálculo de la cantidad de sembradíos que se pueden plantar
  cantidad_sem= area_terreno // area_sembradio
  print("Se plantarán", cantidad_sem, "sembradíos de", lado_t, "*", lado_t)

# Cálculo del área sembrada y sobrante
  metros_plantados= area_sembradio * cantidad_sem
  print("El total sembrado será de", metros_plantados, "m2")

  sobrante= area_terreno - metros_plantados
  print("El sobrante no sembrado en el terreno será de", sobrante, "m2")

# Cálculo del costo de los sensores
  cantidad_sen_hum = 4 * metros_plantados
  cant_sen_tem = metros_plantados
  cant_sen_ph = 3* metros_plantados

# Cálculo del costo de los sensores según la cantidad de sembradíos
  if cantidad_sem <=200:
      precio_sensore= (cantidad_sen_hum * 350) + (cant_sen_tem * 450) + (cant_sen_ph * 1400)
  elif cantidad_sem <= 400:
      precio_sensore= (cantidad_sen_hum * 300) + (cant_sen_tem * 350) + (cant_sen_ph * 1200)
  elif cantidad_sem <= 1000:
      precio_sensore= (cantidad_sen_hum * 250) + (cant_sen_tem * 250) + (cant_sen_ph * 1000)
  else:
      precio_sensore= (cantidad_sen_hum * 200) + (cant_sen_tem * 150) + (cant_sen_ph * 800)


# Convierte el costo de los sensores a millones de pesos
  precio_sensore = float(precio_sensore/1000000)
  print("El costo de los sensores será: M$", round(precio_sensore, 2))

# Cálculo del subsidio del gobierno
  subsidio= float(15 * (metros_plantados// 10000))
  print("El subsidio del gobierno será: M$", round(subsidio, 2))

# Cálculo del costo total de la plantación
  costo_total= float(precio_sensore - subsidio)
  print("Costo total de la plantación: M$", round(costo_total, 2))