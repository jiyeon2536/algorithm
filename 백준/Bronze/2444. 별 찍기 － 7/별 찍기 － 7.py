N = int(input())

# 위쪽 공백: N-line 별수 2line -1
for i in range(1, N + 1):
    print(' ' * (N - i), end='')
    print('*' * (2*i - 1), end='')
    print()

# 아래쪽 공백: line 별수: 1-7 2-5 3-3 4-1
for j in range(N-1, 0, -1):
    print(' ' * (N - j), end='')
    print('*' * (2*j - 1), end='')
    print()