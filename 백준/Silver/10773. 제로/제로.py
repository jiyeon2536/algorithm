k = int(input())

stack = []

for i in range(k):
    n = int(input())
    if n == 0:
        if len(stack) == 0:
            break
        else:
            stack.pop()
    else:
        stack.append(n)
res = 0
while len(stack):
    res += stack.pop()

print(res)