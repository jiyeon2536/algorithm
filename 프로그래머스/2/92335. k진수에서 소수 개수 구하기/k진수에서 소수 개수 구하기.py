def int_to_k(integer, k):
    res = ''
    while integer > 0:
        integer, remainder = divmod(integer, k)
        res += str(remainder)
    return res[::-1]


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True


def solution(n, k):
    answer = 0
    for i in int_to_k(n, k).split('0'):
        if i.isdigit() and is_prime(int(i)):
            answer += 1
            
    return answer