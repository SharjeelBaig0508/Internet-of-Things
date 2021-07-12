import RPi.GPIO as GPIO
import time

relay_channel = [17, 23]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(relay_channel, GPIO.OUT, initial=GPIO.LOW)

def main():
    while 1:
        for channel in relay_channel:
            GPIO.output(channel, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(channel, GPIO.LOW)
            time.sleep(2)

def destroy():
    GPIO.setip(relay_channel, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()