# 이항 계수 1

# nCk를 구하는 프로그램

n, k = map(int, input().split())

dp = [[0] * (n+1) for _ in range(n+1)]

# n개 중에 k개를 뽑기 . 초기화 해준다
# dp[i][i] = 1   -- i 개 중에 i개를 뽑는 경우의 수
# dp[i][1] = i   -- i 개 중에 1개를 뽑는 경우의 수
# dp[i][0] = 1  -- 0개를 뽑는 경우의 수 - 1개

for i in range(1, n+1):
    dp[i][0] = 1
    dp[i][i] = 1
    dp[i][1] = i

for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i][j] == 0:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

print(dp[n][k])
