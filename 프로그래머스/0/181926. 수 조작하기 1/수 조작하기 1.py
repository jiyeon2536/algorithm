def solution(n, control):
    control = control.replace('w', '+1')
    control = control.replace('s', '-1')
    control = control.replace('d', '+10')
    control = control.replace('a', '-10')
    return eval(str(n)+control)