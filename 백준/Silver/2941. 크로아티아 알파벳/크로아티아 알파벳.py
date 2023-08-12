word = input()

cnt = len(word)
stack = [word[0]]
for i in word:
    if i == '=':
        if len(stack) > 1 and stack[-2] == 'd' and stack[-1] =='z':
            cnt -= 2
            stack.append(i)
        else:
            cnt -= 1
            stack.append(i)
    elif i == '-':
        cnt -= 1
        stack.append(i)
    elif i == 'j' and (stack[-1] == 'n' or stack[-1] == 'l'):
        cnt -= 1
        stack.append(i)
    else:
        stack.append(i)

print(cnt)