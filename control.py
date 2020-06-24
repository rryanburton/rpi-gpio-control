import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # GPIO Numbers instead of board numbers

RELAY_1_GPIO = 23
GPIO.setup(RELAY_1_GPIO, GPIO.OUT)  # GPIO Assign mode
GPIO.output(RELAY_1_GPIO, GPIO.LOW)  # out
GPIO.output(RELAY_1_GPIO, GPIO.HIGH)  # on
time.sleep(0.5)
GPIO.output(RELAY_1_GPIO, GPIO.LOW)  # on
