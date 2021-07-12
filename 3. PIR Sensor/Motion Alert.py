from gpiozero import MotionSensor, LED
from time import sleep
from signal import pause
from datetime import datetime

pir = MotionSensor(4)

def motion():
    print('Someone entered, {}'.format(datetime.now().strftime('%I:%M %p')))
def no_motion():
    print('Someone Left, {}'.format(datetime.now().strftime('%I:%M %p')))

print('Starting the sensor')
pir.wait_for_no_motion()
print('Ready')

pir.when_motion = motion
pir.when_no_motion = no_motion

pause()