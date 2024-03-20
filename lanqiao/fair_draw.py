from itertools import *

name = []

n = int(input())
for i in range(n):
    name.append(input())

for element in permutations(name):
    print(' '.join(element))
