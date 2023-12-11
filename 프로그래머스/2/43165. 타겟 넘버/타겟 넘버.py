def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(depth, total):
        nonlocal answer
        if depth == n-1:
            if total == target:
                answer += 1
            return
        dfs(depth + 1, total + numbers[depth + 1])
        dfs(depth + 1, total - numbers[depth + 1])
        
    visited = [False for _ in range(n)]
    
    total = 0
    dfs(0, numbers[0])
    dfs(0, -numbers[0])
    
    
    return answer