a, b = map(int, input().split())

ans = 0
res = a
for i in range(a, b + 1):
    s = str(i)
    temp = 0
    for j in s:
        if j == '0' or j == '6' or j == '9':
            temp += 1
        elif j == '8':
            temp += 2

    if temp > ans:
        ans = temp
        res = i

print(res)
        
