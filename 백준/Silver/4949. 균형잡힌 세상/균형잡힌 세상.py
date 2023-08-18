while True:
    sentence = input()
    if sentence == '.':
        break
    else:
        stack = []
        res = 'no'
        
        for a in sentence:
            if a in '([':
                stack.append(a)
            elif a in ')]':
                if len(stack) == 0:
                    stack.append(a)
                    break
                else:
                    if a == ')' and stack[-1] == '(':
                        stack.pop()
                    elif a == ']' and stack[-1] == '[':
                        stack.pop()
                    else:
                        break

        if len(stack) == 0:
            res ='yes'

        print(res)
