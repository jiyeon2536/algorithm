def solution(arr, idx):
    for i, val in enumerate(arr):
        if i >= idx and val == 1:
            return i
    return -1