from gpiozero import OutputDevice
from time import sleep

relay = OutputDevice(21, active_high = False, initial_value = True)

while 1:
    relay.on()
    sleep(2)
    relay.off()
    sleep(2)