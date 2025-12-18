
class Driver:
    def __init__(self, driver_id, name, location, vehicle):
        self.driver_id = driver_id
        self.name = name
        self.location = location
        self.vehicle = vehicle # Aggregation
        self.available = True
        self.rating = 5.0