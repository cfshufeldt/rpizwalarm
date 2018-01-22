import time, datetime

class Alarm:
    def __init__(self, hour, minute):
        self.days = []
        for i in range(0,7):
            self.days.append(True)
        self.t = datetime.time(int(hour), int(minute))
        self.t0 = self.t
        self.snoozing = False
        self.awake = False

    # turn off alarm
    def setOff(self):
        self.awake = False

    def reset(self):
        self.t = self.t0

    # turn alarm on for weekdays
    def setWeekday(self):
        for i in range(0,5):
            self.days[i] = True
        for i in range(5,7):
            self.days[i] = False

    # turn alarm on for weekends
    def setWeekend(self):
        for i in range(0,5):
            self.days[i] = False
        for i in range(5,7):
            self.days[i] = True

    # turn alarm on everyday
    def setEveryday(self):
        for i in range(0,7):
            self.days[i] = True

    # set alarm using time struct
    def setAlarm(self,hour,minute):
        self.t = datetime.time(hour, minute)
        self.t0 = self.t

    # test if alarm is triggered
    def isTrigger(self,currTime):
        curT = datetime.time(int(time.strftime("%H",currTime)),int(time.strftime("%M",currTime)))
        if (self.days[currTime[6]] and curT == self.t):
            self.awake = True
        return self.awake

    # need to figure out how to rationalize with above function
    def isAwake(self):
        return self.awake

    def snooze(self, snoozePeriod):
        #increment alarm time by snooze period
        self.snoozing = True
        t2 = self.t.minute + snoozePeriod
        self.t = datetime.time(self.t.hour + int(t2/60), t2 % 60)

    def isSnoozing(self):
        return self.snoozing

    def snoozeOff(self):
        self.snoozing = False
