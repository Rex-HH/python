from decimal import Decimal
n, S = map(int,input().split())
a = list(map(int, input().split()))
avg = S / n
n1 = n
m = avg
ans = 0
a.sort()
for i in a:
    if i < m:
        ans += (i - avg) ** 2
        S -= i
    else:
        ans += ((m - avg) ** 2) * n1
        break
    n1 -= 1
    if n1 != 0:
        m = S / n1
res = (ans / n) ** 0.5
res = str(res)
res = Decimal(res).quantize(Decimal('0.0001'), rounding = 'ROUND_HALF_UP')

print(res)
    
    
