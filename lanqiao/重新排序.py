# 差分+贪心
# 注意下标
n = int(input())
a = list(map(int, input().split()))
Max = len(a) 
cf = [0] * (Max+2) # 差分列表
sum1 = 0
sum2 = 0

m = int(input())

# 下面两个for循环是差分
for _ in range(m):
    l, r = map(int, input().split())
    cf[l] += 1
    cf[r+1] -= 1

for i in range(1, Max+1):
    cf[i] += cf[i-1]
    sum1 += cf[i] * a[i-1] # 顺便把排列前的和计算出来

cf.sort(reverse=True)
a.sort(reverse=True)

# 计算排列后的和
for i in range(Max):
    sum2 += cf[i] * a[i] 

print(sum2 - sum1)
    
