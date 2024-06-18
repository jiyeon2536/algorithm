def solution(arr):
    s = 0
    e = len(arr) - 1
    while s <= e:
        if arr[s] == 2 and arr[e] == 2:
            break
        if arr[s] != 2:
            s += 1
        if arr[e] != 2:
            e -= 1
    if s > e:
        return [-1]
    return arr[s:e + 1]