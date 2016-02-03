import vol
from time import sleep
from subprocess import call, check_output
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--minutes_until_mute", help="time (in minutes) to set the volume to mute", type=int)
a = parser.parse_args()
minutes_until_mute = a.minutes_until_mute if a.minutes_until_mute else 30

current_volume = check_output(['osascript', '-e', 'set ovol to output volume of (get volume settings)'])

for i in range(minutes_until_mute):
    percent_of_volume = (-1.0/(minutes_until_mute**2))*(i**2) + 1
    new_volume = int(float(current_volume) * percent_of_volume)
    print "{}% of {} at minute {} is {}".format(percent_of_volume, current_volume, i, new_volume)

    call(["vol", "out", str(new_volume)])
    call(["vol", "info"])
    sleep(60)

call(["vol", "mute"]) #for the likely chance that I stupidly manually increased the volume