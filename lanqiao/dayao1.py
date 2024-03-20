n, m = map(int, input().split())

a = [0] + list(map(int, input().split()))

fsum = [0]
for i in range(1, n+1):
    fsum.append(a[i] + fsum[i-1])

for _ in range(m):
    s, e = map(int, input().split())

    print(fsum[e] - fsum[s-1])


"""
for _ in range(m):
    input_ = list(map(int, input().split()))

    a[input_[0]] += input_[2]
    a[input_[1]+1] -= input_[2]

for i in range(1, n+1):
    a[i] = a[i] + a[i-1]

print(sum(a[1:n+1]))
"""
  
