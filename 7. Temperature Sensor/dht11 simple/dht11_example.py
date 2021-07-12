import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

# read data using Pin GPIO21 
instance = dht11.DHT11(pin=21)

while True:
    result = instance.read()
    if result.is_valid():
        print(f"Temp: {result.temperature}*C, Humid: {result.humidity}%")
    time.sleep(1)
