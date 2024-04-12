INF = 0x3f3f3f3f3f3f3f3f
N = 405
dp = [[INF for i in range(N)] for j in range(N)]

def floyd(n):
    global dp
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                dp[j][i] = dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


def main():
    n, m, q = map(int, input().split())

    for _ in range(m):
        u, v, w = map(int, input().split())
        dp[u][v] = dp[v][u] = min(dp[u][v], w)

    floyd(n)

    for _ in range(q):
        st, ed = map(int, input().split())
        if dp[st][ed] == INF:
            print("-1")
        elif st == ed:
            print("0")
        else:
            print(dp[st][ed])
            
if __name__ == "__main__":
    main()
