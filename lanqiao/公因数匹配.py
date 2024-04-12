from collections import defaultdict

INF = int(1e3 + 1)

def euler(limit):
    """
    欧拉筛
    """
    
    cnt = 0
    primes = []
    isprime = [True] * limit

    for i in range(2, limit):
        if isprime[i]:
            primes.append(i)
            cnt += 1

        j = 0
        while j < cnt and primes[j] * i < limit:
            isprime[primes[j] * i] = False
            if i % primes[j] == 0:
                break
            j += 1

    return primes

def find(k, num, dic, primes):
    """
    将a[k]的位置k记录在质数字典中其包含的质因数的位置(如果该位置还没有值的情况下)
    并且一直更新与a[k]具有相同质因数并且最靠前的位置pos
    如果pos被更新过，返回pos，否则False
    """

    pos = k
    for p in primes:
        
        if p > num:
            break
        
        if num % p == 0:
            
            while num % p == 0:
                num //= p

            if dic[p]:
                pos = min(pos, dic[p])
            else:
                dic[p] = k

    if num > 1:
        if dic[num]:
            pos = min(pos, dic[num])
        else:
            dic[num] = k

    return pos if pos < k else False
            

def main():
    n = int(input())
    a = [0] + list(map(int, input().split()))

    dic = defaultdict(int)
    mini, minj = n+1, n+1
    primes = euler(INF)
    
    for i in range(1, n+1):
        pos = find(i, a[i], dic, primes)
        
        if pos and pos < mini:
            mini = pos
            minj = i
            
    print(mini, minj)
    
if __name__ == '__main__':
    main()
    
