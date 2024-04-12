s = input()

a = []
l = len(s)
i = 0
while i < l:
    if s[i] == 'L':
        a.append('L')
        while i + 1 < l and s[i+1] == 'L':
            i += 1
    else:
        a.append('Q')

    i += 1

ans = ''.join(a)
print(ans)
