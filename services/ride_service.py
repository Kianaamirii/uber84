from utils.distance import distance
from models.ride import Ride


class RideService:
    def __init__(self, rate_per_km=2):
            self.drivers = []
            self.completed_rides = []
            self.rate = rate_per_km

    def add_driver(self, driver):
       self.drivers.append(driver)


    def find_nearest_driver(self, pickup):
        available = [d for d in self.drivers if d.available]
        if not available:
          return None
        return min(available, key=lambda d: distance(d.location, pickup))


    def estimate_fare(self, dist, time):
       return dist * time * self.rate


    def request_ride(self, request):
        driver = self.find_nearest_driver(request.pickup)
        if not driver:
            return None


        driver.available = False
        request.assigned_driver = driver


        trip_time = request.distance / 40
        fare = self.estimate_fare(request.distance, trip_time)
        ride = Ride(request, driver, fare, trip_time)


        driver.location = request.destination
        driver.available = True
        self.completed_rides.append(ride)
        return ride