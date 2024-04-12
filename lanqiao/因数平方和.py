mod = int(1e9 + 7)
n = int(input())

def calc(x):
    return x * (x + 1) * (2 * x + 1) // 6

ans = 0
i = 1
while i <= n:
    x = n // i
    y = n // x
    ans += (calc(y) - calc(i - 1)) * x
    i = y + 1

print(int(ans % mod))
