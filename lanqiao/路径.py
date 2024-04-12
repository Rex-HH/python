import heapq
INF = 0x3f3f3f3f3f3f3f3f

class Edge:
    '''
    边类
    起、终点 及 边权
    '''
    
    def __init__(self, f, t, w):
        self.f = f
        self.t = t
        self.w = w


class Node:
    '''
    节点类
    会包含id和距源点距离
    '''
    
    def __init__(self, id, dis=INF):
        self.id = id
        self.dis = dis

    def __lt__(self, other):
        return self.dis < other.dis

def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def lcm(a, b):
    return a // gcd(a, b) * b

def create_map(n):
    '''
    依题意生成图
    '''
    
    e = [[] for _ in range(n + 1)]
    
    for i in range(1, n):
        for j in range(1, 22):
            k = i + j
            
            if k > n:
                break

            w = lcm(i, k)
            
            e[i].append(Edge(i, k, w))
            e[k].append(Edge(k, i, w))
            
    return e
              
def dijkstra(s, e, n):
    done = [False] * (n + 1)
    hq = []
    dis = [INF] * (n + 1)
    dis[s] = 0
    heapq.heappush(hq, Node(s, dis[s]))
    
    while hq:
        u = heapq.heappop(hq)
        
        if done[u.id]:
            continue
        done[u.id] = True
        
        for v in e[u.id]:
            if done[v.t]:
                continue
            
            if dis[u.id] + v.w < dis[v.t]:
                dis[v.t] = dis[u.id] + v.w
                heapq.heappush(hq, Node(v.t, dis[v.t]))

    return dis

def main():
    n = 2021
    e = create_map(n)
    dis = dijkstra(1, e, n)
    
    print(dis[n])
  
if __name__ == "__main__":
    main()
