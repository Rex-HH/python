dic = {'A':1, 'K':13, 'Q':12, 'J':11,
       '10':10, '9':9, '8':8, '7':7,
       '6':6, '5':5, '4':4, '3':3,
       '2':2}
def trsti(s):
    return dic[s]
a = list(map(trsti, input().split()))
ans = [[] for i in range(10)]
ans[0].append(a[0])
for i in range(1, 6):
    for j in range(len(ans[i-1])):
        ans[i].append(ans[i-1][j] + a[i])
        ans[i].append(ans[i-1][j] - a[i])
        ans[i].append(ans[i-1][j] * a[i])
        ans[i].append(ans[i-1][j] // a[i])
yes = 0
for j in range(len(ans[5])):
    if ans[5][j] == 42:
        yes = 1
        break
if yes == 0:
    print("NO")
else:
    print("YES")


