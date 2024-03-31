from datetime import datetime, timedelta
n = input()

dt = datetime.strptime(n, "%Y%m%d").date()

#s = str(next_dt).replace('-','')
dnum = [0, 31, 28, 31, 30, 31, 30, 31 ,31, 30, 31, 30, 31]
#dnum2 = [31, 29, 31, 30, 31, 30, 31 ,31, 30, 31, 30, 31]

def isrun(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def check(year):
    y = str(year)
    if len(y) < 4:
        y = '0' * (4-len(y)) + y
    r = y[::-1]
    #ir = int(r)
    if year == int(n[:4]) and int(r) < int(n[-4:]):
        return False
    m = int(r[:2])
    d = int(r[-2:])
    if m > 12 or m < 1:
        return False
    if d < 1:
        return False
    if m == 2:
        if isrun(year):
            dnum[2] = 29
        else:
            dnum[2] = 28
        if d > dnum[2]:
            return False
    else:
        if d > dnum[m]:
            return False
    return True
    
    
year = int(n[0:4])
while year < 10000:
    if check(year):
        y = str(year)
        if len(y) < 4:
            y = '0' * (4-len(y)) + y
        nd = y + y[::-1]
        nd = datetime.strptime(nd, "%Y%m%d").date()
        print((nd - dt).days)
        break
    year += 1

if year == 10000:
    x = datetime.strptime("99991231", "%Y%m%d").date()
    print((x-dt).days + 3927)
