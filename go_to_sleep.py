import vol
from time import sleep
from subprocess import call, check_output
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--minutes_until_mute", help="time (in minutes) to set the volume to mute", type=int)
a = parser.parse_args()
minutes_until_mute = a.minutes_until_mute if a.minutes_until_mute else 30

current_volume = check_output(['osascript', '-e', 'set ovol to output volume of (get volume settings)'])
amount_to_subtract = int(current_volume) / minutes_until_mute

for i in range(minutes_until_mute):
    current_volume = int(current_volume)
    current_volume -= amount_to_subtract
    call(["vol", "out", str(current_volume)])
    sleep(60)
