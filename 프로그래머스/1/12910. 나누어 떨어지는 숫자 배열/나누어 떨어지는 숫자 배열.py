def solution(arr, divisor):
    return sorted([el for el in arr if not el % divisor]) or [-1]