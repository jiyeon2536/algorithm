def solution(s):
    answer = True
    stack = []
    for i in range(len(s)) :
        if s[i] == '(' :
            stack.append(s[i])
        elif s[i] == ')':
            if len(stack) == 0:
                return False
            if stack[-1] == ')':
                stack.append(s[i])
            elif stack[-1] == '(':
                stack.pop()
    if len(stack) > 0:
        return False
    
    return True