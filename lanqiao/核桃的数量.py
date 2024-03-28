a, b, c = map(int, input().split())

def gcd(a, b):
    return a if b==0 else gcd(b, a%b)

def lcm(a, b):
    return a // gcd(a, b) * b

print(lcm(a, lcm(b, c)))
