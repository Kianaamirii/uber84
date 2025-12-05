
from models.location import Location
from models.vehicle import vehicle  
from models.driver import Driver
from models.ride import Ride
from models.passenger import Passenger
from models.ride_service import RideService



class Uber:
    def __init__(self):
        self.passengers = []
        self.drivers = []
        self.vehicles = []
        self.rides = [] 

    def register_passenger(self, name):
        passenger = Passenger(name)
        self.passengers.append(passenger)
        return passenger
    
    def register_driver(self, name):
        driver = Driver(name)
        self.drivers.append(driver)
        return driver
    

    def register_vehicle(self, driver, location):
        vehicle_instance = vehicle(driver, location)
        self.vehicles.append(vehicle_instance)
        return vehicle_instance
    

    def request_ride(self, passenger, origin, destination):
        ride = passenger.request_ride(origin, destination)
        self.rides.append(ride)
        return ride
    
    def get_all_rides(self):
        return self.rides
    

    def find_rides_by_passenger(self, passenger_name):
        return [ride for ride in self.rides if ride.passenger.name == passenger_name]
    

    def find_rides_by_driver(self, driver_name):
        return [ride for ride in self.rides if ride.passenger.name == driver_name]
    
    def get_available_vehicles(self):
        return self.vehicles
    
    def get_registered_passengers(self):
        return self.passengers
    
    def get_registered_drivers(self):
        return self.drivers
    

    def get_vehicle_by_driver(self, driver_name):
        for vehicle_instance in self.vehicles:
            if vehicle_instance.driver.name == driver_name:
                return vehicle_instance
        return None


# Example usage:
if __name__ == "__main__":
    uber_app = Uber()
    passenger1 = uber_app.register_passenger("Alice")
    driver1 = uber_app.register_driver("Bob")
    vehicle1 = uber_app.register_vehicle(driver1, Location(10, 20))
    ride1 = uber_app.request_ride(passenger1, Location(10, 20), Location(30, 40))
    all_rides = uber_app.get_all_rides()
    




   




    




    






    





