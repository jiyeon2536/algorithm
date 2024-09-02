def solution(prices):
    answer = [0 for _ in prices]
    
    for i, price in enumerate(prices):
        for j in range(i, len(prices) - 1):
            if prices[j] < price:
                break
            answer[i] += 1
    
    answer[-1] = 0
    
    return answer