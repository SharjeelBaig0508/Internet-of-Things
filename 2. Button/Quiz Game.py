from gpiozero import LED, Button
from time import sleep

led = LED(17)
btn1 = Button(3)
btn2 = Button(4)

while 1:
    if btn1.is_pressed:
        print('Player 1 Wins')
        led.on()
        sleep(5)
    if btn2.is_pressed:
        print('Player 2 Wins')
        led.on()
        sleep(5)
    led.off()