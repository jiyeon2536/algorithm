# 대지
import sys
n = int(sys.stdin.readline())
x_ls = []
y_ls = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().strip().split())
    x_ls.append(x)
    y_ls.append(y)

print((max(x_ls)-min(x_ls)) * (max(y_ls) - min(y_ls)))