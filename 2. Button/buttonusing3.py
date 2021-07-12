from gpiozero import Button
from signal import pause
btn = Button(4)
def say_hello(button, text=''):
    print(str(button.pin.number))
def say_goodbye():
    print('Goodbye')

btn.when_pressed = say_hello
btn.when_released = say_goodbye

pause()