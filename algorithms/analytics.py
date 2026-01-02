
class Analytics:
    @staticmethod
    def generate(rides):
        if not rides:
           return {}


        return {
            "average_trip_time": sum(r.trip_time for r in rides)/len(rides),
            "average_fare": sum(r.fare for r in rides)/len(rides),
            "total_rides": len(rides)
            }
