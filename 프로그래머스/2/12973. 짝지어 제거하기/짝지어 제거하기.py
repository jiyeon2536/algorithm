def solution(s):
    stk = []
    
    for ch in s:
        if stk and ch == stk[-1]:
            stk.pop()
        else:
            stk.append(ch)

    return 0 if stk else 1