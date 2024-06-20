def solution(a, b, c, d):
    answer = 0
    dice = [0] * 7
    
    for i in [a, b, c, d]:
        dice[i] += 1
        
    if max(dice) == 4:
        answer = dice.index(4) * 1111
    elif max(dice) == 3:
        answer = (10 * dice.index(3) + dice.index(1)) ** 2
    elif max(dice) == 1:
        answer = min(a, b, c, d)
    elif max(dice) == 2 and (1 not in dice):
        tmp = list(filter(lambda x : dice[x] == 2, range(7)))
        answer = (tmp[0] + tmp[1]) * abs(tmp[0] - tmp[1])
    else:
        tmp = list(filter(lambda x : dice[x] == 1, range(7)))
        answer = tmp[0] * tmp[1]
        
    return answer