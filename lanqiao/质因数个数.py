n = int(input())

def euler(limit):
    cnt = 0
    primes = []
    isprime = [True] * limit
    for i in range(2, limit):
        if isprime[i]:
            primes.append(i)
            #print(i, end=' ')
            cnt += 1

        j = 0
        while j < cnt and primes[j] * i < limit:
            isprime[primes[j] * i] = False
            if i % primes[j] == 0:
                break
            j += 1
    return primes

ans = 0

primes = euler(n+1)
for i in primes:
    if i > n:
        break
    if n % i == 0:
        while n % i == 0:
            n //= i
        ans += 1

print(ans if n == 1 else ans + 1)
