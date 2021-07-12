from gpiozero import MotionSensor, LED
from time import sleep

led = LED(17)
pir = MotionSensor(4)

print('Starting the sensor')
pir.wait_for_no_motion()

while 1:
    print('Ready')
    led.off()
    pir.wait_for_motion()
    led.on()
    print('Motion Detected')
    sleep(3)