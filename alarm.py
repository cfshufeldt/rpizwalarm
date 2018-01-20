import time, datetime

class Alarm:
  def __init__(self, hour, minute):
    self.days = []
    for i in range(0,7):
      self.days.append(True)
    self.t = datetime.time(int(hour), int(minute))

  # turn off alarm
  def setOff(self):
    for i in range(0,7):
      self.days[i] = False    

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
  
  # test if alarm is triggered
  def isTrigger(self,currTime):
    curT = datetime.time(int(time.strftime("%H",currTime)),int(time.strftime("%M",currTime)))
    return (self.days[currTime[6]] and curT == self.t)