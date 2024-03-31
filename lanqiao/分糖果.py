n, x = map(int, input().split())

s = input()

s = sorted(s)
s = ''.join(s)
if s[0] == s[-1]:
    if n % x == 0:
        print(s[0] * (n//x))
    else:
        print(s[0] * (n//x + 1))
elif s[x-1] == s[0]:
    print(s[x-1:])
else:
    print(str(s[x-1]))
