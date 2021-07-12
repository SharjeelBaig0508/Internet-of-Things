from gpiozero import DistanceSensor
from time import sleep
                            # Echo
ultrasonic = DistanceSensor(4, 3)
                                # Trigger
while 1:
    print(f'Distance: {ultrasonic.distance*100}cm')
    sleep(1)