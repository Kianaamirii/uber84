class Location:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def repr(self):
        return f"Location(lat={self.lat}, lon={self.lon})"
    
#EXAMPLE USAGE: 
loc1 = Location(37.7749, -122.4194)
loc2 = Location(34.0522, -118.2437)
