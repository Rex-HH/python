a, b, n = map(int, input().split())

aa = a * 5
bb = b * 2
d = 0

w = n // (aa + bb)
m = n % (aa + bb)
d += w * 7

if m > aa:
    if m - aa - b > 0:
        d += 7
    else:
        d += 6

else:
    if m % a != 0:
        d += (m // a) +  1
    else:
        d += m // a
        
print(d)
