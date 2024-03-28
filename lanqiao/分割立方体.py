n = int(input())

if n == 1:
    print(0)

else:
    totol = (n*n*n) * ((n*n*n)-1) // 2

    l = n - 2
    m = l * l
    t = m * l

    cnt = l * 4 * 12 + m * 5 * 6 + t * 6 + 8 * 3

    print(totol - (cnt//2))


