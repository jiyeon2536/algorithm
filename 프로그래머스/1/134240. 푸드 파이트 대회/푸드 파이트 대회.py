def solution(food):
    answer = ''
    for i, v in enumerate(food):
        answer += (str(i) * (v // 2))
    
    return answer + '0' + answer[::-1]