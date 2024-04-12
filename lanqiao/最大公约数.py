t = int(input())

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

for _ in range(t):
    a, b = map(int, input().split())
    print(gcd(a, b))
