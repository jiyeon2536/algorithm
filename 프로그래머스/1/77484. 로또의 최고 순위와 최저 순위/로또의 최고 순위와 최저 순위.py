def solution(lottos, win_nums):
    answer = [0, 0]
    cor = 0
    
    for l in lottos:
        if l in win_nums:
            cor += 1
        answer[1] = min(7 - cor, 6)
    
    cor += lottos.count(0)
    answer[0] = min(7 - cor, 6)
    
    return answer