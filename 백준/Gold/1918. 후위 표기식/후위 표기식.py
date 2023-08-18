pre = input()

stack = []
res = ''
for i in pre:
    if i == '(':
        stack.append(i)
    elif i in '+-':
        while len(stack) and stack[-1] in '+-*/':
            res += stack.pop()
        stack.append(i)
    elif i in '*/':
        while len(stack) and stack[-1] in '*/':
            res += stack.pop()
        stack.append(i)
    elif i == ')':
        while len(stack) and stack[-1] != '(':
            res += stack.pop()
        stack.pop()
    elif ord('A') <= ord(i) <= ord('Z'):
        res += i

while len(stack):
    res += stack.pop()

print(res)
