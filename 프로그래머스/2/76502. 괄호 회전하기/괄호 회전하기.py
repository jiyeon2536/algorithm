# 정적으로 괄호유효성검사
def is_valid(string):
    stk = []
    for i in string:
        if i in ('[', '(', '{'):
            stk.append(i)
        else:
            # 닫힌 괄호인데 스택에 없으면 틀림
            if not stk:
                return False 
            if i == ']' and stk.pop() != '[':
                return False
            elif i == '}' and stk.pop() != '{':
                return False
            elif i == ')' and stk.pop() != '(':
                return False
    # 끝났는데 남아있으면 틀림
    if stk:
        return False
    return True

def solution(s):
    answer = 0
    
    # s를 왼쪽으로 i만큼 움직인다 == 
    for i in range(len(s)):
        # 여기서 string 을 가공하여 넘겨주기
        new_s = s[i:] + s[:i]
        if is_valid(new_s):
            answer += 1
        
    return answer