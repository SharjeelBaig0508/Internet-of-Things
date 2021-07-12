from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution(1024, 768)
camera.start_preview()
sleep(3)
camera.stop_preview()