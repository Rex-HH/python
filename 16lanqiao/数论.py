print(pow(2, 10, 1000))


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a / gcd(a, b) * b


print(gcd(15, 81))
print(gcd(-17, 289))
print(gcd(-6, -15))
