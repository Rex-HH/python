MAX = int(1e6)
mod = int(1e9+7)
g = [1] * (MAX + 1)

n = int(input())
a = list(map(int, input().split()))

for i in a:
    g[i] += 1
ans = 1
for i in g:
    ans = ans * (i % mod) % mod

print(ans - 1)
