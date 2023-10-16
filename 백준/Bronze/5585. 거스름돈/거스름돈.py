# 거스름돈

n = 1000 - int(input())  # 받아야 할 돈

coin = 0
while n > 0:
    if n >= 500:
        coin += (n // 500)
        n %= 500
    elif n >= 100:
        coin += (n // 100)
        n %= 100
    elif n >= 50:
        coin += (n // 50)
        n %= 50
    elif n >= 10:
        coin += (n // 10)
        n %= 10
    elif n >= 5:
        coin += (n // 5)
        n %= 5
    else:
        coin += n
        n = 0

print(coin)
