import bisect
mod = int(1e9+7)
'''
def pown(n):
    ans = 1
    res = 2
    while n:
        #print(n)
        if n & 1:
            ans = ans * res % mod
            

        n >>= 1
        res = res * res % mod

    return ans
'''


#print(pown(5))

n, k = map(int, input().split())

pown = [1] * (n + 1)
res = 1
for i in range(1, n + 1):
    res = res * 2 % mod
    pown[i] = res


a = list(map(int, input().split()))
a.sort()
#print(a)
l = len(a)
i = 0

ans = 0
while i < l and a[i] <= k:
    #print(i)
    limit = k - a[i]
    
    j = bisect.bisect_right(a, limit, i, l)
    #l = bisect.bisect_left(a, limit, i, l)
    #print(a[j], end=' ')
   # print(a[j-1], end=' ')
    #l = j
    if j <= i:
        n = 0
    else:
        n = j - 1 - i

    if n == 0 and 2 * a[i] > k:
        break
        
    ans = (ans + pown[n]) % mod
    i += 1

print(ans)

