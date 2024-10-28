def fac(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def solution(n, k):
    ans = []
    numbers = list(range(1, n + 1))  
    k -= 1  

    for i in range(n, 0, -1):
        child = fac(i - 1)  
        index = k // child  
        ans.append(numbers.pop(index))  
        k %= child  

    return ans
