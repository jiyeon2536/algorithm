import sys
t = int(sys.stdin.readline().rstrip())
for tc in range(t):
    n = int(sys.stdin.readline().rstrip())
    scores = [0 for _ in range(n + 1)]
    for i in range(n):
        idx, val = map(int, sys.stdin.readline().rstrip().split())
        scores[idx] = val
    selected = 1    # 1등은 무조건 뽑힌다
    mn = scores[1]  # 앞에 나온 순위중에 제일 작은 아이를 갱신하면서 가고 그거보다 작으면 넣고 갱신
    for i in range(2, n+1):
        if scores[i] < mn:
            selected += 1
            mn = scores[i]

    print(selected)