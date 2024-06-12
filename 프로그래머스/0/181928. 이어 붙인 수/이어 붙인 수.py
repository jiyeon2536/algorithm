def solution(num_list):
    even = ''.join([str(n) for n in num_list if not n % 2])
    odd = ''.join([str(n) for n in num_list if n % 2])
    return int(odd) + int(even)