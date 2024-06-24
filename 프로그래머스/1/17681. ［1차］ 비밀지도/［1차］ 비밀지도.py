def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = ''
        for j in range(n):
            if str(bin(arr1[i]))[2:].zfill(n)[j] == '1' or str(bin(arr2[i]))[2:].zfill(n)[j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer