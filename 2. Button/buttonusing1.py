from gpiozero import Button
btn = Button(4)
while 1:
    btn.wait_for_press()
    print('Button Pressed')
    btn.wait_for_release()
    print('Button Released')