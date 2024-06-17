def solution(num_list):
    answer = 0
    for n in num_list:
        for i in range(5):
            if 2**i <= n < 2**(i+1):
                answer += i
    return answer