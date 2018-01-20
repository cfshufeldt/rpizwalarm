import alarm, pickle

h = input("Enter hour: ")
m = input("Enter minute: ")

a = alarm.Alarm(h,m)
a.setWeekday()

print(a.t)
print(a.days)

output = open('alarm.pkl', 'wb')

pickle.dump(a, output, 3)

output.close()