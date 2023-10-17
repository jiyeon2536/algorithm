# 뒤집기

group0 = 0
group1 = 0

s = input()

is_zero = False
is_one = False

for i in s:
    if i == '0' and is_one:
        group1 += 1
        is_one = False
        is_zero = True
    elif i == '1' and is_zero:
        group0 += 1
        is_zero = False
        is_one = True
    elif i == '0':
        is_zero = True
    elif i == '1':
        is_one = True

# 마지막에
if is_zero:
    group0 += 1
elif is_one:
    group1 += 1

print(min(group0, group1))