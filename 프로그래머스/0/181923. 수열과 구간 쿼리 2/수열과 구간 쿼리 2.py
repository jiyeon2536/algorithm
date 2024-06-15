def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        a = min([arr[i] if (arr[i] > k) else float('INF') for i in range(s, e + 1)])
        answer.append(a if a != float('INF') else -1)
    return answer