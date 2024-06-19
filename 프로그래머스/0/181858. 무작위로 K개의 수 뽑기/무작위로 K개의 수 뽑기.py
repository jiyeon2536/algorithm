def solution(arr, k):
    answer = []
    for a in arr:
        if a not in answer:
            answer.append(a)
    if len(answer) > k:
        return answer[:k]
    elif len(answer) < k:
        answer += [-1] * (k - len(answer))
        return answer
    return answer