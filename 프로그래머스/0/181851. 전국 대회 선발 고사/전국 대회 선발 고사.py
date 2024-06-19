def solution(rank, attendance):
    arr = sorted([[r, i] for i, r in enumerate(rank) if attendance[i]])
    return 10000 * arr[0][1] + 100 * arr[1][1] + arr[2][1]