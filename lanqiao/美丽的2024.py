n = 2024

cnt = 0
while n:
    if n & 1:
        cnt += 1

    n >>= 1

print(cnt)
