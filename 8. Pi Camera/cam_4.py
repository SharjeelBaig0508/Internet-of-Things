from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution(1024, 768)
camera.start_preview()
for i in range(5):
    camera.capture(f'images/timing.{i}.jpg')
    sleep(2)
camera.stop_preview()