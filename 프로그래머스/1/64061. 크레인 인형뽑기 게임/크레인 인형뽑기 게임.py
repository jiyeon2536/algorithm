def solution(board, moves):
    answer = 0
    stk = []
    
    # 열을 순회해서 처음으로 나오는 숫자. 
    # 그리고 그자리는 0으로 바꾼다.
    # 건져올린 아이가 -1 과 같다면 pop하고 answer+=2
    
    n = len(board)
    for m in moves:
        m -= 1  # 인덱스로 변환
        for i in range(n):
            if board[i][m] != 0:
                if len(stk) and board[i][m] == stk[-1]:
                    stk.pop()
                    answer += 2
                else:
                    stk.append(board[i][m])
                
                board[i][m] = 0
                break
    return answer