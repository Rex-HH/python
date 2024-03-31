# 只要有非1的最大公约数 ，就会经过交叉点
#

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

t = int(input())

for _ in range(t):
    
    x, y = map(int, input().split())

    
    if x == 0 and y == 0:
        print(0)
        continue
        
    if x == 1 or y == 1:
        print(1)
        continue
    
    if x == 0 or y == 0:
        print(2)
        continue
    
    g = gcd(x, y)
    if g == 1:
        print(1)
    else:
        print(2)

    
