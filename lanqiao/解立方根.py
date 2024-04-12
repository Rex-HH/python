emp = 1e-3

def sqrt3(n):
    left = int(n ** (1/3))
    right = left + 1
    if left ** 3 == n:
        return left
    mid = (left + right) / 2
    while abs(n - (mid ** 3)) > emp:
        temp = mid ** 3
        if temp > n:
            left = mid
        elif temp == n:
            return mid
        else:
            right = mid
        mid = (left + right) / 2

    return mid

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        ans = sqrt3(n)
        print("%.3f" %ans)
    
