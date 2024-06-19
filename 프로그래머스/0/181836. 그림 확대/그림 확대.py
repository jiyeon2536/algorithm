def solution(picture, k):
    answer = []
    for row in picture:
        tmp = ''
        for col in range(len(row)):
            tmp += row[col] * k
        for _ in range(k):
            answer.append(tmp)
    return answer