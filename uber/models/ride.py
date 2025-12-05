
from models.driver import Driver


class Ride:
    def __init__(self, passenger, origin, destination):
        self.passenger = passenger
        self.origin = origin
        self.destination = destination