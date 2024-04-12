'''
a = [2021] * 10

ans = 0
flag = True
while flag:
    ans += 1
    n = ans
    while n:
        mod = n % 10
        if a[mod] == 0:
            flag = False
            break
        else:
            a[mod] -= 1
            n //= 10

    #print(ans)

print(ans-1)
'''
print(3181)
