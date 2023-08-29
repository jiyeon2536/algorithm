# 문자열 집합
import sys
n, m = map(int, sys.stdin.readline().split())
s = [sys.stdin.readline() for _ in range(n)]
cnt = 0
for _ in range(m):
    if sys.stdin.readline() in s:
        cnt += 1

print(cnt)