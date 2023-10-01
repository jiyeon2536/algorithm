# the triangle
import sys
inp = sys.stdin.readline
n = int(inp())
triangle = [list(map(int, inp().split())) for _ in range(n)]

# dp 생성 및 초기화
dp = [[0] * n for _ in range(n)]

dp[0][0] = triangle[0][0]

# i 번째 행 j 번째 열은 본인 열 / 본인열 + 1
for i in range(1, n):
    for j in range(i+1):
        if dp[i-1][j-1] <= dp[i-1][j]:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        else:
            dp[i][j] = dp[i-1][j-1] + triangle[i][j]



print(max(dp[n-1]))