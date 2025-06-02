ancho = int(input("Ingrese el ancho del terreno (m):"))
largo = int(input("Ingrese el largo del terreno (m):"))

lado_t=int(input("Ingrese el lado de cada sembradío (m):"))

if (lado_t> largo or lado_t > ancho or lado_t<0):
    print("No hay solución posible")
else:
  area_terreno= ancho * largo
  area_sembradio= lado_t * lado_t

  cantidad_sem= area_terreno // area_sembradio
  print("Se plantarán", cantidad_sem, "sembradíos de", lado_t, "*", lado_t)

  metros_plantados= area_sembradio * cantidad_sem
  print("El total sembrado será de", metros_plantados, "m2")

  sobrante= area_terreno - metros_plantados
  print("El sobrante no sembrado en el terreno será de", sobrante, "m2")

  cantidad_sen_hum = 4 * metros_plantados
  cant_sen_tem = metros_plantados
  cant_sen_ph = 3* metros_plantados

  if cantidad_sem <=200:
      precio_sensore= (cantidad_sen_hum * 350) + (cant_sen_tem * 450) + (cant_sen_ph * 1400)
  elif cantidad_sem <= 400:
      precio_sensore= (cantidad_sen_hum * 300) + (cant_sen_tem * 350) + (cant_sen_ph * 1200)
  elif cantidad_sem <= 1000:
      precio_sensore= (cantidad_sen_hum * 250) + (cant_sen_tem * 250) + (cant_sen_ph * 1000)
  else:
      precio_sensore= (cantidad_sen_hum * 200) + (cant_sen_tem * 150) + (cant_sen_ph * 800)

  precio_sensore = float(precio_sensore/1000000)
  print("El costo de los sensores será: M$", round(precio_sensore, 2))

  subsidio= float(15 * (metros_plantados// 10000))
  print("El subsidio del gobierno será: M$", round(subsidio, 2))

  costo_total= float(precio_sensore - subsidio)
  print("Costo total de la plantación: M$", round(costo_total, 2))