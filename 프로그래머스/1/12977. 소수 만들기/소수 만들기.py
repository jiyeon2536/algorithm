from itertools import combinations
def pn(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True
    
def solution(nums):
    answer = 0
    arr = [sum(i) for i in combinations(nums, 3)]
    for a in arr:
        if pn(a):
            answer += 1
            
    return answer