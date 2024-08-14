def solution(n, left, right):
    answer = []
    idx = left
    while idx <= right:
        answer.append(max(idx // n, idx % n) + 1)
        idx += 1
    return answer
        