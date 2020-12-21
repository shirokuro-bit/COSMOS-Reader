import time

import RPi.GPIO as GPIO

BeepPin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(BeepPin, GPIO.OUT)

buzzer = GPIO.PWM(BeepPin, 1000)
buzzer.start(50)
print("buzzer 1000 Hz ,duty 50%")
time.sleep(5)

buzzer.ChangeFrequency(500)
print("change 500 Hz")
time.sleep(5)

buzzer.ChangeDutyCycle(10)
print("duty 10 %")
time.sleep(5)

GPIO.cleanup()

# https://physical-computing-lab.net/raspberry-pi-b/4-raspberry-pi-b%E3%81%A7%E3%83%95%E3%82%A3%E3%82%B8%E3%82%AB%E3%83%AB%E3%82%B3%E3%83%B3%E3%83%94%E3%83%A5%E3%83%BC%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%EF%BC%88%E3%83%87%E3%82%B8%E3%82%BF%E3%83%ABpw.html
