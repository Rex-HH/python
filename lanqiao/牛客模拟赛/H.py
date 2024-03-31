from datetime import datetime, timedelta, date

dt = date(2025,1,13)

#print(dt)
delta = timedelta(days=1)

enddt = date(2276,12,31)

ans = 0
while dt < enddt:
    if dt.day == 13 and dt.weekday() == 6:
        ans += 1
    dt += delta

print(ans)
