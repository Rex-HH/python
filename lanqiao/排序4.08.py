n = int(input())

a = list(map(int, input().split()))

def partition(a, l, r):
    i, j = l, r
    while i < j:
        while i < j and a[j] >= a[l]:
            j -= 1
        while i < j and a[i] <= a[l]:
            i += 1
        a[i], a[j] = a[j], a[i]

    a[l], a[i] = a[i], a[l]
    return i
def quicksort(a, l, r):

    if l >= r: return
    i = partition(a, l, r)
    quicksort(a, l, i-1)
    quicksort(a, i+1, r)


quicksort(a, 0, len(a)-1)
for i in range(len(a)):
    print(a[i] , end=' ')
print()

for i in range(len(a)-1, -1, -1):
    print(a[i], end=' ')
    

    
        
