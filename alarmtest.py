#alarm specs
#time of day
#day of the week

#if weekday number is in list

#list will be of length 7 with boolean values

import pickle, pprint, alarm, time
t = time.localtime()

x = alarm.Alarm(int(time.strftime("%H",t)),int(time.strftime("%M",t)))
#x.setEveryday()
if x.isTrigger(t):
  print("alarm trigger")
print(x.days)
print(x.t)

output = open('data.pkl', 'wb')

pickle.dump(x, output, 3)

output.close()

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

pkl_file.close()

print(data1.days)
print(data1.t)