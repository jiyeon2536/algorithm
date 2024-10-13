# def solution(n):
#     dp = {}
#     dp[1] = '1'
#     dp[2] = '2'
#     dp[3] = '4'
    
#     for i in range(4, n + 1):
#         # 몫
#         q = i // 3
#         # 나머지
#         r = i % 3
#         if r == 0:
#             q -= 1
#             r += 3
#         dp[i] = dp[q] + dp[r]
    
#     return dp[n]


def solution(n):
    tmp = n
    dp = {}
    dp[1] = '1'
    dp[2] = '2'
    dp[0] = '4'
    
    answer = ''
    while tmp > 0:
        # 나머지
        r = tmp % 3
        if r == 0:
            tmp -= 3
        answer += dp[r]
        tmp //= 3

    return answer[::-1]