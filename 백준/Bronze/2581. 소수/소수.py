M = int(input())
N = int(input())

def prime(num1):
    if num1 == 1:
        return False
    else:
        for i in range(2, num1):
            if num1 % i == 0:
                return False
        return True

pr_sum = 0
pr_mn = N
for j in range(M, N+1):
    if prime(j):
        pr_sum += j
        if pr_mn > j:
            pr_mn = j


if pr_sum == 0:
    print(-1)
else:
    print(pr_sum)
    print(pr_mn)
