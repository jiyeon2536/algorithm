def solution(arr, queries):
    for [s, e, k] in queries:
        if k == 0 :
            return arr
        for i in range(s, e+1):
            if k != 0 and not i % k:
                arr[i] += 1
    return arr