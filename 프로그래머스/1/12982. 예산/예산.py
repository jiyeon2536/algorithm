def solution(d, budget):
    answer = 0
    for p in sorted(d):
        budget -= p
        if budget < 0:
            break
        answer += 1
    return answer