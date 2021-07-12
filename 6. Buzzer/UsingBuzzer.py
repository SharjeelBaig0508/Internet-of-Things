from gpiozero import Buzzer
from time import sleep

sound = Buzzer(4)

while 1:
    sound.on()
    sleep(2)
    sound.off()
    sleep(2)