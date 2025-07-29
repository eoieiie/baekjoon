import sys

def solve(n: int) -> int:
    if n <= 1:
        return 0

    dp = [0] * (n + 1)          # dp[1] = 0 자동
    for x in range(2, n + 1):
        m = dp[x - 1] + 1       # -1 연산
        if x % 2 == 0:          # /2 가능?
            m = min(m, dp[x // 2] + 1)
        if x % 3 == 0:          # /3 가능?
            m = min(m, dp[x // 3] + 1)
        dp[x] = m
    return dp[n]

print(solve(int(sys.stdin.readline())))
