# lotto
# 3 kg, 5 kg
n = int(input())

# dp 배열 만들기
# 초기화
dp = [-1] * 5001

dp[3] = 1
dp[5] = 1

for i in range(3, 5001):
    if dp[i-3] != -1:
        dp[i] = dp[i-3] + 1
    if dp[i-5] != -1:
        dp[i] = dp[i-5] + 1


print(dp[n])