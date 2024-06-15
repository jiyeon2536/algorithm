def solution(code):
    mode = False
    ret = ''
    for i in range(len(code)):
        if code[i] == '1':
            mode = not mode
        elif (not mode) and (not i % 2):
            ret += code[i]
        elif mode and i % 2:
            ret += code[i]
    if ret == '':
        return 'EMPTY'
    return ret