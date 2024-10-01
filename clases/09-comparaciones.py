class Coordenadas:
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self,otro):
        return self.lat == otro.lat and self.lon == otro.lon
    
    def __ne__(self,otro):
        return self.lat != otro.lat or self.lon != otro.lon


cord1 = Coordenadas(23,34)
cord2 = Coordenadas(23,34)

print(cord1 != cord2)

