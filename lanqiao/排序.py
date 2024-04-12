# abcdefghijklmnopqrstuvwxyz zyxwvut srqp

'''
s = "jonmlkihgfedcba"
cnt = 0
s = list(s)

def maopao(s):
    global cnt
    l = len(s)
    for i in range(l-1):
        k = 0
        for j in range(l - 1 - i):
            if s[j] > s[j+1]:
                cnt += 1
                k += 1
                s[j], s[j+1] = s[j+1], s[j]
        if k == 0:
            break

maopao(s)
print(cnt)
print(s)
'''
print("jonmlkihgfedcba")
