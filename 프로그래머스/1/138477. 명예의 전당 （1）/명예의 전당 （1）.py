def solution(k, score):
    honor = []
    res = []
    for s in score:
        if len(honor) < k:
            honor.append(s)
        else:
            if honor[0] <= s:
                honor.pop(0)
                honor.append(s)
        honor.sort()
        res.append(honor[0])
    return res