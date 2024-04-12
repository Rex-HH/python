# 增加一条直线，其与其他直线的交点有k个，则增加的区域有k+1个

def calc(a, b):
    p = set()
    
    for A, B in line:
        if a == A: continue

        x = (b - B) / (A - a) 
        y = a * x + b
        p.add((x, y))

    return len(p) + 1

n = int(input())
ans = 1
line = []

for _ in range(n):
    a, b = map(int, input().split())
    if (a, b) in line: continue

    ans += calc(a, b)
    line.append((a, b))

print(ans)
    
