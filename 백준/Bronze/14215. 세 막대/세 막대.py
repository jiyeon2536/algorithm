import sys
a, b, c = map(int, sys.stdin.readline().strip().split())

def triangle(a, b, c):
    if (a+b+c) - max(a,b,c) > max(a,b,c):
        return a + b + c
    else:
        # a 가 최대일 때
        if a > b and a > c:
            a -= 1
        # b 가 최대일 때
        elif b > a and b > c:
            b -= 1
        # c 가 최대일 때
        elif c > a and c > b:
            c -= 1
        return triangle(a, b, c)


print(triangle(a, b, c))

