import argparse
from datetime import datetime
import ipdb
import json
from subprocess import call, check_output
from time import sleep
from urllib import urlopen

import vol

sunset_api_url = "https://api.sunrise-sunset.org/json?lat=38.897834&lng=-77.032992"
sun_data = json.loads(urlopen(sunset_api_url).read())
sunset = sun_data['results']['sunset']
present_time = datetime.now()
sunset_time = datetime.strptime(sunset, '%H:%M:%S %p')  # get time of sunset

# convert time of sunset to today's date
sunset_time_today = datetime(present_time.year,
                             present_time.month,
                             present_time.day,
                             sunset_time.hour + 12,  # assuming sunset is always after noon
                             sunset_time.minute,
                             sunset_time.second)

# time difference between now and sunset
delta = sunset_time_today - present_time
minutes_until_sunset = delta.seconds / 60.0

parser = argparse.ArgumentParser()

parser.add_argument(
    "-d", "--delay",
    help="time (in minutes) until volume begins to lower",
    default=0,
    type=int)

parser.add_argument(
    "-m", "--minutes_until_mute",
    help="time (in minutes) to set the volume to mute",
    default=minutes_until_sunset,
    type=int)
a = parser.parse_args()
sleep(a.delay * 60)
starting_volume = float(check_output(
    ['osascript', '-e',
        'set ovol to output volume of (get volume settings)']))

for i in range(a.minutes_until_mute + 1): 
    percent_of_volume = (-1.0 / (a.minutes_until_mute**2)) * (i**2) + 1
    # quadratic function with maximum at (0, 100%)
    # and crossing at (minutes_until_mute, 0)
    updated_volume = int(starting_volume * percent_of_volume)
    call(["vol", "out", str(updated_volume)])
    call(["vol", "info"])
    sleep(60)

call(["vol", "mute"])  # accounts for rounding errors