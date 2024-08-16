from collections import Counter

def solution(want, number, discount):
    answer = 0
    d_want = dict(zip(want, number))
    if len(discount) < 10:
        return 0
    
    for i in range(len(discount) - 9):
        if d_want == Counter(discount[i:i+10]) :
            answer += 1

    return answer