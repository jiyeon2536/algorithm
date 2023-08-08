S = input().strip()

cnt = 0
if len(S) == 0:
    print(0)
else:
    for i in S:
        if i == ' ':
            cnt += 1
    print(cnt + 1)