from collections import defaultdict

s = input()

dic = defaultdict(int)

for c in s:
    #print(c)
    dic[c] += 1

cnt = 0
ans = ''
for c, v in dic.items():
    #print(c, v)
    if v > cnt:
        ans = c
        cnt = v
    elif v == cnt:
        if c < ans:
            ans = c
            cnt = v

print(ans)
print(cnt)
