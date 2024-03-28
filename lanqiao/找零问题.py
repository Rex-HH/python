n = int(input())

m = [100, 50, 20, 5, 1]
ans = [0] * 5

for i in range(5):
    if n == 0:
        break

    num  = n // m[i]
    ans[i] = num
    n -= num * m[i]

for i in range(5):
    print(str(m[i]) + ':' + str(ans[i]))

    
