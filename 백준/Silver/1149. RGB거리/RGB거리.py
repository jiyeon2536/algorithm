# RGB거리
import sys
input = sys.stdin.readline
n = int(input())
house = [list(map(int, input().rstrip().split())) for _ in range(n)]

# dp 초기화
dp = [[0] * 3 for _ in range(1001)]

dp[0][0] = house[0][0]
dp[0][1] = house[0][1]
dp[0][2] = house[0][2]


# 앞에껀 모두 선택된 상태일때
# i-1 이 r 을 뽑았을 때 R G B
for i in range(1, n):
    dp[i][1] = min(dp[i-1][0] + house[i][1], dp[i-1][2] + house[i][1])
    dp[i][2] = min(dp[i-1][0] + house[i][2], dp[i-1][1] + house[i][2])
    dp[i][0] = min(dp[i-1][1] + house[i][0], dp[i-1][2] + house[i][0])

print(min(dp[n-1]))