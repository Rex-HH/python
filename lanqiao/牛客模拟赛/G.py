e = 1e9 + 7
d = []
for i in range(4):
    d.append(1)

for i in range(4, 101):
    d.append(((d[i-3] % e * 3)%e + (d[i-2] % e * 2)%e + d[i-1] % e) % e)
    #print(d[i])
    #d.append(d[i-3]*3 + d[i-2]*2 + d[i-1])

print(int(d[100]))
