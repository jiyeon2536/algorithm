def solution(n):
    answer = 0

    dp = [0] * (n + 1)
    
    for i in range(n + 1):
        if i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 2
        else:
            dp[i] = dp[i-1] + dp[i-2]
            
    return dp[n] % 1234567