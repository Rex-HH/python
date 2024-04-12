n = int(input())

q = []

for _ in range(n):
    q.append(list(map(int, input().split())))

q.sort(key=lambda x: sum(x))

ans = q[0][0] + q[0][1]
res = sum(q[0])


for i in range(1, n):
    temp = res + q[i][0] + q[i][1]
    ans += temp
    res += sum(q[i])

print(ans)
