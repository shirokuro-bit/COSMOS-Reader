import time

import RPi.GPIO as GPIO

BeepPin = 11


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BeepPin, GPIO.OUT)
    GPIO.output(BeepPin, GPIO.HIGH)


def loop():
    while True:
        GPIO.output(BeepPin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(BeepPin, GPIO.HIGH)
        time.sleep(0.1)


def destroy():
    GPIO.output(BeepPin, GPIO.HIGH)
    GPIO.cleanup()


if _name_ == '_name_':
    print('Please Ctrl+C to end the program...')
    setup()

    try:
        loop()
    except KeyboardInterrupt:
        destroy()

# https://www.fabshop.jp/lesson2-buzzer/
