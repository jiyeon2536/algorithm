word = input()

# change the alphabet into the number corresponding
alph = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
nums = ''
for alp in word:
    for i in range(len(alph)):
        if alp in alph[i]:
            nums += str(i + 2)

sum_sec = 0
for num in nums:
    sum_sec += int(num) + 1

print(sum_sec)