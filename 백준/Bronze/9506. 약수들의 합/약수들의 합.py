while True:
    n = int(input())
    if n == -1:
        break
    fac = []
    fac_sum = 0
    for i in range(1, n):
        if n % i == 0:
            fac.append(i)
            fac_sum += i
    if fac_sum != n:
        print(f'{n} is NOT perfect.')
    else:
        print(f'{n} = ', end='')
        for j in range(len(fac) - 1):
            print(f'{fac[j]} + ', end='')
        print(fac[-1])

