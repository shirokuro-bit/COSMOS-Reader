#!/usr/bin/env python
import time

# import RPi.GPIO as GPIO

# GPIO.setmode(GPIO.BCM)  # GPIO番号で指定


class LED:
    def enter(self):
        # GPIO.setup(25, GPIO.OUT)
        #
        # GPIO.output(25, GPIO.HIGH)
        # time.sleep(2)
        #
        # GPIO.cleanup()
        print('退室')

    def exit(self):
        # GPIO.setup(26, GPIO.OUT)
        #
        # GPIO.output(26, GPIO.HIGH)
        # time.sleep(2)
        #
        # GPIO.cleanup()
        print('入室')

    def Sing_Up(self):
        # GPIO.setup(25, GPIO.OUT)
        # GPIO.setup(26, GPIO.OUT)
        #
        # GPIO.output(25, GPIO.HIGH)
        # GPIO.output(26, GPIO.HIGH)
        # time.sleep(2)
        #
        # GPIO.cleanup()
        print('新規登録')
