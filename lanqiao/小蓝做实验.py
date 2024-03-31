"""
with open("./primes.txt", 'r' , encoding='utf-8') as fr:
     data = fr.read().split()
#print(data[:10])

data1 = [int(i) for i in data if len(i) <= 8]
data2 = [int(i) for i in data if len(i) >8]

cnt = 0
maxn = 10 ** 8 + 1
dp = [True] * (maxn)
count = []

for i in range(2, maxn):
    if dp[i]: 
        count.append(i)
        cnt += 1

    j = 0
    while j < cnt and i * count[j] < maxn:
        dp[i * count[j]] = False

        if i % count[j] == 0:
            break
        j += 1


ans = 0
for i in data1:
    if dp[i]:
        ans += 1

for i in data2:
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            ans -= 1
            break

    ans += 1

print(ans)
"""
print(342693)
