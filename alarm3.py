# raspberry pi zero w alarm clock
# snooze and off buttons
# flashing light

import time
import RPi.GPIO as GPIO
import buzzer
import alarm
import pickle

# helper function for setting alarm
def getAlarmValue():
    f = open('alarm.pkl','rb')
    a = pickle.load(f)
#  f = open("alarm.time","r")
#  response = f.read().strip()
    f.close()

    return a

# pin definitions
pwmPin = 18 # Broadcom pin 18 (P1 pin 12)
snoozeButtonPin = 26 # Broadcom pin 26
offButtonPin = 25 # Broadcom pin 25
buzzerPin = 24 # Broadcom pin 24
ledFlasherPin = 18 #Broadcom pin 18

GPIO.setmode(GPIO.BCM)

# set up buttons
GPIO.setup(snoozeButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(offButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# set up alarm buzzer
alarmbuzzer = buzzer.Buzzer(buzzerPin)

# set up led flasher
dc = 100 # duty cycle (0-100) for PWM pin
GPIO.setup(ledFlasherPin, GPIO.OUT) # PWM pin set as output
ledFlasher = GPIO.PWM(ledFlasherPin, 100)  # Initialize PWM on pwmPin 100Hz frequency

# alarm time setting
print("Current time is %s" % time.strftime("%H:%M"))
currAlarm = getAlarmValue()
#newAlarm = currAlarm
#awake = 0

snoozePeriod = 8
#snoozing = 0

try:
    # Loop to continuously check time, buzz the buzzer for the set alarm time
    while True:
        # Continually get's the time as an integer value
        #curr_time = int(time.strftime("%H%M"))

        # update alarm time
        if not(currAlarm.isSnoozing()) and not(currAlarm.isAwake()):
            currAlarm = getAlarmValue()

        # Buzzes the buzzer when the time reaches the set alarm time
        if currAlarm.isTrigger(time.localtime()):
            print("Alarm triggered at %s" % time.strftime("%H:%M"))
            ledFlasher.start(dc)
            alarmbuzzer.buzz(10,0.5)
            time.sleep(0.25)
            alarmbuzzer.buzz(20,0.5)
            time.sleep(0.25)
            #awake = 1

        # Snoozes the alarm for 8 minutes from the current time
        # Only works whilst the alarm is buzzing
        if GPIO.input(snoozeButtonPin) == 0 and currAlarm.isAwake():
            currAlam.snooze(snoozePeriod)
            #alarm += snoozePeriod
            currAlarm.setOff()
            ledFlasher.stop()
            print(alarm)
            print("alarm snoozed")

        # alarm stop button
        elif GPIO.input(offButtonPin) == 0 and currAlarm.isAwake():
            currAlarm.setOff()
            currAlam.snoozeOff()
            ledFlasher.stop()
            currAlarm.rest()
            #alarm = getAlarmValue()
            print(alarm)
            print("alarm reset to next day")
            time.sleep(60)

        # If alarm continues past the set alarm time without being
        # snoozed, the alarm time is changed to the current time.
        # This ensures the alarm buzzes continuously until the
        # snooze button is pressed.
        #elif curr_time != alarm and awake == 1:
        #    alarm = curr_time
        #    alarmbuzzer.buzz(10,0.5)
        #    time.sleep(0.25)
        #    alarmbuzzer.buzz(20,0.5)

finally:
    ledFlasher.stop()
    GPIO.cleanup()
    print("End")
