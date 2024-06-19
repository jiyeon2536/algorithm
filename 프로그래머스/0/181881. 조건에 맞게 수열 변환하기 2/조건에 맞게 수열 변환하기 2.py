def solution(arr):
    # 모든 요소가 50 이상의 홀수 또는 50 미만의 짝수가 되면 끝남
    answer = 0
    # 요소마다 하고 가장 카운트가 높은 아이의 카운트를 반납
    for a in arr:
        c = 0
        while (a >= 50 and not a % 2) or (a < 50 and a % 2):
            c += 1
            if (a >= 50 and not a % 2):
                a /= 2
            elif (a < 50 and a % 2):
                a = a * 2 + 1
        answer = max(answer, c)
    return answer