MOD = 998244353

a, b = map(int, input().split())

if a == 1:
    print(0)
    exit(0)

def qpow(x, n):
    res = 1
    while n:
        if n & 1:
            res = res * x % MOD
        x = x * x % MOD
        n >>= 1
    return res

def euler(x):
    res = x
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            while x % i == 0:
                x //= i
            res = res // i * (i - 1)
    if x > 1:
        res = res // x * (x - 1)
    return res

print(qpow(a, b - 1) * euler(a) % MOD)
