import re

def solution(files):
    p = re.compile('(\d+)')
    
    new = [p.split(file) for file in files]
    new.sort(key=lambda x: int(x[1]))
    new.sort(key=lambda x: x[0].upper())
            
    return [''.join(i) for i in new]