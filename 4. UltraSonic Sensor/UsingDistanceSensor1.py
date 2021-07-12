from gpiozero import DistanceSensor, LED
from time import sleep
from datetime import datetime
from pushbullet import Pushbullet

pb = Pushbullet('o.G0RsjBlhn095imfzaqRZCGBXs00o4BPY')
#print(pb.devices)
dev = pb.get_device('HUAWEI JAT-L29')

#led = LED(17)
ultrasonic = DistanceSensor(4, 3)
                                # Trigger
while 1:
    #led.off()
    dist = ultrasonic.distance*100
    if dist < 90.0:
        print(f'Distance: {dist}cm')
        #led.on()
        dev.push_note('Alert!', 'Someone entered {}cm, {}'.format(round(dist, 2), datetime.now().strftime('%I:%M %p')))
        sleep(5)
    sleep(1)