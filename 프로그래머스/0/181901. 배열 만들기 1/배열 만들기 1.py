def solution(n, k):
    answer = []
    for i in range(1, n+1):
        if not i % k:
            answer.append(i)
    return answer