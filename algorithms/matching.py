import heapq
from multiprocessing import heap
from models.ride import Ride


class GreedyMatcher:
    @staticmethod
    def match(drivers, requests, rate):
            heap = []
            rides = []


            for d in drivers:
                if d.available:
                   heapq.heappush(heap, (0, d))


            for req in requests:
                if not heap:
                        break
                _, driver = heapq.heappop(heap)
                driver.available = False

                trip_time = req.distance / 40
                fare = req.distance * trip_time * rate
                rides.append(Ride(req, driver, fare, trip_time))


                driver.available = True
                heapq.heappush(heap, (trip_time, driver))


            return rides