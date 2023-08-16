n = int(input())

def dotsinaline(k):
    if k == 0:
        return 2
    else:
        return dotsinaline(k-1) + (2 ** (k-1))

print(dotsinaline(n) ** 2)