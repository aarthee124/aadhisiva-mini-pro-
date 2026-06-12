from flask import Flask, render_template, request

app = Flask(__name__)

# Real Train Data - Thirumangalam to Madurai
TRAINS = {
    "12694": {
        "name": "Pearl City Express",
        "from": "Thirumangalam",
        "to": "Madurai Junction",
        "departure": "03:10",
        "arrival": "03:27",
        "duration": "17 mins",
        "distance": "18 km",
        "platform": "PF 2",
        "status": "Running On Time",
        "delay": 0,
        "current_location": "Tirupparankundram",
        "arrival_in": "8 Mins"
    },
    "16237": {
        "name": "Tuticorin Express",
        "from": "Thirumangalam",
        "to": "Madurai Junction",
        "departure": "08:10",
        "arrival": "08:30",
        "duration": "20 mins",
        "distance": "18 km",
        "platform": "PF 1",
        "status": "Running On Time",
        "delay": 0,
        "current_location": "Departed Thirumangalam",
        "arrival_in": "12 Mins"
    },
    "16724": {
        "name": "Anantapuri Express",
        "from": "Thirumangalam",
        "to": "Madurai Junction",
        "departure": "14:35",
        "arrival": "14:55",
        "duration": "20 mins",
        "distance": "18 km",
        "platform": "PF 3",
        "status": "Signal Blocked Ahead",
        "delay": 10,
        "current_location": "Near Tirupparankundram",
        "arrival_in": "30 Mins"
    },
    "56701": {
        "name": "Punalur Passenger",
        "from": "Thirumangalam",
        "to": "Madurai Junction",
        "departure": "23:45",
        "arrival": "00:08",
        "duration": "23 mins",
        "distance": "18 km",
        "platform": "PF 4",
        "status": "Running On Time",
        "delay": 0,
        "current_location": "Tirupparankundram",
        "arrival_in": "15 Mins"
    }
}

# Home page - Search form
@app.route("/")
def index():
    return render_template("index.html")

# Verify page - Confirm travel details
@app.route("/verify")
def verify():
    train_no = request.args.get("train_no", "")
    departure = request.args.get("departure", "Today")
    destination = request.args.get("destination", "Thirumangalam")
    return render_template("verify.html",
                           train_no=train_no,
                           departure=departure,
                           destination=destination)

# Dashboard page - Live status
@app.route("/dashboard")
def dashboard():
    train_no = request.args.get("train_no", "")
    departure = request.args.get("departure", "Today")
    destination = request.args.get("destination", "Thirumangalam")

    # Get train info from our data
    train = TRAINS.get(train_no)

    # All trains for recent history
    all_trains = TRAINS

    return render_template("dashboard.html",
                           train_no=train_no,
                           train=train,
                           departure=departure,
                           destination=destination,
                           all_trains=all_trains)

if __name__ == "__main__":
    app.run(debug=True)