def check4():

    for i in [a, b]:
        for j in [c, d]:
            for k in [e, f]:
                if i==j==k:
                    return True
                elif i==j and a+b+c+d-i-j == k:
                    return True
                elif i==k and a+b+e+f-i-k == j:
                    return True
                elif j==k and c+d+e+f-j-k == i:
                    return True
    return False
                    

def check6():
    for i in [a, b]:
        for j in [c, d]:
            for k in [e, f]:
                if i==j or i==k or j==k:
                    return True
                elif i == j+k or j == i+k or k == i+j:
                    return True
    return False



t = int(input())

for _ in range(t):
    a, b, c, d, e, f = map(int, input().split())

    if check4():
        print(4)
    elif check6():
        print(6)
    else:
        print(8)

