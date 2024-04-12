import datetime

s = datetime.datetime(2000,1,1)
e = datetime.datetime(2020,10,1)

delta = datetime.timedelta(days=1)

ans = 0
while s <= e:
    if s.weekday() == 0 or s.day == 1:
        ans += 2
    else:
        ans += 1
    s += delta

print(ans)
