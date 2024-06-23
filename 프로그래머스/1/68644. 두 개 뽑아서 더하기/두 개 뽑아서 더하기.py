from itertools import combinations
def solution(numbers):
    answer = []
    for c in combinations(numbers, 2):
        print(c)
        answer.append(sum(c))
    return sorted(list(set(answer)))