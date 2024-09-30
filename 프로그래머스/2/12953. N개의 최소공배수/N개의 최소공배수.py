def gcd(a, b):
    res = 0
    while b != 0:
        res = a % b
        a = b
        b = res
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def solution(arr):
    res = arr[0]
    for i in range(len(arr)) :
        res = lcm(res, arr[i])
    
    return res