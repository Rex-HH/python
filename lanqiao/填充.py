s = input()

s = list(s)

ans = 0
p = False
#pre = " "

for i in range(len(s)):
    if s[i] != '?':
        if p:
            if s[i] == s[i-1]:
                ans += 1
                p = False
        else:
            p = True
    else:
        if p:
            s[i] = s[i-1]
            ans += 1
            p = False
        else:
            if i != len(s) - 1:
                s[i] = s[i+1]
                p = True

print(ans)
            
        
