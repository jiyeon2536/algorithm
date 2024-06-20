def solution(arr, query):
    for i in range(len(query)):
        if not i % 2: # 짝수인 경우
            arr = arr[:query[i] + 1] # 앞만 남긴다
        else:
            arr = arr[query[i]:] # 뒤만 남긴다
    return arr