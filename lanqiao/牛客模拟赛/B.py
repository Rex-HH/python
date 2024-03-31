n = 2021041820210418
nq = 44955998
count = []
#print(n)
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        count.append(i)
        if n / i != i:
            count.append(n/i)
ans = 0
"""
for i in count:
    ii = n // i
    for j in count:
        if j > ii:
            break
        if ii % j == 0:
            ans += 1
"""
for i in count:
    for j in count:
        for k in count:
            if i * j * k == n:
                ans += 1
                

print(ans)
