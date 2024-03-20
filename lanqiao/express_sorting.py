n = int(input())

city = []
express = [[] for _ in range(1000)]

def _find(c):
    for i in range(len(city)):
        
        if city[i] == c:
            #print(type(i))
            return i
        
    return -1

for _ in range(n):

    input_ = input().split()
    flag = _find(input_[1])
    #print(type(flag))

    if flag == -1:
        express[len(city)].append(input_[0])
        city.append(input_[1])

    else:
        express[flag].append(input_[0])

for i in range(len(city)):

    print(city[i], len(express[i]), sep=' ')
    
    for num in express[i]:
        print(num)
