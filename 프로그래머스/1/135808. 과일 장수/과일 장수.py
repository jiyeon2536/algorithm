def solution(k, m, score):
    answer = 0
    # 마지막 인덱스는 사과의 전체개수에서 나머지를 뺀만큼
    last = len(score) - (len(score) % m)
    score.sort(reverse=True)
    for s in range(0, last, m):
        answer += min(score[s: s+m]) * m
    return answer