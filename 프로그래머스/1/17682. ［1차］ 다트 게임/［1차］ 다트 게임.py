def solution(dartResult):
    total = 0
    bonus = {'S' : 1, 'D': 2, 'T': 3}
    
    prev_score = 0
    cur_score = 0
    cur = ''
    
    for d in dartResult:
        # 숫자인 경우 
        if d.isdigit():
            cur += d
            if cur != '10':
                total += prev_score
            prev_score = cur_score
        # 보너스인 경우
        elif d in bonus:
            cur_score = int(cur) ** bonus[d]
            cur = ''
        # 옵션인 경우
        else:
            if d == '*':
                prev_score *= 2
                cur_score *= 2
            elif d == '#':
                cur_score *= -1

        
    return total + prev_score + cur_score