# 다리놓기
import sys
input = sys.stdin.readline

t = int(input())
# m개 중에 n개를 뽑는 경우의 수다. - 뽑아서 순서대로 배정하면 됨
for tc in range(t):
    n, m = map(int, input().rstrip().split())
    dp = [[0] * 30 for _ in range(30)]
    # dp[i][0] = i개 중에 0개 뽑는 거 = 1
    # dp[i][1] = i개 중에 1개 뻡ㄴㄴ거 i
    for i in range(30):
        dp[i][0] = 1
        dp[i][1] = i
        dp[i][i] = 1

    for i in range(1, 30):
        for j in range(1, 30):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

    print(dp[m][n])