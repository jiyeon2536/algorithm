from itertools import combinations
def solution(number):
    answer = 0
    for t in list(combinations(number, 3)):
        if sum(t) == 0:
            answer += 1
    return answer