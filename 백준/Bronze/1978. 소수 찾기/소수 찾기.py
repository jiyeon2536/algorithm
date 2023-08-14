N = int(input())

def prime(num1):
    if num1 == 1:
        return False
    else:
        for i in range(2, num1):
            if num1 % i == 0:
                return False
        return True

nums = list(map(int, input().split()))

cnt = 0
for n in nums:
    if prime(n):
        cnt += 1

print(cnt)
