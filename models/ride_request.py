from utils.distance import distance


class RideRequest:
    def __init__(self, passenger, destination):
            self.passenger = passenger
            self.pickup = passenger.location
            self.destination = destination
            self.distance = distance(self.pickup, destination)
            self.assigned_driver = None


class RideRequest:
    def __init__(self, passenger, destination):
        self.passenger = passenger
        self.pickup = passenger.location
        self.destination = destination
        self.distance = distance(self.pickup, destination)
        self.assigned_driver = None