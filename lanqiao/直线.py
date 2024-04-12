'''
docker = set()

for x1 in range(20):
    for x2 in range(20):
        if x1 == x2:
            continue
        for y1 in range(21):
            for y2 in range(21):
                k = (y2 - y1) / (x2 - x1)
                b = (x2*y1 - x1*y2) / (x2 - x1)
                if (k, b) not in docker:
                    docker.add((k, b))

l = len(docker)

print(l + 20)
'''
print(40257)         
                
