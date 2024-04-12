from collections import deque
s = input()
e = input()
l = len(s)

def bfs():
    q = deque()
    q.append((s, 0))
    mset = set()
    mset.add(s)
    move = [1, -1, 2, -2, 3, -3]

    while q:
        b = q.popleft()
        nq = b[0]
        cnt = b[1]
        c = nq.index("*")

        for i in move:
            bq = list(nq)
            a = c + i
            if 0 <= a < l:
                bq[c] = bq[a]
                bq[a] = "*"

            else:
                continue
            bq = ''.join(bq)
            
            if bq == e:
                print(cnt + 1)
                return
            
            if bq not in mset:
               # print(bq, cnt+1)
                mset.add(bq)
                q.append((bq, cnt + 1))

bfs()
