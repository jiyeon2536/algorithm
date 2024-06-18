def solution(strArr):
    lend = dict(zip([i for i in range(1, 31)], [0 for _ in range(30)]))
    for s in strArr:
        lend[len(s)] += 1
    return max(lend.values())