class RideService:

    def __init__(self):

        self.rides = []



    def add_ride(self, ride):

        self.rides.append(ride)

    
    def get_rides(self):

        return self.rides
    
    def find_rides_by_passenger(self, passenger_name):

        return [ride for ride in self.rides if ride.passenger.name == passenger_name]