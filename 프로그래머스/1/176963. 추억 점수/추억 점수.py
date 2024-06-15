def solution(name, yearning, photo):
    score = dict(zip(name, yearning))
    answer = []
    for p in photo:
        sc = 0
        for person in p:
            if person in score:
                sc += score[person]
        answer += [sc]
    return answer