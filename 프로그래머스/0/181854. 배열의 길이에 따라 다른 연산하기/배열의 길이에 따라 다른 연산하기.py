def solution(arr, n):
    answer = []
    if len(arr) % 2: # 홀수면
        for i in range(len(arr)):
            if not i % 2: # 짝수 인덱스에
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    else:
        for i in range(len(arr)):
            if i % 2:
                answer.append(arr[i] + n)
            else:
                answer.append(arr[i])
    return answer
                