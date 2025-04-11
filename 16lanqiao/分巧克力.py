n, k = map(int, input().split())

m = []
for _ in range(n):
    
    m.append(list(map(int, input().split())))




def pd(l):
    cnt = 0
    for i in range(n):
        cnt += (m[i][0] // l) * (m[i][1] // l)

    if cnt >= k:
        return True
    
    return False


l, r = 1, 0
for i in range(n):
    r = max(r, max(m[i]))

while l < r:
    mid = (l + r + 1) >> 1
    if pd(mid):
        l = mid
    else:
        r = mid - 1

print(l)



