# securing the barn
import sys
l, c = map(int, sys.stdin.readline().split())
arr = sorted(list(sys.stdin.readline().split()))


board = [-1] * l
visited = [False for _ in range(c)]
vowel = 0
consonant = 0

def password(row, last):
    global vowel
    global consonant
    if row == l:
        for i in board:
            if i in 'aeiou':
                vowel = 1
            elif i in 'bcdfghjklmnpqrstvwxyz':
                consonant += 1
        if vowel > 0 and consonant > 1:
            print(''.join(board))
        return
    for col in range(last, c):
        if visited[col] == False:
            visited[col] = True
            board[row] = arr[col]
            password(row+1, col)
            visited[col] = False
            vowel = 0
            consonant = 0

password(0, 0)

