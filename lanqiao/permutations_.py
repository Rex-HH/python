from itertools import *

s = ['a', 'b', 'c']

for element in permutations(s, 2):

    a= ''.join(element)
    print(a)
