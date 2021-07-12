from gpiozero import Button
btn = Button(4)
while 1:
    if btn.is_pressed:
        print('Button Pressed')
    else:
        print('Released')