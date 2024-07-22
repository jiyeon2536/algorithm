def solution(n):
    answer = 0
    
    arr = [i + 1 for i in range(n)]
    start, end = 0, 0
    total = 1
    
    while start <= end and end < len(arr):
        if total == n:
            answer += 1
            total -= arr[start]
            start += 1
            
        elif total < n:
            end += 1
            total += arr[end]
            
        elif total > n:
            total -= arr[start]
            start += 1
    
    return answer