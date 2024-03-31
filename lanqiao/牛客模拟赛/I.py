from datetime import datetime, timedelta
n = input()

dt = datetime.strptime(n, "%Y%m%d").date()
next_dt = dt
delta = timedelta(days=1)

while True:
    next_dt += delta
    s = str(next_dt).replace('-','')
    if s == s[::-1]:
        print((next_dt - dt).days)
        break

