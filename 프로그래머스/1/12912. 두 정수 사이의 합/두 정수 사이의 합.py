def solution(a, b):
    return sum([i for i in range(sorted([a, b])[0],sorted([a, b])[1]+1)])