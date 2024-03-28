import sys
import os
import heapq

INF = 0x3f3f3f3f3f3f3f3f


class Node:

    def __init__(self, s, dis=INF):
        self.s = s
        self.dis = dis

    def __lt__(self, other):
        return self.dis < other.dis

class Edge:

    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

n, m = map(int, input().split())
e = [[] for _ in range(n + 5)]


for _ in range(m):
    u, v, w = map(int, input().split())
    e[u].append(Edge(u, v, w))

def dijkstra(no):
    hq = []   
    done = [0] * (n + 5)
    dis = [INF] * (n + 5)
    
    dis[no] = 0
    heapq.heappush(hq, Node(no, dis[no]))
    

    while hq:
        u = heapq.heappop(hq)
        s = u.s
        
        if done[s] == 1:
            continue
            
        done[s] = 1
        
        for y in e[s]:
            to = y.v
            if done[to] == 1:
                continue

            if u.dis + y.w < dis[to]:
                dis[to] = u.dis + y.w
                heapq.heappush(hq, Node(to, dis[to]))
                
    for i in range(1, n+1):
        
        if dis[i] >= INF:
            print(-1, end=' ')
            
        else:
            print(dis[i], end=' ')

dijkstra(1)
            

            

            

        

