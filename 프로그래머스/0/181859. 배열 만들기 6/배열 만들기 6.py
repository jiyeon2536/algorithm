def solution(arr):
    stk = []
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        else:
            if stk[-1] == arr[i]:
                stk.pop()
            else:
                stk.append(arr[i])
    return stk or [-1]