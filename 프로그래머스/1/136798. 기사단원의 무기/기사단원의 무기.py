# 약수의 개수 구하기
def divisor(n):
    res = 0
    sq = n ** 0.5
    # 제곱수라면
    if (sq % 1) == 0:
        for i in range(1, int(sq)):
            if n % i == 0:
                res += 1
        res = res * 2 + 1
    # 제곱수가 아니라면
    else:
        for i in range(1, int(sq) + 1):
            if n % i == 0:
                res += 1
        res *= 2
    return res

def solution(number, limit, power):
    arr = []
    for i in range(1, number + 1):
        d = divisor(i)
        if d > limit:
            arr.append(power)
        else:
            arr.append(d)

    return sum(arr)