from flask import Flask, render_template, request

from models.passenger import Passenger
from models.vehicle import Vehicle
from models.driver import Driver
from models.ride_request import RideRequest
from services.ride_service import RideService

app = Flask(__name__)

# ---------- Setup Service ----------
service = RideService()

drivers = [
    Driver(1, "Ali", (0, 0), Vehicle("34ABC01", "Sedan")),
    Driver(2, "Mehmet", (5, 5), Vehicle("34XYZ02", "SUV")),
    Driver(3, "Zeynep", (8, 1), Vehicle("34QWE03", "Hatchback")),
]

for d in drivers:
    service.add_driver(d)


# ---------- Routes ----------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        px = float(request.form["px"])
        py = float(request.form["py"])
        dx = float(request.form["dx"])
        dy = float(request.form["dy"])

        passenger = Passenger(1, name, (px, py))
        ride_request = RideRequest(passenger, (dx, dy))
        ride = service.request_ride(ride_request)

        if ride:
            result = {
                "passenger": passenger.name,
                "driver": ride.driver.name,
                "fare": round(ride.fare, 2)
            }
        else:
            result = {"error": "No available drivers"}

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request

from models.passenger import Passenger
from models.vehicle import Vehicle
from models.driver import Driver
from models.ride_request import RideRequest
from services.ride_service import RideService

app = Flask(__name__)

# ---------- Setup Service ----------
service = RideService()

drivers = [
    Driver(1, "Ali", (0, 0), Vehicle("34ABC01", "Sedan")),
    Driver(2, "Mehmet", (5, 5), Vehicle("34XYZ02", "SUV")),
    Driver(3, "Zeynep", (8, 1), Vehicle("34QWE03", "Hatchback")),
]

for d in drivers:
    service.add_driver(d)


# ---------- Routes ----------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        name = request.form["name"]
        px = float(request.form["px"])
        py = float(request.form["py"])
        dx = float(request.form["dx"])
        dy = float(request.form["dy"])

        passenger = Passenger(1, name, (px, py))
        ride_request = RideRequest(passenger, (dx, dy))
        ride = service.request_ride(ride_request)

        if ride:
            result = {
                "passenger": passenger.name,
                "driver": ride.driver.name,
                "fare": round(ride.fare, 2)
            }
        else:
            result = {"error": "No available drivers"}

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
