from models.passenger import Passenger
from models.vehicle import Vehicle
from models.driver import Driver
from models.ride_request import RideRequest
from services.ride_service import RideService


service = RideService()


v1 = Vehicle("34ABC01", "Sedan")
d1 = Driver(1, "Ali", (0, 0), v1)
service.add_driver(d1)


p1 = Passenger(1, "Ayse", (2, 2))
req = RideRequest(p1, (10, 10))
ride = service.request_ride(req)


print("Ride Fare:", ride.fare)
