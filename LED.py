#!/usr/bin/env python
import time

import RPi.GPIO as GPIO


class LED:
    def enter(self):
        GPIO.setmode(GPIO.BCM)  # GPIO番号で指定
        GPIO.setup(4, GPIO.OUT)

        GPIO.output(4, GPIO.HIGH)
        time.sleep(2)

        GPIO.cleanup()
        print('退室')

    def exit(self):
        GPIO.setmode(GPIO.BCM)  # GPIO番号で指定
        GPIO.setup(17, GPIO.OUT)

        GPIO.output(17, GPIO.HIGH)
        time.sleep(2)

        GPIO.cleanup()
        print('入室')

    def Sing_Up(self):
        GPIO.setmode(GPIO.BCM)  # GPIO番号で指定
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(17, GPIO.OUT)

        GPIO.output(4, GPIO.HIGH)
        GPIO.output(17, GPIO.HIGH)
        time.sleep(2)

        GPIO.cleanup()
        print('新規登録')
