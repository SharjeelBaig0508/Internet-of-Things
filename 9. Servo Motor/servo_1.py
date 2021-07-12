import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
pwm=GPIO.PWM(18, 50)
pwn.start(0)
pwm.ChangeDutyCycle(1)