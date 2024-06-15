def solution(num_list):
    arr = [i for i, num in enumerate(num_list) if num < 0]
    if arr:
        return min(arr)
    else:
        return -1