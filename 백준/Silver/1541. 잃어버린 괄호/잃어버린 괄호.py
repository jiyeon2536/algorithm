# 잃어버린 괄호

# 1. 마이너스 뒤를 전부 묶어서 가장 크게 만드는 게 좋음

f = input()

res = 0
is_minus = False
tmp = ''
for i in f:
    if i.isdigit():
        tmp += i
        continue
    if i == '-' and is_minus == False:
        is_minus = True
        res += int(tmp)
        tmp = ''
        continue
    elif i == '-' and is_minus:
        res -= int(tmp)
        tmp = ''
        continue
    elif i == '+' and is_minus:
        res -= int(tmp)
        tmp = ''
        continue
    elif i == '+' and is_minus == False:
        res += int(tmp)
        tmp = ''
        continue

if is_minus:
    res -= int(tmp)
else:
    res += int(tmp)

print(res)