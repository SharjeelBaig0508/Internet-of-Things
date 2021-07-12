from gpiozero import LED
from time import sleep
led = LED(4)
try:
    while 1:
        led.on()
        print("Led On")
        sleep(5)
        led.off()
        print("Led Off")
        sleep(5)
except KeyboardInterrupt:
    print("Program Exiting")