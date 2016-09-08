import vol
from time import sleep
from subprocess import call, check_output
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-d", "--delay",
    help="time (in minutes) until volume begins to lower",
    default=0,
    type=int)
parser.add_argument(
    "-m", "--minutes_until_mute",
    help="time (in minutes) to set the volume to mute",
    default=30,
    type=int)
a = parser.parse_args()
sleep(a.delay * 60)
current_volume = float(check_output(
    ['osascript', '-e',
        'set ovol to output volume of (get volume settings)']))

for i in range(a.minutes_until_mute + 1):
    percent_of_volume = (-1.0 / (a.minutes_until_mute**2)) * (i**2) + 1
    # quadratic function with maximum at (0, 100%)
    # and crossing at (minutes_until_mute, 0)
    new_volume = int(current_volume * percent_of_volume)
    call(["vol", "out", str(new_volume)])
    call(["vol", "info"])
    sleep(60)

call(["vol", "mute"])  # accounts for rounding errors
