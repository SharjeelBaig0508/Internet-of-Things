from gpiozero import MotionSensor, LED
from time import sleep
from signal import pause
from datetime import datetime
from pushbullet import Pushbullet

pb = Pushbullet('o.G0RsjBlhn095imfzaqRZCGBXs00o4BPY')
#print(pb.devices)
dev = pb.get_device('HUAWEI JAT-L29')

led = LED(17)
pir = MotionSensor(4)

def motion():
    led.on()
    dev.push_note('Alert!', 'Someone entered, {}'.format(datetime.now().strftime('%I:%M %p')))
def no_motion():
    led.off()

print('Starting the sensor')
pir.wait_for_no_motion()
print('Ready')

pir.when_motion = motion
pir.when_no_motion = no_motion

pause()