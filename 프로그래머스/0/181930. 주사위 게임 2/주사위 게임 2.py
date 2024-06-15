def solution(a, b, c):
    answer = 0
    one = (a + b + c)
    two = (a ** 2 + b ** 2 + c ** 2)
    three = (a ** 3 + b ** 3 + c ** 3)
    if a == b == c:
        answer = one * two * three
    elif a != b and b != c and a != c:
        answer = one
    else:
        answer = one * two
    return answer