import pickle, alarm, time

f = open('alarm.pkl','rb')
a = pickle.load(f)
f.close()

currTime = time.localtime()

a.setAlarm(int(time.strftime("%H",currTime)),int(time.strftime("%M",currTime))+1)
a.setEveryday()
print("Alarm set at ", a.t)
print(a.days)

while True:
    print(a.t)
    if a.isTrigger(time.localtime()):
        print("Alarm!")
        a.snooze(1)
    time.sleep(15)
