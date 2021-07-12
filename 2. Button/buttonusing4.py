from gpiozero import Button, LED
from signal import pause

led = LED(17)
btn = Button(4)

btn.when_pressed = led.on
btn.when_released = led.off

pause()