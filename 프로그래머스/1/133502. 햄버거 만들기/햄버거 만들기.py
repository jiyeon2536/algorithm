def solution(ingredient):
    answer = 0
    stk = []
    
    for i in ingredient:
        stk.append(i)
        if stk[-4:] == [1, 2, 3, 1]:
            del stk[-4:]
            answer += 1

    return answer