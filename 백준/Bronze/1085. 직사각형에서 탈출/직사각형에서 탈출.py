# 직사각형에서 탈출
import sys
x, y, w, h = map(int, sys.stdin.readline().split())
# x y 는 한수의 현재 위치
# wh 는 가장 큰 좌표

mn_x = 100000000
mn_y = 100000000

if (w // 2) >= x:
    mn_x = x
else:
    mn_x = (w - x)
if (h // 2) >= y:
    mn_y = y
else:
    mn_y = (h - y)

print(min(mn_x, mn_y))