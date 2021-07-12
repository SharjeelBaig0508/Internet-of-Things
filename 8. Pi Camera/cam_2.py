from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution(1024, 768)
camera.start_preview()
camera.capture('/home/pi/Internet of Things/8. Pi Camera/images/abc.jpg')
sleep(3)
camera.stop_preview()