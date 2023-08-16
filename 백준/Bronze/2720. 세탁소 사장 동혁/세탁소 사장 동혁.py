N = int(input())

for i in range(N):
    change = int(input())

    q = change // 25
    change = change % 25
    d = change // 10
    change = change % 10
    n = change // 5
    p = change % 5

    print(q, d, n, p)