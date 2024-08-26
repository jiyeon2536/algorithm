def solution(numbers):
    l = len(numbers)
    answer = [-1 for _ in range(l)]
    stk = []
    
    for i in range(l - 1, -1, -1): 
        while stk:
            if stk[-1] > numbers[i]:
                answer[i] = stk[-1]
                stk.append(numbers[i])
                break
            else:
                stk.pop()
        if not stk:
            stk.append(numbers[i])
            continue
    
    return answer