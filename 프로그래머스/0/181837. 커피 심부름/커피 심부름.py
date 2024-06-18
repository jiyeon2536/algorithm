def solution(order):
    answer = 0
    for o in order:
        if 'am' in o:
            answer += 4500
        elif 'cafe' in o:
            answer += 5000
        else:
            answer += 4500
    return answer