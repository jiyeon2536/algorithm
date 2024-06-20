def solution(left, right):
    # 약수의 개수를 구한다
    # 정수의 제곱이면 홀수 아니면 짝수임
    answer = 0
    for i in range(left, right+1):
        if (i ** 0.5) % 1 == 0:
            answer -= i
        else:
            answer += i
    return answer