t = int(input())
for i in range(t):
    parenthesis = input()

    match = 0
    stack = []
    res = 'YES'
    for p in parenthesis:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if len(stack):
                stack.pop()
            else:
                res = 'NO'
                break
    if len(stack) != 0:
        res = 'NO'

    print(res)