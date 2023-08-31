def hanoi(n, start, end):
    # 기저 조건
    if n == 1:
        print(start, end)
        return
    p = 6 - (start + end)
    hanoi(n-1, start, p)
    print(start, end)
    hanoi(n-1, p, end)


N = int(input())
hanoi_top = 2**N-1
print(hanoi_top)
hanoi(N, 1, 3)