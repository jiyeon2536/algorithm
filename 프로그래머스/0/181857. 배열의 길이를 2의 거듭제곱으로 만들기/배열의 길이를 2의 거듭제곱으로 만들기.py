def solution(arr):
    answer = []
    for i in range(10):
        if 2**i == len(arr):
            return arr
        elif 2**i < len(arr) < 2**(i+1):
            d = 2**(i+1) - len(arr)
            return arr + [0] * d
