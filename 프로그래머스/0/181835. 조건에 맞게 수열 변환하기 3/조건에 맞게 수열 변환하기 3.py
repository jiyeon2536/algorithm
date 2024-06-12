def solution(arr, k):
    return [k * i if k % 2 else k + i for i in arr]
