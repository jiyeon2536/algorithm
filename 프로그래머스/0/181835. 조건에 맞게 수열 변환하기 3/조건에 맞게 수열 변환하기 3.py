def solution(arr, k):
    if k % 2:
        return [k * i for i in arr]
    return [k + i for i in arr]
