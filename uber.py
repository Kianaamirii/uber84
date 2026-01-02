from algorithms.analytics import Analytics
from flask import Flask, request, render_template

from models.passenger import Passenger
from models.vehicle import Vehicle
from models.driver import Driver
from models.ride_request import RideRequest
from services.ride_service import RideService


app = Flask(__name__)
service = RideService()


v1 = Vehicle("34ABC01", "Sedan")
d1 = Driver(1, "Ali", (0, 0), v1)
service.add_driver(d1)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        px = float(request.form["px"])
        py = float(request.form["py"])
        dx = float(request.form["dx"])
        dy = float(request.form["dy"])

        passenger = Passenger(1, "Ayse", (px, py))
        ride_request = RideRequest(passenger, (dx, dy))
        ride = service.request_ride(ride_request)

        analytics = Analytics.generate(service.completed_rides)

        return render_template(
            "result.html",
            fare=ride.fare,
            time=ride.trip_time,
            analytics=analytics
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
