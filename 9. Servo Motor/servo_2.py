import RPi.GPIO as GPIO
from time import sleep

slow=0.01
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
pwm=GPIO.PWM(3, 50)
pwm.start(0)
pwm.ChangeDutyCycle(2)
while 1:
    for x in range(0, 180):
        y=1./18.*(x)+2
        pwm.ChangeDutyCycle(y)
        sleep(slow)
    for x in range(180, 0, -1):
        y=1./18.*(x)+2
        pwm.ChangeDutyCycle(y)
        sleep(slow)
pwm.stop()
GPIO.cleanup()