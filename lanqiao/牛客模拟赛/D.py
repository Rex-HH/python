n , m = map(int, input().split())

data = []
for _ in range(m):
    data.append(list(map(int, input().split())))
out = [[] for _ in range(m)]
for i in range(m):
    for j in range(0,n*3,3):
        if sum(data[i][j:j+3]) <=90:
            out[i].append(True)
        else:
            out[i].append(False)

for i in range(m):
    for j in out[i]:
        if j:
            print(1, end='')
        else:
            print(0, end='')
    print()
