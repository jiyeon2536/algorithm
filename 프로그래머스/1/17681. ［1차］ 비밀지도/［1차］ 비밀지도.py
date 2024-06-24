def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        row = bin(i|j)[2:].zfill(n)
        answer.append(row.replace('0', ' ').replace('1', '#'))
    return answer