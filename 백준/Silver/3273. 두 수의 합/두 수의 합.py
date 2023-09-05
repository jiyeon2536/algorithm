# sumX
import sys
n = int(sys.stdin.readline().strip())   # n 개의 정수가 주어짐
a = sorted(list(map(int, sys.stdin.readline().strip().split())))    # 숫자열
x = int(sys.stdin.readline().strip())   # 합이 x 가 되는 수 찾기

st = 0
ed = (n-1)  # 끝에서부터 탐색

cnt = 0
while st < ed:
    if a[st] + a[ed] == x:
        cnt += 1
        st += 1
    elif a[st] + a[ed] > x:
        ed -= 1
    elif a[st] + a[ed] < x:
        st += 1

print(cnt)
