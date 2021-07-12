from gpiozero import LED
from time import sleep
import datetime
red = LED(2)
yellow = LED(3)
green = LED(4)
while 1:
    red.on()
    sleep(3)
    yellow.on()
    sleep(2)
    red.off()
    yellow.off()
    green.on()
    sleep(3)
    green.off()
    check = datetime.datetime.now()
    with open('timecheck.txt', 'w') as f:
        f.write(check.strftime('%A, %B, %d, %Y - %H:%M:%S %p\n'))