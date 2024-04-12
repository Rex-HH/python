t = int(input())

cnt = 0
isprime = [True] * 4001
primes = []

def euler():
    global cnt, isprime, primes
    for i in range(2, 4001):
        if isprime[i]:
            primes.append(i)
            cnt += 1
        j = 0
        while j < cnt and primes[j] * i <= 4000:
            isprime[primes[j] * i] = False
            if i % primes[j] == 0:
                break
            j += 1
            
euler()
def is_pow2(n):
    l = int(n ** 0.5)
    return l * l == n or (l+1) * (l+1) == n

def is_pow3(n):
    l = int(n ** (1/3))
    return l ** 3 == n or (l+1) ** 3 == n



for _ in range(t):

    a = int(input())

    if is_pow2(a) or is_pow3(a):
        print("yes")
        continue
    flag = True
    for i in primes:
        if a % i == 0:
            cnt = 0
            while a % i == 0:
                a //= i
                cnt += 1
            if cnt == 1:
                flag = False
                break
    if flag and (is_pow2(a) or is_pow3(a)):
        print("yes")
    else:
        print("no")
