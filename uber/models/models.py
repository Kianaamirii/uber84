from models.driver import Driver
from models.passenger import Passenger
from models.vehicle import vehicle
from models.ride import Ride
from models.ride_service import RideService


class passengerModel:
    def __init__(self, name):
        self.name = name
        self.rides = []

    def request_ride(self, origin, destination):
        ride = Ride(self, origin, destination)
        self.rides.append(ride)
        return ride