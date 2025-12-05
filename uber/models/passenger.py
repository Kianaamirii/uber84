from models.ride import Ride


class Passenger:
    def __init__(self, name):
        self.name = name

    def request_ride(self, origin, destination):
        return Ride(self, origin, destination)
    
