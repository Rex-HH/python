n = int(input())

a = [True] * (n + 5)
count = []

cnt = 0

for i in range(2, n):

    if a[i]:
        cnt += 1
        count.append(i)
        print(i, end=' ')

    j = 0
    while j<cnt and i * count[j] < n:

        a[i*count[j]] = False
        if i % count[j] == 0:
            break
        j += 1

print()
print(cnt)
