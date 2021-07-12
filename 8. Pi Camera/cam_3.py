from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution(1024, 768)
camera.start_preview()
camera.capture('images/testing.jpg', resize=(320, 240))
sleep(3)
camera.stop_preview()