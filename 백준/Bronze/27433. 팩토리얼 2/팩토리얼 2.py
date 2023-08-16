n = int(input())

def fact(i):
    if i == 1 or i == 0:
        return 1
    else:
        return i * fact(i - 1)

print(fact(n))