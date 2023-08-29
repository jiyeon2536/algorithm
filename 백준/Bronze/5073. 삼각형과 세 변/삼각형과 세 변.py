# triangles
import sys
while True:
    a, b, c = map(int, sys.stdin.readline().strip().split())
    if a == b == c == 0:
        break
    else:
        if (a + b + c) - max(a, b, c) <= max(a, b, c):
            print('Invalid')
        elif a == b == c:
            print('Equilateral')
        elif a != b and b != c and a != c:
            print('Scalene')
        else:
            print('Isosceles')


