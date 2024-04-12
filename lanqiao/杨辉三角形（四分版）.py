n = int(input())


ans = 3
yh = [0, 1]

if n == 1:
    print(1)

row = 3
flag = False
while not flag:
    half = (row + 1) // 2
    yh.append(yh[half-1] + 1)
    for i in range(half-1, 1, -1):
        yh[i] = yh[i] + yh[i-1]

    for i in range(2, half + 1):
        if yh[i] == n:
            ans += i
            flag = True
            break
    if not flag:
        ans += row
        row += 1

print(ans)
         




