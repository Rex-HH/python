from collections import defaultdict
k = int(input())
s = list(input())
l = len(s)
m = []
step = l // k 
for i in range(step):
    m.append(s[i::step])

ans = 0
for a in m:
    dic = defaultdict(int)
    for i in a:
        dic[i] += 1
    values = dic.values()
    #print(values)
    ans += k - max(values)

print(ans)
