#!/usr/bin/python3
##A simple webserver to view raw temperature logs for the day

from flask import Flask
import os

# Create a flask object called app
app = Flask(__name__)
home_dir = os.path.expanduser("~")

# Run the following code whenever someone goes to the URL in app route (in this case it is /)
@app.route("/")
def todays_logs():
    with open(f'{home_dir}/RPI-Temp-Sensor/DS18B_email_alert/Logging/logs/freezer01_temperature.log') as f:
        todays_temperatures = f.read()
    return todays_temperatures

if __name__ == "__main__":
    app.run(host=0.0.0.0, port=80, debug=True)
