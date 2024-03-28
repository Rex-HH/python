b, p, k = map(int, input().split())
s = 1
b %= k
while p:

    if p & 1:
        s = (s * b) % k

    b =  (b*b) % k
    p >>= 1

print(s)
