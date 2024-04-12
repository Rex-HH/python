n = 100

dp = [1] * (n + 1)

def calc(x):
    global dp
    i = 2
    while i <= x:
        if x % i == 0:
            while x % i == 0:
                x //= i
                dp[i] += 1

        i += 1
    

if __name__ == "__main__":
    for i in range(2, n + 1):
        calc(i)

    ans = 1
    for i in dp:
        ans *= i

    print(ans)
