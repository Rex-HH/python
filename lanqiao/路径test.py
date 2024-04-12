import heapq
INF = 0x3f3f3f3f3f3f3f3f

class Edge:

    def __init__(self, f, t, w):
        self.f = f
        self.t = t
        self.w = w


class Node:
    def __init__(self, id, dis=INF):
        self.id = id
        self.dis = dis

    def __lt__(self, other):
        self.dis < other.dis

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def lcm(a, b):
    return a // gcd(a, b) * b

def create_map(n):
    e = [[] for _ in range(n + 1)]
    
    for i in range(1, n):
        for j in range(1, 22):
            k = i + j
            
            if k > n:
                break

            w = lcm(i, k)
            #print(w)
            e[i].append(Edge(i, k, w))
            e[k].append(Edge(k, i, w))
            
    return e


e = create_map(23)

print(e)
