s = input()

r = len(s) - 1
l = 0

while l < r:
    if s[l] != s[r]:
        #print(s[l], s[r])
        print("N")
        break

    l += 1
    r -= 1

if l >= r:
    print('Y')
    
