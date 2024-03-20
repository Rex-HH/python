from collections import deque

vip = deque()
nor = deque()

m = int(input())

for _ in range(m):
    
    input_ = input().split()

    if input_[0] == "IN":

        if input_[2] == "N":
            nor.append(input_[1])

        else:
            vip.append(input_[1])

    else:

        if input_[1] == "V":
            vip.popleft()

        else:
            nor.popleft()

for name in vip:
    print(name)

for name in nor:
    print(name)

