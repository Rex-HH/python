# dict = defaultdict(factorty_function)

from collections import defaultdict

Map = defaultdict(int)
n = int(input())
a = list(map(int, input().split()))

for i in a:
    Map[i] += 1

m = a[0]

while True:
    x = Map[m]
    if x % (m+1) == 0:
        Map[m+1] += x // (m+1)
        m += 1
        
    else:
        break
    
print(m)

            
