N, B = input().split()
B = int(B)

num_sum = 0

for i in range(len(N)):
    if chr(65) <= N[i] <= chr(90):
        num_sum += (ord(N[i]) - 55) * (B ** (len(N) - 1 - i))
    else:
        num_sum += int(N[i]) * (B ** (len(N) - 1 - i))

print(num_sum)