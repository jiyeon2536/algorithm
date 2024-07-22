def solution(s):
    stk = []
    arr = [ch for ch in s]
    
    while arr:
        tmp = arr.pop()
        if stk and tmp == stk[-1]:
            stk.pop()
        else:
            stk.append(tmp)

    return 0 if stk else 1