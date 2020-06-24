import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # GPIO Numbers instead of board numbers
RELAY_1_GPIO = 23
while True:
    GPIO.setup(RELAY_1_GPIO, GPIO.OUT)  # GPIO Assign mode
    GPIO.output(RELAY_1_GPIO, GPIO.LOW)  # turns off
    GPIO.output(RELAY_1_GPIO, GPIO.HIGH)  # turns on
    time.sleep(2)                         # wait 2 sec
    GPIO.output(RELAY_1_GPIO, GPIO.LOW)  # turns off
    time.sleep(20)                      # wait 20 sec
