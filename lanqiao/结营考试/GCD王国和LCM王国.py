def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def lcm(a, b):
    return a // gcd(a, b) * b

s = set()

n = int(input())

a = list(map(int, input().split()))

for i in range(n-1):
    for j in range(i + 1, n):
        s.add(lcm(a[i], a[j]))
ans = a[n-1]
for k in s:
    ans = gcd(ans, k)


print(ans)
