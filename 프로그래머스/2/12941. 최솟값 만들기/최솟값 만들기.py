def solution(A,B):
    A, B = sorted(A, reverse=True), sorted(B)
    answer = 0
    for i in range(len(A)):
        answer += A[i] * B[i]
    return answer