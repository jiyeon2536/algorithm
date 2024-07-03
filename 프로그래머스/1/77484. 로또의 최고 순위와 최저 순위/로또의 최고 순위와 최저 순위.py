def solution(lottos, win_nums):
    answer = [0, 0]

    win_dict = {}
    for w in win_nums:
        win_dict[w] = 0
    
    unknown = 0
    for l in lottos:
        if l in win_dict:
            win_dict[l] = 1
        if l == 0:
            unknown += 1
    
    answer[1] = min(7 - sum(win_dict.values()), 6)
    answer[0] = min(7 - (sum(win_dict.values()) + unknown), 6)
    
    return answer