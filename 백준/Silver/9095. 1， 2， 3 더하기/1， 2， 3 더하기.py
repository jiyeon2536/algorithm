# adding 1s, 2s, and 3s
def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return f(n - 1) + f(n - 2) + f(n - 3)

import sys
inp = sys.stdin.readline
t = int(inp())
for tc in range(t):
    n = int(inp())

    res = f(n)
    print(res)