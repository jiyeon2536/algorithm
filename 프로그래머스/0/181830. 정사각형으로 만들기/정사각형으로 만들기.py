def solution(arr):
    row = len(arr)
    col = len(arr[0])
    if row < col:
        for _ in range(col-row):
            arr.append([0 for _ in range(col)])
    elif col < row:
        for a in arr:
            a += ([0] * (row - col))
    return arr