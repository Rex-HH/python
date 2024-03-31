n = 111111
count = []
a = [True] * (n + 5)
cnt = 0

for i in range(2, n + 1):

    if a[i]:
        count.append(i)
        cnt += 1

    j = 0
    while j < cnt and i * count[j] <= n:

        a[i * count[j]] = False
        if i % count[j] == 0:
            break
        j += 1

ans = 0
for i in range(1111, n+1):
    if a[i] and i % 10 != 1:
        ans += 1

print(ans)
