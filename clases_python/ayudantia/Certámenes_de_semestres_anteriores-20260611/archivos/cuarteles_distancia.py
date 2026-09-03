# ESTA PARTE NO FORMA PARTE DEL CERTAMEN
# SE INCLUYE ÚNICAMENTE PARA QUE FUNCIONE EL CÓDIGO DE LA P1
from math import radians, sin, cos, atan2, sqrt

def distancia(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en kilómetros
    R = 6371.0

    # Convierte las latitudes y longitudes de grados a radianes
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)

    # Diferencia en coordenadas
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Fórmula de Haversine
    a = sin(dlat/2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    # Distancia en kilómetros
    dist = R * c

    return dist
