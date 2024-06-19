def solution(arr, k):
    answer = []
    for a in arr:
        if a not in answer:
            answer.append(a)
        if len(answer) >= k:
            break
    return answer + [-1] * (k - len(answer))