# 부녀회장이 될테야

# dp[a][b] = a층의 b호에 사는 사람 수
import sys

t = int(input())
for tc in range(t):
    k = int(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip())

    dp = [[0] * (n+1) for _ in range(k+1)]
    # dp 초기화
    for i in range(1, n+1):
        dp[0][i] = i

    # i층의 j호에는 i-1 층의 1호부터 j호까지 사람수의 합만큼
    for i in range(1, k+1):
        for j in range(n+1):
            dp[i][j] = sum(dp[i-1][:j+1])

    print(dp[k][n])