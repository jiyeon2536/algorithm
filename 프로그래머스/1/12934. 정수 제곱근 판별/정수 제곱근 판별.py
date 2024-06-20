def solution(n):
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return (n**(1/2) + 1) ** 2 if not n ** (1/2) % 1 else -1 