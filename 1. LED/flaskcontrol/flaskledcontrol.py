import RPi.GPIO as GPIO
# pip3 install flask
from flask import Flask, render_template, request

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
pins = {
        3:{
            'name':'Red LED', 
            'state':GPIO.LOW
            },
        5:{
            'name':'Yellow LED',
            'state':GPIO.LOW
            },
        7:{
            'name':'Green LED',
            'state':GPIO.LOW
            }
        }

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

@app.route('/')
def main():
    for pin in pins:
        pins[pin]['state'] = GPIO.input(pin)
    templateData = {'pins':pins}
    return render_template('main.html', **templateData)

@app.route('/<changePin>/<action>')
def action(changePin, action):
    changePin=int(changePin)
    devicename = pins[changePin]['name']

    if action == 'on':
        GPIO.output(changePin, GPIO.HIGH)
    if action == 'off':
        GPIO.output(changePin, GPIO.LOW)
    
    return main()

if __name__ == '__main__':
    app.run(debug=True)