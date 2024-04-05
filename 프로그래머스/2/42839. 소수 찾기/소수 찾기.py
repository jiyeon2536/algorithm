from itertools import permutations

def isPrime(num):
    for i in range(2, num) :
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    n = len(numbers)
    memo = []
    
    for i in range(1, n + 1):
        perarr = list(permutations(numbers, i))
        for per in perarr:
            tmp = ''.join(list(per))
            if tmp[0] == '0' or tmp == '1':
                continue
            target = int(tmp)
            if target not in memo : 
                memo.append(target)            
                if (isPrime(target)):
                    answer += 1
    
    return answer