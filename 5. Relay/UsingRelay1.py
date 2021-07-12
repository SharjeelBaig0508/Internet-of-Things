from gpiozero import OutputDevice
from time import sleep

relay1 = OutputDevice(4, active_high = False, initial_value = True)
relay2 = OutputDevice(4, active_high = False, initial_value = True)

while 1:
    relay1.on()
    sleep(2)
    relay2.on()
    sleep(2)
    relay1.off()
    sleep(2)
    relay2.off()
    sleep(2)