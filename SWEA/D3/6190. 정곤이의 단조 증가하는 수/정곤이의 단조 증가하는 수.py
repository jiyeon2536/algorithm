t = int(input())

for tc in range(1, t+1):
    n = int(input())
    a = list(map(int, input().split()))

    mx_mul = 0
# 서로서로 다 곱하고 (자기자신이면 제외)
# 그거중에 그 원소들이 단조증가하면
# 그 중에서 최대값을 구하라
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                continue
            else:
                tmp = str(a[i] * a[j])
                for m in range(1, len(tmp)):
                    if int(tmp[m]) < int(tmp[m-1]):
                        break
                else:
                    if mx_mul <= int(tmp):
                        mx_mul = int(tmp)

    if mx_mul == 0:
        print(f'#{tc}', -1)
    else:
        print(f'#{tc} {mx_mul}')

