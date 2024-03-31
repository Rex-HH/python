n, m = map(int, input().split())

data = []

for _ in range(m):
    data.append(input())

for i in range(m):
    cnt = 0
    for j in range(n):
        if data[i][j] == '1':
            cnt += 1
            
        elif cnt != 0 and data[i][j] == '0':
            #print(cnt)
            y = i + 0.5
            x = j  - 0.5 - ((cnt-1) / 2) # (j -1  + 0.5 + j -1 - cnt + 0.5) / 2
            print(y, x, cnt, 1)
            cnt = 0
            
        if cnt != 0 and j == n-1:
            y = i + 0.5
            x = j - (cnt-1) / 2 + 0.5
            print(y, x, cnt, 1)

        

