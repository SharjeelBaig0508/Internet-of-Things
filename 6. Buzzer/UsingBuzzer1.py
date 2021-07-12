import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

while 1:
    GPIO.output(18, GPIO.HIGH)
    sleep(2)
    GPIO.output(18, GPIO.LOW)
    sleep(2)