

class Ride:

    
    def __init__(self, request, driver, fare, trip_time):
        self.request = request
        self.driver = driver
        self.fare = fare
        self.trip_time = trip_time
        self.rating = None