c = input().split()
a = []
for j in c:
    if j == 'A':
        a.append(1)
    elif j == 'J':
        a.append(11)
    elif j == 'Q':
        a.append(12)
    elif j == 'K':
        a.append(13)
    else:
        a.append(int(j))
        
        
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


