def solution(numbers):
    answer = []
    for num in numbers:
        i = 1
        while True:
            if (num & i) == 0:
                num |= i
                num ^= (i >> 1)
                break
            i <<= 1
        answer.append(num)
        
    return answer