'''
n = 2021041820210418

a = []
i = 1
while i * i < n:
    if n % i == 0:
        a.append(i)
        a.append(n // i)

    i += 1
a.sort()
ans = 0
for x in a:
    for y in a:
        if x * y > n:
            break
        for z in a:
            if x * y * z > n:
                break
            if x * y * z == n:
                ans += 1

print(ans)
'''
print(2430)
