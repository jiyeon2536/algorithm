def solution(n, m):
    answer = [0, 0]
    # 최대공약수 = 둘의 약수인데 제일 큰거 - 
        # 둘 중 더 작은 수의 약수 중에 큰 거 순서로 큰 수의 약수인지
    small = sorted([i for i in range(1, min(n, m) + 1) if min(n, m) % i == 0], reverse=True)
    print(small)
    for s in small:
        if max(n, m) % s == 0:
            answer[0] = s
            break
    # 최소공배수 = 둘의 배수인데 제일 작은거
    for i in range(1, n * m + 1):
        if i % n == 0 and i % m == 0:
            answer[1] = i
            break
    
    return answer