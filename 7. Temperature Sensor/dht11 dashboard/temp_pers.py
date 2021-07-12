import adafruit_dht
from ISStreamer.Streamer import Streamer
import time
import board

# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Temp Sensor"
BUCKET_NAME = "Tempurature Dashboard"
BUCKET_KEY = "Q6NP3Q9KUR73"
ACCESS_KEY = "ist_k9oSjvI1VWANliswzB630QJoseCoIyh1"
MINUTES_BETWEEN_READS = 1
METRIC_UNITS = True
# ---------------------------------

dhtSensor = adafruit_dht.DHT11(board.D3) #GPIO 3
streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

while True:
    try:
        humidity = dhtSensor.humidity
        temp_c = dhtSensor.temperature
    except RuntimeError:
        print("RuntimeError, trying again...")
        continue        
    if METRIC_UNITS:
        streamer.log(SENSOR_LOCATION_NAME + " Temperature(C)", temp_c)
    else:
        temp_f = format(temp_c * 9.0 / 5.0 + 32.0, ".2f")
        streamer.log(SENSOR_LOCATION_NAME + " Temperature(F)", temp_f)
    humidity = format(humidity,".2f")
    streamer.log(SENSOR_LOCATION_NAME + " Humidity(%)", humidity)
    streamer.flush()
    time.sleep(60*MINUTES_BETWEEN_READS)