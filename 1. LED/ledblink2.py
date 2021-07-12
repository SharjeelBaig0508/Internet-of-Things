from gpiozero import LED
led = LED(4)
led.blink(1, 5, 10)