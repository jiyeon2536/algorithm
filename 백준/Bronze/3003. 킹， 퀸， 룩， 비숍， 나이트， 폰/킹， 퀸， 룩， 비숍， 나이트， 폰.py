pieces = list(map(int, input().split()))
suppose = [1, 1, 2, 2, 2, 8]
aors = []

for i in range(6):
    aors.append(suppose[i] - pieces[i])

print(*aors)