def solution(nums):
    kind = {}
    for k in nums:
        if k not in kind:
            kind[k] = 1
    return min(len(nums)//2, len(kind.keys()))
    
