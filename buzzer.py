# ~/raspberrypi/buzzer.py
# Script forked from Simon Monk's 'Pi Starter Kit' repo
# https://github.com/simonmonk/pi_starter_kit

import RPi.GPIO as GPIO
import time

class Buzzer:

	def __init__(self, pin):
		GPIO.setmode(GPIO.BCM)
		self.buzzer_pin = pin
		GPIO.setup(self.buzzer_pin, GPIO.OUT)

	def buzz(self, pitch, duration):
		period = 1.0 / pitch
		delay = period / 2
		cycles = int(duration * pitch)
		for i in range(cycles):
			GPIO.output(self.buzzer_pin, True)
			time.sleep(delay)
			GPIO.output(self.buzzer_pin, False)
			time.sleep(delay)
