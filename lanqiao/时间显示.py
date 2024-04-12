import datetime

t = int(input())
timeStamp = t // 1000
dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
otherStyleTime = dateArray.strftime("%H:%M:%S")
print(otherStyleTime)
