mod = [0, 0, 1, 2, 1, 4, 5, 4, 1, 2, 9, 0, 5, 10,
       11, 14, 9, 0, 11, 18, 9, 11, 11, 15, 17, 9,
       23, 20, 25, 16, 29, 27, 25, 11, 17, 4, 29, 22,
       37, 23, 9, 1, 11, 11, 33, 29, 15, 5, 41, 46]

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def lcm(a, b):
    return a // gcd(a, b) * b

n = 1
step = 1

for i in range(2, 50):
    while n % i != mod[i]:
        n += step
    step = lcm(step, i)

print(n)
