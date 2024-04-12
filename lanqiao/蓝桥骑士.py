import bisect

n = int(input())
a = list(map(int, input().split()))

ng = 0
for i in a:
    j = bisect.bisect_left(a, i, 0, ng)
    a[j] = i
    if j == ng:
        ng += 1

print(ng)
    
