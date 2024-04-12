data = [0 for i in range(25)]
cnt= 0

def fib(n):
    global cnt
    cnt += 1
    if data[n] != 0:
        return data[n]
    if n == 1 or n == 2:
        data[n] = 1
        return data[n]

    data[n] = fib(n-1) + fib(n-2)
    return data[n]

print(fib(20))
print(cnt)
