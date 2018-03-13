# sleepy_tv
A command line script to gradually lower the volume of my computer so Job doesn't wake me up when he yells "Come on!"

The program takes two arguments:

**-m / --minutes_until_mute**: the length of time before the volume will completely be muted.  It is based off a quadratic formula so it will start lowering slowly and speed up as time progresses

**-d / --delay**: number of minutes before the volume will begin to lower

Note:  If no value is entered for minutes_until_mute, the volume will begin to lower immediately (or after the delay, if provided) and will reach zero at sunset UTC.